from vehicle import Vehicle
from electric import Electric

class Leaf(Vehicle, Electric):

    def __init__(self):
        Vehicle.__init__(self, "Nissan", "Leaf", 50, 4)
        Electric.__init__(self, 45)

    def drive(self):
        Electric.drive(self, 1)
        

