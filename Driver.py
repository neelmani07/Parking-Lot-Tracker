"""
This file contains the driver code for running the parking lot tracker.
"""

from ParkingLotTracker import ParkingLot


def display_menu():
    """
    Displays the main menu of the parking system.
    """
    print("Welcome to the parking system!")

    no_of_floor = int(input("How many floors are there? By default 2 is taken.") or 2)
    slots_for_each_floor = list(map(int,input("\nProvide a list containg spot numbers for each floor.\n enter the numbers with space in between. \n By Default 20 20 is taken ").strip().split()))[:no_of_floor] or [20,20]
    parking_lot_tracker = ParkingLot(no_of_floor, slots_for_each_floor)

    print("No of floors: {} \ntotal slots in each floor: {}".format(no_of_floor, slots_for_each_floor))

    while True:
        print("\nPlease choose an option: \n1. Book a parking spot. \n2. Retrieve parking spot number. \n3. Clear a parking spot. \n4. Exit.")
        choice = input()

        if choice == "1":
            # book a spot
            if not parking_lot_tracker.is_slot_available():
                print ("No space available. Sorry!")
            else:
                reg_num = input("Enter vehicle registration number: ")
                if reg_num:
                    if parking_lot_tracker.is_vehicle_reg_num_duplicate(reg_num):
                        print("This vehicle registration number is already taken. Sorry!")
                    else:
                        spot_registered = parking_lot_tracker.park(reg_num)
                        print("Vehicle Parked at floor {} and spot no {}.".format(spot_registered.get_floor_number(), spot_registered.get_spot_position()))
                else:
                    print("Nothing enetered.")

        elif choice == "2":
            # retrieve a spot
            reg_num = input("Enter vehicle registration number: ")
            if reg_num:
                spot_info = parking_lot_tracker.get_slot(reg_num)
                if spot_info:
                    print("{{'level': {}, 'spot': {}}}".format(spot_info.get_floor_number(), spot_info.get_spot_position()))
                else:
                    print("Sir! No such vehilce parked.")
            else:
                print("Nothing entered.")

        elif choice == "3":
            # clear a spot
            reg_num = input("Enter vehicle registration number: ")
            if reg_num:
                if parking_lot_tracker.unpark(reg_num) is not None:
                    print("vehile unparked successfully!")
                else:
                    print("Sir! No such vehicle parked.")
            else:
                print("Nothing entered.")

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