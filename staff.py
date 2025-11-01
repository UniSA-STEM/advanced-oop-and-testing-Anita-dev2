"""
File: filename.py
Description: A brief description of this Python module.
Author: Billy Bizilis
ID: 110100110
Username: bizvy001
This is my own work as defined by the University's Academic Integrity Policy.
"""


class Staff:
    def __init__(self, name, id):
        self.__name = name
        self.__id = id
        self.__clocked_in = False

    def get_staff_name(self):
        return self.__name

    staff_name = property(get_staff_name)

    def get_staff_id(self):
        return self.__id

    def set_staff_id(self, id):
        if isinstance(id, int):
            self.__id = id

    staff_id = property(get_staff_id, set_staff_id)

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



    def __str__(self):
        return f"Name: {self.staff_name}\nStaff ID: {self.staff_id}"


class Zookeeper(Staff):
    def __init__(self, name, id):
        super().__init__(name, id)


    def __str__(self):
        return super().__str__() + "\nRole: Zookeeper"


class Veterinarian(Staff):
    def __init__(self, name, id):
        super().__init__(name, id)

    def __str__(self):
        return super().__str__() + "\nRole: Veterinarian"



staff1 = Staff("Bob", 7)
staff1.clock_in()
staff1.get_staff_id()
print(staff1)
zoo1 = Zookeeper("Sally", 2)
print(zoo1)
zoo1.clock_in()
zoo1.clock_in()
zoo1.clock_out()
vet1 = Veterinarian("Rob", 3)
vet1.clock_in()
print(vet1)