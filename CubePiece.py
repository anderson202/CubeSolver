from enum import Enum
xCClockwise = [[1, 0, 0],
               [0, 0, -1],
               [0, 1, 0]]

xClockwise = [[1, 0, 0],
              [0, 0, 1],
              [0, -1, 0]]

yCClockwise = [[0, 0, 1],
               [0, 1, 0],
               [-1, 0, 0]]

yClockwise = [[0, 0, -1],
              [0, 1, 0],
              [1, 0, 0]]

zCClockwise = [[0, -1, 0],
               [1, 0, 0],
               [0, 0, 1]]

zClockwise = [[0, 1, 0],
              [-1, 0, 0],
              [0, 0, 1]]

class Axis(Enum):
    X = "x"
    Y = "y"
    Z = "z"

class CubePiece:

    def __init__(self, color_x, color_y, color_z, loc):
        self.color_x = color_x
        self.color_y = color_y
        self.color_z = color_z
        self.type = None
        self.location = loc
        self.sides = {}
        self.__findSides()


    def __multiply(self, v, rMatrix):
        newVector = []
        i = 0
        for row in rMatrix:
            newVector.append(row[0] * v[0] + row[1] * v[1] + row[2] * v[2])
        self.location = newVector

    def __findSides(self):
        sides = {}
        xSides = {-1: "L", 1: "R", 0: "M"}
        ySides = {-1: "F", 1: "B", 0: "S"}
        zSides = {-1: "D", 1: "U", 0: "E"}

        if (xSides.get(self.location[0]) != None):
            sides[xSides.get(self.location[0])] = 1
        if (ySides.get(self.location[1]) != None):
            sides[ySides.get(self.location[1])] = 1
        if (zSides.get(self.location[2]) != None):
            sides[zSides.get(self.location[2])] = 1
        self.sides = sides

    def rotate(self, matrix):
        rotateAxis = None
        if (matrix[0][0] == 1):
            rotateAxis = Axis.X
        elif (matrix[1][1] == 1):
            rotateAxis = Axis.Y
        elif (matrix[2][2] == 1):
            rotateAxis = Axis.Z
        else:
            raise Exception
        self.__multiply(self.location, matrix)
        self.__swapColor(rotateAxis)
        self.__findSides()

    def __swapColor(self, axis):
        if axis == Axis.X:
            color_x, color_y, color_z = self.color_x, self.color_z, self.color_y
        elif axis == Axis.Y:
            color_x, color_y, color_z = self.color_z, self.color_y, self.color_x
        else:
            color_x, color_y, color_z = self.color_y, self.color_x, self.color_z

        self.setColor(color_x, color_y, color_z)

    def setColor(self, color1, color2, color3):
        self.color_x = color1
        self.color_y = color2
        self.color_z = color3

    def __str__(self):
        return str(self.location) + "\nx: " + self.color_x + " y: " + self.color_y + " z: " + self.color_z + "\nSides: " + str(self.sides)


if __name__ == "__main__":
    a = CubePiece("Green", "Red", "White", [0,-1,0])
    a.rotate(xClockwise)
    print(a)