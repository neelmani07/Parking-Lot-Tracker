"""
This file contains the driver code for running the parking lot tracker.
"""

from parking_lot_tracker import ParkingLot


DEFAULT_FLOORS = 2
DEFAULT_SLOTS = [20, 20]

def space_validation(parking_lot):
    """
    Checks for availability of slots.
    """
    return parking_lot.is_slot_available()


def validations(parking_lot, reg_num):
    """
    Takes input and Performs some in-common validation.
    """
    if not reg_num:
        return False
    elif parking_lot.get_action() == 1 and parking_lot.is_vehicle_reg_num_duplicate(reg_num):
        return False
    elif parking_lot.get_action() == 2 and not parking_lot.is_vehicle_present(reg_num):
        return False
    elif parking_lot.get_action() == 3 and not parking_lot.is_vehicle_present(reg_num):
        return False
    else:
        return True

def park(parking_lot):
    """
    Book a spot.
    """
    if not space_validation(parking_lot):
        print ("No space available. Sorry!")
    else:
        reg_num = input("Enter vehicle registration number: ")
        if validations(parking_lot, reg_num):
            parking_lot.park(reg_num)
            print("Vehicle Parked at successfully!")
        else:
            print("Invalid Entry!. \nVehicle number already taken or null entry")

def retrieve_spot(parking_lot):
    """
    Retrieve a spot.
    """
    reg_num = input("Enter vehicle registration number: ")
    if validations(parking_lot, reg_num):
        level, spot = parking_lot.get_level_and_spot(reg_num)
        print("{{'level': {}, 'spot': {}}}".format(level, spot))
    else:
        print("Invalid Entry! \nNo such vehicle or null entry.")

def unpark(parking_lot):
    """
    clear a spot.
    """
    reg_num = input("Enter vehicle registration number: ")
    if validations(parking_lot, reg_num):
        parking_lot.unpark(reg_num)
        print("vehile unparked successfully!")
    else:
        print("Invalid Entry. \nNo such vehicle or null entry.")

def exit_program(*args):
    """
    exit from the lot.
    """
    print("Thank you for using the parking system!")
    exit()


MENU_OPTIONS = {
    "1": park,
    "2": retrieve_spot,
    "3": unpark,
    "4": exit_program
}


def main():
    print("Welcome to the parking system!")
    no_of_floor = int(input("How many floors are there? By default 2 is taken: ") or DEFAULT_FLOORS)
    slots_for_each_floor = list(map(int, input("\nEnter the number of slots for each floor:"
                                               " \nBy default 20,20 is taken. "
                                               "\nenter the numbers with space in between: ").strip().split()))[:no_of_floor] or DEFAULT_SLOTS
    parking_lot = ParkingLot(no_of_floor, slots_for_each_floor)

    print("No of floors: {}\nTotal slots in each floor: {}".format(no_of_floor, slots_for_each_floor))

    while True:
        print("\nPlease choose an option:")
        print("1. Book a parking spot")
        print("2. Retrieve parking spot number")
        print("3. Clear a parking spot")
        print("4. Exit")
        choice = input()

        try:
            action = MENU_OPTIONS.get(choice)
            parking_lot.set_action(int(choice))
            if action:
                action(parking_lot)
            else:
                print("Invalid choice. Please try again.")
        except Exception as e:
            print("Invalid entry",e)


if __name__ == "__main__":
    main()
