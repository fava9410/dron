class Dron(object):
    maxPos = 0 #cuadras a la redonda + 1
    maxDeliveries = 0
    posX = 0
    posY = 0
    orientation = 'N'
    degree = 90
    error = 0

    def __init__(self, maxPos, maxDeliveries):
        self.maxPos = maxPos
        self.maxDeliveries = maxDeliveries

    def identify_command(self, command):
        if command == 'A':
            self.forward()
        elif command == 'I':
            self.rotate(90)
        elif command == 'D':
            self.rotate(-90)

        return self.error

    def rotate(self, degree):
        self.degree = (self.degree + degree) % 360
        if self.degree == 0:
            self.orientation = 'E'
        elif self.degree == 90:
            self.orientation = 'N'
        elif self.degree == 180:
            self.orientation = 'W'
        elif self.degree == 270:
            self.orientation = 'S'

    def forward(self):
        if self.degree == 0:
            self.posX = self.posX + 1
        elif self.degree == 90:
            self.posY = self.posY + 1
        elif self.degree == 180:
            self.posX = self.posX - 1
        elif self.degree == 270:
            self.posY = self.posY - 1

        if self.posX in [self.maxPos, -self.maxPos] or self.posY in [self.maxPos, -self.maxPos]:
            self.error = 1
