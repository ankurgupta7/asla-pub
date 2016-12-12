# 2016-group-15
[![Build Status](https://travis-ci.com/jhu-oose/2016-group-15.svg?token=WPwURECkpN4xsLzZYqVc&branch=master)](https://travis-ci.com/jhu-oose/2016-group-15)

## Installing Dependencies
### Python and Packages
`sudo add-apt-repository ppa:fkrull/deadsnakes-python2.7`<br/>
`sudo apt-get update `<br/>
`sudo apt-get install python2.7`<br/>
`sudo apt-get install python-pip python2.7-dev libxext-dev build-essential` <br/>
`sudo pip install -U -r requirements.txt` <br/>
### libs
`sudo add-apt-repository ppa:ubuntu-toolchain-r/test` <br/>
`sudo apt-get update` <br/>
`sudo apt-get install libstdc++-4.9-dev` <br/>
`sudo apt-get install -q python-numpy python-scipy python-sklearn libstdc++6`
### Installing PyQt5
download Qt5.2 from http://sourceforge.net/projects/pyqt/files/sip/sip-4.16.5/sip-4.16.5.tar.gz <br/>
download SIP http://sourceforge.net/projects/pyqt/files/sip/sip-4.16.5/sip-4.16.5.tar.gz <br/>
download http://sourceforge.net/projects/pyqt/files/PyQt5/PyQt-5.3.2/PyQt-gpl-5.3.2.tar.gz/download <br/>

`chmod +x qt-opensource-linux-x64-5.3.1.run` <br/>
`./qt-opensource-linux-x64-5.3.1.run` <br/>
`sudo apt-get install build-essential` <br/>
`sudo apt-get install python-dev` <br/>
`sudo apt-add-repository ppa:ubuntu-sdk-team/ppa` <br/>
`sudo apt-get update` <br/>
`sudo apt-get install qtdeclarative5-dev` <br/>
`tar xvzf sip-4.16.5.tar.gz` <br/>
`cd sip-4.16.5` <br/>
`python configure.py` <br/>
`make` <br/>
`sudo make install` <br/>
`cd ..` <br/>
`tar xvzf PyQt-gpl-5.3.2.tar.gz` <br/>
`cd PyQt-gpl-5.3.2` <br/>
`python configure.py --qmake ~/Qt5.3.1/5.3/gcc_64/bin/qmake --sip-incdir ../sip-4.16.5/siplib` <br/>
`sudo ln -s /usr/include/python2.7 /usr/local/include/python2.7` <br/>
`make` <br/>
`sudo make install` <br/>

## Cloning the repo
`git clone git@github.com:jhu-oose/2016-group-15.git` <br/>

## Running Tests
Connect the Leap Motion <br/>
`cd 2016-group-15` <br/>
`nosetests asla/binary/ml_tools/tests/test_predict_service.py` <br/>
`nosetests asla/binary/ml_tools/tests/test_training_service.py` <br/>
`nosetests asla/server/binary_server_backend/tests/test_ASLAController.py` <br/>
`nosetests asla/server/binary_server_backend/tests/test_global_model_service.py` <br/>
`nosetests asla/server/flask_website/tests/test_binary_helper.py` <br/>
`nosetests asla/server/flask_website/tests/test_FlaskWebsiteBackend.py` <br/>
`nosetests asla/server/flask_website/tests/test_user_admin_service.py` <br/>
## Steps to Run UI 
* Connect the Leap Motion Device <br/>
* cd 2016-group-15/asla
* chmod u+x main.sh
* ./main.sh
