import abc

class Vehicle(abc.ABC):
    company = None
    model = None
    year_release = 0
    num_wheels = 0
    speed = 0

    def test_drive():
        pass

    def park():
        pass
