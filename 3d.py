from manimlib.imports import *

class ThreeDTest(SpecialThreeDScene):
    def construct(self):
        cube = Cube(fill_color=RED, side_length=1)
        self.set_camera_orientation(phi=70*DEGREES, theta=30*DEGREES)
        cube.add_updater(lambda m, dt: m.rotate(0.1 * dt))
        self.add(cube)
        self.wait()