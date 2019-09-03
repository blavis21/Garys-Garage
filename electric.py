class Electric:
    def __init__(self, capacity):
        self.battery_capacity = capacity
        self.battery_level = 0

    def drive(self, lowerby):
        self.battery_level -= lowerby
        print(f'Your vehicle has {self.battery_level} kwh left, you road hog')

    def refuel(self):
        self.battery_level = self.battery_capacity
        print('You recharged your battery')