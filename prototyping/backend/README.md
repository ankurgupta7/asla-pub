## To capture expert data:
1. Run invoke_update_service.py to start the process
2. Enter 'y' to add gesture
3. Enter label (currently only integers between 1 to 5)
4. When 'Bring hand in View' is seen, bring your hand in view of the Leap Motion Controller(LMC)
5. Data starts recording automatically after a pre-set time
6. If hand is not visible for the preset record duration data is scrapped
7. If hand is visible for the preset record duration, data is captured.
8. Currently number of repetitions for each gesture are set to 5(this can be changed in the code)
9. Once the data is recorded, it is displayed and user is asked whether he wants to add another gesture
10. If yes, go to 3, else data is saved in a .csv file(with timestamp)