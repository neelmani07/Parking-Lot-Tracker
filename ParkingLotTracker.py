"""
This file contains the definition of class Parking Lot.
"""

from typing import Any
from collections import deque

from ParkingSlots import Slot


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

    def get_slot(self, vehicle_num):
        """
        Retrieves the parking spot information for a vehicle with the given registration number.

        Args:
            vehicle_num (Any): The registration number of the vehicle.

        Returns:
            Slot: The Slot object representing the parking spot where the vehicle is parked.
                  Returns None if the vehicle is not parked.

        """
        if vehicle_num in self.occupied_slots:
            return self.occupied_slots[vehicle_num]
        return None

    def unpark(self, vehicle_num):
        """
        Unparks a vehicle with the given registration number.

        Args:
            vehicle_num (Any): The registration number of the vehicle.

        Returns:
            Slot: The Slot object representing the parking spot that was cleared.
                  Returns None if the vehicle is not parked.

        """
        if vehicle_num not in self.occupied_slots:
            return None

        slot = self.occupied_slots.pop(vehicle_num)
        self.available_slots.append(slot)
        return slot