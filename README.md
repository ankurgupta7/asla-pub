# 2016-group-15
[![Build Status](https://travis-ci.com/jhu-oose/2016-group-15.svg?token=WPwURECkpN4xsLzZYqVc&branch=master)](https://travis-ci.com/jhu-oose/2016-group-15)

## Installing Dependencies including PyQt5

`sudo asla/setup.sh` <br/>
## Cloning the repo
`git clone git@github.com:jhu-oose/2016-group-15.git` <br/>

## Running Tests
Connect the Leap Motion <br/>
`cd 2016-group-15` <br/>
`nosetests asla/binary/ml_tools/tests/test_predict_service.py` <br/>
`nosetests asla/binary/ml_tools/tests/test_training_service.py` <br/>
`nosetests asla/server/binary_server_backend/tests/test_ASLAController.py` <br/>
`nosetests asla/server/binary_server_backend/tests/test_model_generator.py` <br/>
`nosetests asla/server/flask_website/tests/test_binary_helper.py` <br/>
`nosetests asla/server/flask_website/tests/test_FlaskWebsiteBackend.py` <br/>
`nosetests asla/server/flask_website/tests/test_user_admin_service.py` <br/>
## Steps to Run UI 
* Connect the Leap Motion Device <br/>
* cd 2016-group-15/asla
* chmod u+x main.sh
* ./main.sh
