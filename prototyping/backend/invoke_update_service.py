"""
Class to invoke update_service
"""
from update_service import UpdateService


def main():
    update_service = UpdateService()
    add_gesture = False
    print "Add Gesture ?(y/n)"
    user_input = raw_input()
    if user_input == 'y':
        add_gesture = True
    elif user_input == 'n':
        add_gesture = False
    while add_gesture:
        print "Enter Label(Int 1 to 5): "
        label = raw_input()
        if label:
            update_service.capture_gesture(label)
            print 'Add Another Gesture ?(y/n) '
            user_input = raw_input()
            if user_input == 'y':
                add_gesture = True
            elif user_input == 'n':
                update_service.save_collected_data()
                add_gesture = False


if __name__ == "__main__":
    main()
