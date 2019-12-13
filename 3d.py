from manimlib.imports import *

class ThreeDTest(SpecialThreeDScene):
    def construct(self):
        cubes = VGroup()
        for i in range(8):
            for j in range(10):
                l = 0.3
                c = Cube(side_length=l, stroke_width=1)
                pos = i * l * RIGHT + j * l * UP
                pos += LEFT + DOWN
                c.move_to(pos)
                if j > 2 and j < 6:
                    c.set_fill(RED)
                cubes.add(c)
        self.set_camera_orientation(phi=60*DEGREES, theta=30*DEGREES)
        self.play(ShowCreation(cubes))
        self.wait()
