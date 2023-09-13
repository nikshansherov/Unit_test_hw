from vehicle import *


class Car(Vehicle):
    company = 'Москвич'
    model = 'Москвич-3'
    year_release = 2023
    num_wheels = 4
    speed = 0

    def test_drive(self):
        self.speed = 60
        return self.speed

    def park(self):
        self.speed = 0
        return self.speed

