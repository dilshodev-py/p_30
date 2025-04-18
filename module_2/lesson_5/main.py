from abc import ABC , abstractmethod

class Vehicle(ABC): # interface

    @abstractmethod # sub class ichida berilgan method override
    # qilinishini talab qilinadi
    def move(self):
        pass

    @abstractmethod
    def stop(self):
        pass

# Vehicle()
class Car(Vehicle):

    def move(self):
        pass

    def stop(self):
        pass


c = Car()
print(c)


