## Installation & Setup
The following instructions cover everything necessary to setup your Raspberry Pi for this project. I tried to script out a good chunk of system installation stuff to help keep things fairly simple. With that said, I welcome feedback about how to make this better.

#### Step 1: Clone this repository

```
git clone https://github.com/projectweekend/Pi-Box.git
```

#### Step 2: Run install script

From the project directory `Pi-Camera-Time-Lapse/`, run the following command:

```
./install.sh
```

**NOTE:** This step will probably take several minutes to complete. When the script starts to install [Upstart](http://upstart.ubuntu.com/), you will receive a warning message. It will prompt you to type the following message to confirm the installation: `Yes, do as I say!`. You must type it exactly.

The install script will also prompt you to authorize your Dropbox account using this site I made: [http://raspberry-pi-box.herokuapp.com/](http://raspberry-pi-box.herokuapp.com/). It handles generating a key file you will need to save on your Raspberry Pi. The script will let you know where to save the file.
