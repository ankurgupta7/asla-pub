# 2016-group-15
[![Build Status](https://travis-ci.com/jhu-oose/2016-group-15.svg?token=WPwURECkpN4xsLzZYqVc&branch=master)](https://travis-ci.com/jhu-oose/2016-group-15)

## Installing Dependencies
### libs
`sudo add-apt-repository ppa:ubuntu-toolchain-r/test` <br/>
`sudo apt-get update` <br/>
`sudo apt-get install libstdc++-4.9-dev` <br/>
`sudo apt-get install -q python-numpy python-scipy python-sklearn libstdc++6`
### Python Packages
`git clone git@github.com:jhu-oose/2016-group-15.git` <br/>
`sudo pip install -U -r requirements.txt` <br/>
`sudo apt-get install python-pip python2.7-dev libxext-dev python-qt4 qt4-dev-tools build-essential` <br/>
## Running Tests
Connect the Leap Motion <br/>
`ASLAROOT=<project_root>/asla` <br/>
`cd $ASLAROOT` <br/>
`nosetests asla/binary/ml_tools/tests/test_predict_service.py` <br/>
`nosetests asla/binary/ml_tools/tests/test_training_service.py` <br/>
`nosetests asla/server/binary_server_backend/tests/test_ASLAController.py` <br/>
`nosetests asla/server/binary_server_backend/tests/test_global_model_service.py` <br/>
`nosetests asla/server/flask_website/tests/test_binary_helper.py` <br/>
`nosetests asla/server/flask_website/tests/test_FlaskWebsiteBackend.py` <br/>
`nosetests asla/server/flask_website/tests/test_user_admin_service.py` <br/>
## Steps to Run UI (may not work fully)
Connect the Leap Motion Device <br/>
`ASLAROOT=<project_root>/asla` <br/>
Open `$ASLAROOT` in PyCharm <br/>
Set `$ASLAROOT` as source directory in PyCharm <br/>
Run `$ASLAROOT/binary/user_ui/main.py` for user ui <br/>
Run `$ASLAROOT/binary/expert_ui/main.py` for expert ui <br/>
