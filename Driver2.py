DEFAULT_FLOORS = 2
DEFAULT_SLOTS = [20, 20]

MENU_OPTIONS = {
    "1": park,
    "2": retrieve_spot,
    "3": unpark,
    "4": exit_program
}

def validate_reg_num(reg_num):
    # Add your validation logic here
    return True

def park(parking_lot):
    # book a spot
    if not parking_lot.is_slot_available():
        print ("No space available. Sorry!")
    else:
        reg_num = input("Enter vehicle registration number: ")
        if reg_num:
            if parking_lot.is_vehicle_reg_num_duplicate(reg_num):
                print("This vehicle registration number is already taken. Sorry!")
            else:
                spot_registered = parking_lot.park(reg_num)
                print("Vehicle Parked at floor {} and spot no {}.".format(spot_registered.get_floor_number(), spot_registered.get_spot_position()))
        else:
            print("Nothing entered.")

def retrieve_spot(parking_lot):
    # retrieve a spot
    reg_num = input("Enter vehicle registration number: ")
    if reg_num:
        spot_info = parking_lot.get_slot(reg_num)
        if spot_info:
            print("{{'level': {}, 'spot': {}}}".format(spot_info.get_floor_number(), spot_info.get_spot_position()))
        else:
            print("Sir! No such vehilce parked.")
    else:
        print("Nothing entered.")

def unpark(parking_lot):
    # clear a spot
    reg_num = input("Enter vehicle registration number: ")
    if reg_num:
        if parking_lot.unpark(reg_num) is not None:
            print("vehile unparked successfully!")
        else:
            print("Sir! No such vehicle parked.")
    else:
        print("Nothing entered.")

def exit_program():
    # exit
    print("Thank you for using the parking system!")


def main():
    print("Welcome to the parking system!")
    no_of_floor = int(input("How many floors are there? By default 2 is taken: ") or DEFAULT_FLOORS)
    slots_for_each_floor = list(map(int, input("\nEnter the number of slots for each floor: ").strip().split()))[:no_of_floor] or DEFAULT_SLOTS
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
            if action:
                action(parking_lot)
            else:
                print("Invalid choice. Please try again.")
        except Exception as e:
            print("An error occurred:", str(e))

def book_spot(parking_lot):
    # Existing implementation

if __name__ == "__main__":
    main()
