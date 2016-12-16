#!/bin/bash

#Python and Packages
sudo add-apt-repository ppa:fkrull/deadsnakes-python2.7
sudo apt-get update
sudo apt-get install python2.7
sudo apt-get install python-pip python2.7-dev libxext-dev build-essential 
sudo pip install -U -r requirements.txt

#libs
sudo add-apt-repository ppa:ubuntu-toolchain-r/test
sudo apt-get update
sudo apt-get install libstdc++-4.9-dev
sudo apt-get install -q python-numpy python-scipy python-sklearn libstdc++6

#installing PyQt5
wget "http://sourceforge.net/projects/pyqt/files/sip/sip-4.16.5/sip-4.16.5.tar.gz"
wget "http://sourceforge.net/projects/pyqt/files/sip/sip-4.16.5/sip-4.16.5.tar.gz"
wget "http://sourceforge.net/projects/pyqt/files/PyQt5/PyQt-5.3.2/PyQt-gpl-5.3.2.tar.gz/download"

chmod +x qt-opensource-linux-x64-5.3.1.run
./qt-opensource-linux-x64-5.3.1.run
sudo apt-get install build-essential
sudo apt-get install python-dev
sudo apt-add-repository ppa:ubuntu-sdk-team/ppa
sudo apt-get update
sudo apt-get install qtdeclarative5-dev
tar xvzf sip-4.16.5.tar.gz
cd sip-4.16.5
python configure.py
make
sudo make install
cd ..
tar xvzf PyQt-gpl-5.3.2.tar.gz
cd PyQt-gpl-5.3.2
python configure.py --qmake ~/Qt5.3.1/5.3/gcc_64/bin/qmake --sip-incdir ../sip-4.16.5/siplib
sudo ln -s /usr/include/python2.7 /usr/local/include/python2.7
make
sudo make install
