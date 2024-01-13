# classes to define new types to model real concepts
# new type called point
# capitalizing the letter is called pascal naming convention
# you don't use underscore to seperate but use capitilize


class Point:
    def move(self):
        print("move")

    def draw(self):
        print("draw")

point1 = Point()
point1.x = 10
point1.y = 20

print(point1.x)
point1.draw()

point2 = Point()
point2.x = 1
point2.y = 2

print(point2.x)