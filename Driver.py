"""
This file contains the driver code for running the parking lot tracker.
"""

from ParkingLotTracker import ParkingLot


def display_menu():
    """
    Displays the main menu of the parking system.
    """
    print("Welcome to the parking system!")
    no_of_floor = input("How many floors are there? if nothing is enetered 2 is assumed") or 2
    slots_for_each_floor = input("provide a list containg spot numbers for each floor. if nothing is assumed, list is assumed to be [20,20]") or [20,20]
    parking_lot_tracker = ParkingLot(no_of_floor, slots_for_each_floor)

    while True:
        print("Please choose an option:")
        print("1. Book a parking spot")
        print("2. Retrieve parking spot number")
        print("3. Clear a parking spot")
        print("4. Exit")
        choice = input()
        if choice == "1":
            # book a spot
            if not parking_lot_tracker.available_slots:
                print ("No space available. Sorry!")
            else:
                reg_num = input("Enter vehicle registration number: ")
                if parking_lot_tracker.occupied_slots.get(reg_num) is None:
                    spot_registered = parking_lot_tracker.park(reg_num)
                    spot_floor = chr(spot_registered.get_floor_number()+64)
                    spot_num = spot_registered.get_spot_position()
                    print("Vehicle Parked at floor {} and spot no {}.".format(spot_floor,spot_num))
                else:
                    print("This vehicle registration number is already taken. Sorry!")

        elif choice == "2":
            # retrieve a spot
            reg_num = input("Enter vehicle registration number: ")
            spot_info = parking_lot_tracker.get_slot(reg_num)

            if spot_info:
                level = chr(spot_info.get_floor_number()+ 64)
                spot_pos = spot_info.get_spot_position()
                print("{{'level': {}, 'spot': {}}}".format(level, spot_pos))
            else:
                print("Sir! No such vehice parked.")

        elif choice == "3":
            # clear a spot
            reg_num = input("Enter vehicle registration number: ")
            if parking_lot_tracker.unpark(reg_num) is not None:
                print("vehile unparked successfully!")
            else:
                print("Sir! No such vehice parked.")

        elif choice == "4":
            # exit
            print("Thank you for using the parking system!")
            break
        else:
            print("Invalid choice. Please try again.")

def main():
    display_menu()


if __name__ == "__main__":
    main()