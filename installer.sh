#!/bin/bash
clear
echo "Starting install Python3.6..."

# Create destination folder

if python3.6 -V ; then
    echo "Python3.6 is install "
else
    sudo apt-get install software-properties-common
    sudo add-apt-repository ppa:deadsnakes/ppa
    sudo apt-get update
    sudo apt-get install python3.6
    
fi


clear
echo "Python3.6 installed !!!"
echo "Install Python Packages..."
sudo python3.6 -m pip install --upgrade pip
sudo python3.6 -m pip install --upgrade setuptools
sudo python3.6 -m pip install -r requirements.txt
sudo apt-get install redis-server


echo -ne '#####                     (33%)\r'
sleep 1
echo -ne '#############             (66%)\r'
sleep 1
echo -ne '#######################   (100%)\r'
echo -ne '\n'

clear
python3.6 bot.py

# Exit from the script with success (0)
exit 0

__ARCHIVE__
