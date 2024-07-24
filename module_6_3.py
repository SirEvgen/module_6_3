class Horse:
    sound = 'Frrr'

    def __init__(self):
        super().__init__()
        self.x_distance = 0

    def run(self, dx):
        self.dx = dx
        self.x_distance += self.dx
        return self.dx


class Eagle:
    sound = 'I train, eat, sleep and repeat'

    def __init__(self):
        super().__init__()
        self.y_distance = 0

    def fly(self, dy):
        self.dy = dy
        self.y_distance += self.dy
        return self.dy


class Pegasus(Horse, Eagle):
    def __init__(self):
        Horse.__init__(self)
        Eagle.__init__(self)
        self.sound = Eagle.sound

    def move(self, dx, dy):
        self.run(dx)
        self.fly(dy)

    def get_pos(self):
        return self.x_distance, self.y_distance

    def voice(self):
        return print(self.sound)


p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())
p1.voice()
