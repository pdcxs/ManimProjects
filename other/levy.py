from manimlib.imports import *

class Levy(VMobject):
    def __init__(self, start, end, it, **kwargs):
        self.start = start
        self.end = end
        self.it = it
        VMobject.__init__(self, **kwargs)

    def get_point(self, p1, p2):
        v = (p2 - p1) / 2
        [x, y] = v[0:2]
        rv = y * RIGHT + x * DOWN
        return p1 + v + rv

    def generate_levy_point(self, start, end, it):
        if it == 0:
            return [start, end]
        else:
            p = self.get_point(start, end)
            return self.generate_levy_point(start, p, it-1) +\
                self.generate_levy_point(p, end, it-1)

    def generate_points(self):
        self.set_points_as_corners(
            self.generate_levy_point(
            self.start,
            self.end,
            self.it
        ))


class LevyScene(Scene):
    CONFIG = {
        "camera_class": MovingCamera
    }
    def construct(self):
        text = TexMobject('N=0')
        text.to_corner(UL)
        self.play(Write(text))

        start = RIGHT * 3 + 2 * DOWN
        end = LEFT * 3 + 2 * DOWN

        levy = Levy(start, end, 0)
        self.play(ShowCreation(levy))
        self.wait()

        for i in range(1, 13):
            new_text = TexMobject(f'N={i}')
            new_text.to_corner(UL)
            new_levy = Levy(start, end, i)
                
            self.play(Transform(
                levy, new_levy
                ),
                Transform(
                text, new_text))
            self.wait()
        
        self.wait(20)
