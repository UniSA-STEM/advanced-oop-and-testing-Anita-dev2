"""
File: staff.py
Description: This module includes the Staff class and its children classes
Author: Anita Maratheftis
ID: 110467133
Username: maray160
This is my own work as defined by the University's Academic Integrity Policy.
"""
from abc import ABC, abstractmethod

class Staff(ABC):
    """
    This is the abstract class for staff
    """
    # Set staff id to 1
    __next_id = 1

    def __init__(self, name):
        self.__name = name
        self.__id = Staff.__next_id
        self.__clocked_in = False
        Staff.__next_id = Staff.__next_id + 1

    def get_staff_name(self):
        """
        This is a getter for staff name
        :return: self.__name: str
        """
        return self.__name

    staff_name = property(get_staff_name)


    def get_staff_id(self):
        """
        This is a getter for staff id
        :return: self.__id: int
        """
        return self.__id

    # Set property for staff id
    staff_id = property(get_staff_id)

    def get_attendance(self):
        """
        This is a getter for attendance
        :return: self.__clocked_in: boolean
        """
        return self.__clocked_in

    # Set property for attendance
    working = property(get_attendance)

    def clock_in(self):
        """
        This function allows a staff member to clock in for work, or validates that they are clocked in if they try twice
        :return:
        """
        # If self.__clocked_in returns False, reset attribute to True
        if not self.working:
            self.__clocked_in = True
            # Display result to user
            print(f"{self.staff_name} has clocked in for work.\n")
        else:
            # Display to user that the staff member is already at work (self.__clocked_in returned True)
            print(f"{self.staff_name} is already at work!\n")

    def clock_out(self):
        """
        This function allows a staff member to clock out for work, or validates that they are clocked out if they try twice
        :return:
        """
        # if self.__clocked_in is True, reset attribute to False
        if self.working:
            self.__clocked_in = False
            # Display result to user
            print(f"{self.staff_name} has successfully clocked out for today.\n")
        else:
            # Display to user that the staff member has already clocked out (self.__clocked_in returned False)
            print(f"{self.staff_name} has already finished for today.\n")

    # Abstract string method
    @abstractmethod
    def __str__(self):
        pass

class Zookeeper(Staff):
    """
    This is the child class of staff, zookeeper
    """
    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        """
        This is the string method for zookeeper
        :return: str
        """
        return f"Name: {self.staff_name}\nStaff ID: {self.staff_id}\nRole: Zookeeper\nAllocated Tasks: Feeding + Cleaning\n"


class Veterinarian(Staff):
    """
    This is the child class of staff, veterinarian
    """
    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        """
        This is the string method for veterinarian
        :return:
        """
        return f"Name: {self.staff_name}\nStaff ID: {self.staff_id}\nRole: Veterinarian\nAllocated Tasks: Health Checks\n"
