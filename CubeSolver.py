import Cube
from Cube import Cube
class CubeSolver:

    def __init__(self, cube):
        self.cube = cube
        self.moves = []

    def solve_cross(self):
        first_edge = self.cube.getEdgeByColor("green", "orange")
        print(first_edge)




if __name__ == "__main__":
    front = ["orange"] *9
    back = ["red"] * 9
    up = ["blue"] * 9
    down = ["green"] * 9
    left = ["yellow"] * 9
    right = ["white"] * 9
    cube = Cube(front, back, left, right, up, down)
    solver = CubeSolver(cube)

    solver.solve_cross()