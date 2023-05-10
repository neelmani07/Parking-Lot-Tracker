"""
This file contains the definition of class Parking Lot.
"""

from typing import Any
from collections import deque

from parking_slots import Slot


class ParkingLot:
    """This class defines the entire parking Lot itself."""

    def __init__(self, num_of_floors, spots_for_each_floor_list):
        """
        Initializes the ParkingLot with the specified number of floors and spots for each floor.

        Args:
            num_of_floors (int): The total number of floors in the parking lot.
            spots_for_each_floor_list (list): A list containing the number of spots for each floor.
        """
        self.number_of_floors = num_of_floors
        self.spots_for_each_floor_list = spots_for_each_floor_list
        self.available_slots =  deque()
        self.occupied_slots = {}
        self.action = None
        slot_count = 1
        for floor, spots in enumerate(self.spots_for_each_floor_list, start=1):
            for spot in range(1, spots + 1):
                slot = Slot(chr(floor + 64), slot_count)
                self.available_slots.append(slot)
                slot_count+=1

    def park(self, vehicle_num):
        """
        Parks a vehicle with the given registration number.

        Args:
            vehicle_num (Any): The registration number of the vehicle.

        Returns:
            Slot: The Slot object representing the parking spot where the vehicle is parked.
        The checks for availablity of slots is already done  in driver code.
        """
        slot = self.available_slots.popleft()
        self.occupied_slots[vehicle_num] = slot
        return slot

    def is_vehicle_present(self, vehicle_num):
        """
        Check if a vehicle is present in lot.

        Args:
            vehicle_num (Any): The registration number of the vehicle.

        Returns:
            True if vehicle is present in lot,
            else False.
        """
        if vehicle_num not in self.occupied_slots:
            return False
        else:
            return True

    def unpark(self, vehicle_num):
        """
        Unparks a vehicle with the given registration number.

        Args:
            vehicle_num (Any): The registration number of the vehicle.

        Returns:
            Slot: The Slot object representing the parking spot that was cleared.
                  Returns None if the vehicle is not parked.

        """
        slot = self.occupied_slots.pop(vehicle_num)
        self.available_slots.append(slot)
        return slot

    def is_slot_available(self):
        """
        Check if a slot is available.

        Args:
           None

        Returns:
            True if a slot is available,
            else False.
        """
        return True if self.available_slots else False

    def is_vehicle_reg_num_duplicate(self, vehicle_num):
        """
        Check if given vehicle number is already belong to somebody else.

        Args:
           vehicle_num (Any): The registration number of the vehicle.

        Returns:
            True if vehicle number is duplicate,
            else False.
        """
        if self.occupied_slots.get(vehicle_num):
            return True
        else:
            return False

    def get_level_and_spot(self, vehicle_num):
        """
        Provides floor level and spot position for a vehicle.

        Args:
           vehicle_num (Any): The registration number of the vehicle.

        Returns:
            floor level and spot number.
        """
        slot_num = self.occupied_slots[vehicle_num]
        return slot_num.get_floor_number(), slot_num.get_spot_position()

    def set_action(self, action):
        """
        Set the action required in the slot.

        Args:
           None

        Returns:
            set the action's value.
        """
        self.action = action

    def get_action(self):
        """
        Returns the action required in the slot.

        Args:
           None

        Returns:
            Returns the action's value.
        """
        return self.action