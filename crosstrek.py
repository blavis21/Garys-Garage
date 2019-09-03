from vehicle import Vehicle
from gas import Gas
from electric import Electric


class Crosstrek(Vehicle, Gas, Electric):
    def __init__(self):
        Vehicle.__init__(self, "Subaru", "Crosstrek", 60, 4)
        Gas.__init__(self, 40)
        Electric.__init__(self, 6)

    def refuel(self):
        Electric.refuel(self)
        Gas.refuel(self)

    def drive(self):
        Electric.drive(self, 2)
        Gas.drive(self, 0.5)