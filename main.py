import os

from dropbox.client import DropboxClient, ErrorResponse


DROPBOX_TOKEN = os.getenv('DROPBOX_TOKEN')


class Dropbox(object):

    def __init__(self, dropbox_token):
        self.delta_cursor = ""
        self.token = dropbox_token
        self.client = DropboxClient(dropbox_token)

    def get_delta(self):
        if self.delta_cursor:
            return self.client.delta(cursor=self.delta_cursor)
        return self.client.delta(cursor=None)

    def get_file(self, from_path):
        path_parts = from_path.split('/')
        directory = "/".join(path_parts[:-1])

        if not os.path.exists(directory):
            os.makedirs(directory)

        output_file = open(from_path, 'w+b')
        with self.client.get_file(from_path) as f:
            output_file.write(f.read())


def main():
    pass


if __name__ == '__main__':
    main()
