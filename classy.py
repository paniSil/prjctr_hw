class Vector:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def cross_product(self, other):
        return self.x * other.x + self.y * other.y

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y


v = Vector(1, 3)
u = Vector(5, 2)

print(v.cross_product(u))
print(v*u)


class Robot:
    def __init__(self, orientation: str, position_x: int, position_y: int):
        self.orientation = orientation
        self.position_x = position_x
        self.position_y = position_y

    def move(self, steps):
        if self.orientation == 'east':
            self.position_x += steps
        elif self.orientation == 'west':
            self.position_x -= steps
        elif self.orientation == 'north':
            self.position_y += steps
        elif self.orientation == 'south':
            self.position_y -= steps

    def turn(self, direction):
        if direction == 'left':
            if self.orientation == 'east':
                self.orientation = 'north'
            elif self.orientation == 'north':
                self.orientation = 'west'
            elif self.orientation == 'west':
                self.orientation = 'south'
            elif self.orientation == 'south':
                self.orientation = 'east'
        if direction == 'right':
            if self.orientation == 'east':
                self.orientation = 'south'
            elif self.orientation == 'north':
                self.orientation = 'east'
            elif self.orientation == 'west':
                self.orientation = 'north'
            elif self.orientation == 'south':
                self.orientation = 'west'        

    def display_position(self):
        return print(f'Current Robot\'s position: {self.position_x}, {self.position_y} with orientation to {self.orientation}')


bender = Robot('north', 0, 0)
bender.move(9)
bender.turn('left')
bender.move(1)
bender.turn('left')
bender.move(2)
bender.turn('left')
bender.move(13)
bender.turn('right')
bender.move(9)

bender.display_position()
