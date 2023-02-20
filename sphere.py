# Sphere class

from math import pi

class Sphere:
    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius
    
    def surface_area(self):
        return 4 * pi * self.radius**2

    def volume(self):
        return (4/3) * pi * self.radius**3

def main():
    test = Sphere(5)
    print(test)
    print(test.get_radius())
    print(test.surface_area())
    print(test.volume())

if __name__ == '__main__': main() 