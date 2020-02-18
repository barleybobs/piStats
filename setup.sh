#!/bin/bash
cd /home/pi
mkdir piStats
cd /piStats
git clone https://github.com/barleybobs/piStats
sudo pip install psutil
sudo pip install pathlib
sudo pip install termcolor
sudo pip install hurry.filesize
sudo apt-get install xterm
sudo apt-get install unclutter
