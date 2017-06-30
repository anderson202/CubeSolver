from enum import Enum

class Axis(Enum):
    X = "x"
    Y = "y"
    Z = "z"

class CubePiece:

    def __init__(self, color_x, color_y, color_z, loc):
        self.colors = [color_x, color_y, color_z]
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

    def dot(self, otherVector):
        if len(otherVector) > 3: raise Exception
        return self.location[0] * otherVector[0] \
               + self.location[1] * otherVector[1] \
               + self.location[2] * otherVector[2]

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
            color_x, color_y, color_z = self.colors[0], self.colors[2], self.colors[1]
        elif axis == Axis.Y:
            color_x, color_y, color_z = self.colors[2], self.colors[1], self.colors[0]
        else:
            color_x, color_y, color_z = self.colors[1], self.colors[0], self.colors[2]

        self.setColor(color_x, color_y, color_z)

    def setColor(self, color1, color2, color3):
        self.colors = [color1, color2, color3]

    def __str__(self):
        return str(self.location) + "\nx: " + str(self.colors[0]) + " y: " + str(self.colors[1]) + " z: " + str(self.colors[2]) + "\nSides: " + str(self.sides)

