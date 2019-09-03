from vehicle import Vehicle
from gas import Gas

class Ram(Vehicle, Gas):
    
    def __init__(self):
        Vehicle.__init__(self, "Dodge", "Ram", 120, 4)
        Gas.__init__(self, 26)

    

    def drive(self):
        Gas.drive(self, 6)
