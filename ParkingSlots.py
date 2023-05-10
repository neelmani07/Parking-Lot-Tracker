"""This file contains the definition of class Slot. """


class Slot:
    """This class is used for enscaptulating the floor
    and position number together as a single unit."""

    def __init__(self, floors_number, spot_postion):
        """initializes the floor number and slot number."""
        self.floors_number = floors_number
        self.spot_postion = spot_postion

    def get_floor_number(self):
        """return floor number."""
        return self.floors_number

    def get_spot_position(self):
        """return spot position."""
        return self.spot_postion