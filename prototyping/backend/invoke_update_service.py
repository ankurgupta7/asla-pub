"""
Class to invoke update_service
"""
from update_service import UpdateService
import numpy as np
import time
import io
import re


def main():
    us = UpdateService()
    all_gesture_data = []
    cal_param = 1
    # if the sensor was calibrated before, then use the data from calibration_data
    try:
        f = open('calibration_data.txt', 'r')
        calibrated = True
        line = f.read()
        cal_param = float(re.findall('\d+.\d+', line)[0])
    except IOError:
        print "FileNotFoundException: calibration_data.txt not found\n" \
              "Need to calibrate the sensor...Preparing for calibration"
        calibrated = False

    # start calibration and store calibration parameters
    if not calibrated:
        cal_param = us.calibrate()
        with io.FileIO("calibration_data.txt", "w") as cal_file:
            cal_file.write("Length of middle finger: " + str(cal_param))

    print "Add Gesture ?(y/n)"
    user_input = raw_input()
    if user_input == 'y':
        add_gesture = True
    elif user_input == 'n':
        add_gesture = False
    while add_gesture:
        label = us.get_label_from_user()
        if label:
            single_gesture_data_field = us.get_single_gesture_data(label, cal_param)
            all_gesture_data.extend(single_gesture_data_field)
            print "Single Gesture Data: "
            print single_gesture_data_field
            print "Add Another Gesture ?(y/n) "
            user_input = raw_input()
            if user_input == 'y':
                add_gesture = True
            elif user_input == 'n':
                to_save = np.array(all_gesture_data)
                "Data Being Stored: "
                print to_save
                # todo store in a sep folder
                # save data to file with timestamp
                # label, followed by features
                filename = ''.join(['data-', time.strftime("%Y%m%d-%H%M%S"), '.csv'])
                np.savetxt(filename, to_save, delimiter=',', fmt='%1.3f')
                add_gesture = False


if __name__ == "__main__":
    main()
