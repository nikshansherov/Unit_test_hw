from vehicle import *


class Motorcycle(Vehicle):
    company = 'Урал'
    model = 'GEAR UP'
    year_release = 2018
    num_wheels = 2
    speed = 0

    def test_drive(self):
        self.speed = 75
        return self.speed

    def park(self):
        self.speed = 0
        return self.speed

