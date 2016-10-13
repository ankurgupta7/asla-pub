"""
Class to invoke update_service
"""
from update_service import UpdateService
import numpy as np
import time
import os
import inspect


def main():

    us = UpdateService()
    all_gesture_data = []
    print "Add Gesture ?(y/n) "
    user_input = raw_input()
    if user_input == 'y':
        add_gesture = True
    elif user_input == 'n':
        add_gesture = False
    while add_gesture:
        label = us.get_label_from_user()
        if label:
            single_gesture_data = us.get_single_gesture_data(label)
            all_gesture_data.extend(single_gesture_data)
            print "Single Gesture Data: "
            print single_gesture_data
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
