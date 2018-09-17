#!/bin/bash
cd ~/
sudo apt-get install build-essential checkinstall
sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev
wget https://www.python.org/ftp/python/3.6.0/Python-3.6.0.tgz
tar xzvf Python-3.6.0.tgz
cd Python-3.6.0/
./configure
make -j4
sudo make install
sudo pip3 install fauxmo
sudo pip3 install RPi.GPIO
sudo pip3 install pillow
cd ~/Desktop
sudo chmod +x controller.py
sudo chmod +x startAlexa.bat
