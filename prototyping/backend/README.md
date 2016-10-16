## To capture expert data:
1. Run invoke_update_service.py to start the process
2. If the sensor is not calibrated, then process of calibration is started
3. When 'Bring hand in View and extend all the fingers' is seen, place the hand in view of LMC with all extended fingers
4. If the hand is open calibration starts
5. Number of repetitions for calibration is pre-set to 3
6. After the calibration finishes, the calibration parameter is stored locally in file 'calibration.txt', so that there is no need
   to calibrate the sensor again
7. After calibration program switches to the mode of collecting data
8. Enter 'y' to add gesture
9. Enter label (currently only integers between 1 to 5)
10. When 'Bring hand in View' is seen, bring your hand in view of the Leap Motion Controller(LMC)
11. Data starts recording automatically after a pre-set time
12. If hand is not visible for the preset record duration data is scrapped
13. If hand is visible for the preset record duration, data is captured.
14. Currently number of repetitions for each gesture are set to 5(this can be changed in the code)
15. Once the data is recorded, it is displayed and user is asked whether he wants to add another gesture
16. If yes, go to 3, else data is saved in a .csv file(with timestamp)