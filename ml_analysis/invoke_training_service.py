"""
Class to invoke update_service
"""
from training_service import TrainingService


def main():
    update_service = TrainingService()
    count = 0
    add_gesture = False
    print "Add Gesture ?(y/n)"
    user_input = raw_input()
    if user_input == 'y':
        count += 1
        print "Gesture number" , count
        add_gesture = True
    elif user_input == 'n':
        add_gesture = False
    while add_gesture:
        print "Enter Label(Int A to Z): "
        label = raw_input()
        if label:
            update_service.capture_gesture(label)
            print 'Add Another Gesture ?(y/n) '
            user_input = raw_input()
            if user_input == 'y':
                add_gesture = True
                count += 1
                print "Gesture number", count
            elif user_input == 'n':
                update_service.save_collected_data()
                add_gesture = False


if __name__ == "__main__":
    main()
