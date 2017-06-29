import CubePiece
class Cube:
    def __init__(self, front, back, left, right, up, down):
        self.pieces = [
            CubePiece(left[0], back[2], up[0], [-1, 1, 1]),
            CubePiece(None, back[1], up[1], [0, 1, 1]),
            CubePiece(right[2], back[0], up[2], [1, 1, 1]),
            CubePiece(left[1], None, up[3], [-1, 0, 1]),
            CubePiece(None, None, up[4], [0, 0, 1]),
            CubePiece(right[1], None, up[5], [1, 0, 1]),
            CubePiece(left[2], front[0], up[6], [-1, -1, 1]),
            CubePiece(None, front[1], up[7], [0, -1, 1]),
            CubePiece(right[0], front[2], up[8], [-1, -1, 1]),

            CubePiece(left[3], back[5], None, [-1, 1, 0]),
            CubePiece(None, back[4], None, [0, 1, 0]),
            CubePiece(right[5], back[3], None, [1, 1, 0]),
            CubePiece(right[4], None, None, [-1, 0, 0]),
            CubePiece(None, None, None, [0,0,0]),
            CubePiece(left[4], None, None, [1, 0, 0]),
            CubePiece(left[5], front[3], None, [-1, -1, 0]),
            CubePiece(None, front[4], None, [0, -1, 0]),
            CubePiece(right[3], front[5], None, [1, -1, 0]),

            CubePiece(left[6], back[8], down[2], [-1, 1, 0]),
            CubePiece(None, back[7], down[1], [0, 1, 0]),
            CubePiece(right[8], back[6], down[0], [1, 1, 0]),
            CubePiece(left[7], None, down[5], [-1, 0, 0]),
            CubePiece(None, None, down[4], [0, 0, 0]),
            CubePiece(right[7], None, down[3], [1, 0, 0]),
            CubePiece(left[8], front[6], down[8], [-1, -1, 0]),
            CubePiece(None, front[7], down[7], [0, -1, 0]),
            CubePiece(right[6], front[8], down[6], [1, -1, 0]),
        ]


