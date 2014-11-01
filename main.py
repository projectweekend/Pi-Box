import os
from time import sleep

import gevent
from dropbox.client import DropboxClient


DROPBOX_TOKEN_FILE = os.getenv('DROPBOX_TOKEN_FILE')
DELTA_CURSOR_FILE = os.getenv('DELTA_CURSOR_FILE')
PI_BOX_ROOT = os.getenv('PI_BOX_ROOT')


class PiBox(object):

    def __init__(self, dropbox_token, pi_box_root, delta_cursor_file=''):
        self.token = dropbox_token
        self.pi_box_root = pi_box_root
        self.client = DropboxClient(dropbox_token)
        self.delta_cursor_file = delta_cursor_file
        self.delta_cursor = self._read_cursor()

    def _full_local_path(self, path):
        return self.pi_box_root + path

    def _read_cursor(self):
        try:
            with open(self.delta_cursor_file, 'r') as f:
                return f.read()
        except IOError:
            return None

    def _save_cursor(self):
        try:
            with open(self.delta_cursor_file, 'w+') as f:
                f.write(self.delta_cursor)
        except IOError:
            pass

    def get_delta(self):
        response = self.client.delta(cursor=self.delta_cursor)
        self.delta_cursor = response['cursor']
        self._save_cursor()
        return response

    def get_file(self, from_path):
        output_file = open(self._full_local_path(from_path), 'w+b')
        with self.client.get_file(from_path) as f:
            output_file.write(f.read())

    def make_local_directory(self, path):
        local_path = self._full_local_path(path)
        if not os.path.exists(local_path):
            os.makedirs(local_path)


def main():
    with open(DROPBOX_TOKEN_FILE, 'r') as f:
        dropbox_token = f.read()

    pi_box = PiBox(dropbox_token=dropbox_token,
                    pi_box_root=PI_BOX_ROOT,
                    delta_cursor_file=DELTA_CURSOR_FILE)

    while True:
        delta = pi_box.get_delta()
        entries = delta['entries']

        while delta['has_more']:
            delta = pi_box.get_delta()
            entries.extend(delta['entries'])

        tasks = []
        for entry in entries:
            if entry[1]['is_dir']:
                pi_box.make_local_directory(entry[1]['path'])
            else:
                tasks.append(gevent.spawn(pi_box.get_file, entry[0]))

        gevent.joinall(tasks)

        sleep(5)


if __name__ == '__main__':
    main()
