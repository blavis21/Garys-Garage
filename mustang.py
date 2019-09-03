from vehicle import Vehicle
from gas import Gas

class Mustang(Vehicle, Gas):
    
    def __init__(self):
        Vehicle.__init__(self, "Ford", "Mustang", 460, 4)
        Gas.__init__(self, 20)

    def drive(self):
        Gas.drive(self, 4)


