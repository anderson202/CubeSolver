from CubePiece import CubePiece

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

class Cube:
    def __init__(self, front, back, left, right, up, down):
        self.corners = [
            CubePiece(left[0], back[2], up[0], [-1, 1, 1]),
            CubePiece(right[2], back[0], up[2], [1, 1, 1]),
            CubePiece(left[2], front[0], up[6], [-1, -1, 1]),
            CubePiece(right[0], front[2], up[8], [-1, -1, 1]),
            CubePiece(left[6], back[8], down[2], [-1, 1, 0]),
            CubePiece(right[8], back[6], down[0], [1, 1, 0]),
            CubePiece(left[8], front[6], down[8], [-1, -1, 0]),
            CubePiece(right[6], front[8], down[6], [1, -1, 0]),
        ]

        self.edges = [
            CubePiece(None, front[7], down[7], [0, -1, -1]),
            CubePiece(left[7], None, down[5], [-1, 0, -1]),
            CubePiece(right[7], None, down[3], [1, 0, -1]),
            CubePiece(None, back[7], down[1], [0, 1, -1]),
            CubePiece(right[3], front[5], None, [1, -1, 0]),
            CubePiece(left[5], front[3], None, [-1, -1, 0]),
            CubePiece(right[5], back[3], None, [1, 1, 0]),
            CubePiece(left[3], back[5], None, [-1, 1, 0]),
            CubePiece(None, front[1], up[7], [0, -1, 1]),
            CubePiece(right[1], None, up[5], [1, 0, 1]),
            CubePiece(left[1], None, up[3], [-1, 0, 1]),
            CubePiece(None, back[1], up[1], [0, 1, 1]),
        ]

        self.centers = [
            CubePiece(None, None, up[4], [0, 0, 1]),
            CubePiece(None, back[4], None, [0, 1, 0]),
            CubePiece(right[4], None, None, [-1, 0, 0]),
            CubePiece(left[4], None, None, [1, 0, 0]),
            CubePiece(None, None, down[4], [0, 0, 0]),
            CubePiece(None, front[4], None, [0, -1, 0]),
        ]

        self.center = CubePiece(None, None, None, [0,0,0])
        self.pieces = self.corners + self.edges + self.centers

    def __str__(self):
        cube = ""
        i = 0
        for piece in self.pieces:
            cube += "cubie " + str(i) + " " + str(piece) + "\n"
            i += 1
        return cube

    def __applyRotation(self, matrix, side):
        for piece in self.pieces:
            if piece.sides.get(side) != None:
                piece.rotate(matrix)

    def getEdgeByColor(self, color1, color2):
        for edge in self.edges:
            if color1 in edge.colors and color2 in edge.colors:
                return edge

    def getCornerByColor(self, color1, color2, color3):
        for corner in self.corners:
            if color1 in corner.colors and color2 in corner.colors and color3 in corner.colors:
                return corner

    def L(self):
        self.__applyRotation(xCClockwise, "L")

    def LPrime(self):
        self.__applyRotation(xClockwise, "L")

    def R(self):
        self.__applyRotation(xClockwise, "R")

    def RPrime(self):
        self.__applyRotation(xCClockwise, "R")

    def U(self):
        self.__applyRotation(zClockwise, "U")

    def UPrime(self):
        self.__applyRotation(zCClockwise, "U")

    def D(self):
        self.__applyRotation(xCClockwise, "D")

    def DPrime(self):
        self.__applyRotation(xClockwise, "D")

    def F(self):
        self.__applyRotation(yCClockwise, "F")

    def FPrime(self):
        self.__applyRotation(yClockwise, "F")

    def B(self):
        self.__applyRotation(yClockwise, "B")

    def BPrime(self):
        self.__applyRotation(yCClockwise, "B")

