from cmath import sqrt


class Point:
    def __init__(self, x=0, y=0):
        self.x=x
        self.y=y
        # self.p1=p1
        # self.p2=p2

    def coordinates(self):
        print(f'Coordinates: (x,y) = ({self.x},{self.y})')

    def __str__(self):
        print('Using __str__')
        return f'Coordinates: (x,y) = ({self.x},{self.y})'

    def distance(self, obj_b):
        res = sqrt((self.x-obj_b.x)^2+(self.y-obj_b.y)^2)
        print(res)

p1=Point(2,4)
p2=Point(3,7)
print(Point.coordinates(p1))
print(Point.coordinates(p2))

print(p1)
print(p2)

print('')
print('Distance: ')
dis=Point.distance(p1, p2)
print(dis)