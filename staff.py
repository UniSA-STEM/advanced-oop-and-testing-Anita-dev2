"""
File: filename.py
Description: A brief description of this Python module.
Author: Billy Bizilis
ID: 110100110
Username: bizvy001
This is my own work as defined by the University's Academic Integrity Policy.
"""
from abc import ABC, abstractmethod

class Staff(ABC):
    __next_id = 1

    def __init__(self, name):
        self.__name = name
        self.__id = Staff.__next_id
        self.__clocked_in = False
        Staff.__next_id = Staff.__next_id + 1


    def get_staff_name(self):
        return self.__name

    staff_name = property(get_staff_name)

    def get_staff_id(self):
        return self.__id

    staff_id = property(get_staff_id)

    def get_attendance(self):
        return self.__clocked_in

    working = property(get_attendance)

    def clock_in(self):
        if not self.working:
            self.__clocked_in = True
            print(f"{self.staff_name} has clocked in for work.")
        else:
            print(f"{self.staff_name} is already at work!")

    def clock_out(self):
        if self.working:
            self.__clocked_in = False
            print(f"{self.staff_name} has successfully clocked out for today.")
        else:
            print(f"{self.staff_name} has already finished for today.")

    @abstractmethod
    def __str__(self):
        pass


class Zookeeper(Staff):
    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return f"Name: {self.staff_name}\nStaff ID: {self.staff_id}\nRole: Zookeeper\nAllocated Tasks: Feeding + Cleaning\n"


class Veterinarian(Staff):
    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return f"Name: {self.staff_name}\nStaff ID: {self.staff_id}\nRole: Veterinarian\nAllocated Tasks: Health Checks\n"



staff1 = Zookeeper("Bob")
staff1.clock_in()
staff1.get_staff_id()
print(staff1)
zoo1 = Zookeeper("Sally")
print(zoo1)
zoo1.clock_in()
zoo1.clock_in()
zoo1.clock_out()
vet1 = Veterinarian("Rob")
vet1.clock_in()
print(vet1)