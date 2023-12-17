class Bicycle:
    def __init__(self, gear, speed):
        self.gear = gear
        self.speed = speed

    def show_features(self):
        print("The gear of bicycle is", self.gear, "and speed is", self.speed)


class MountainBike(Bicycle):
    def __init__(self, gear, speed, seatheight):
        super().__init__(gear, speed)
        self.seatheight = seatheight

    def show_properties(self):
        print("The gear of bicycle is", self.gear, ",speed is", self.speed, " and seatheight is", self.seatheight)


a = Bicycle("First", 60)
a.show_features()

b = MountainBike("Fifth", 100, 40)
b.show_properties()