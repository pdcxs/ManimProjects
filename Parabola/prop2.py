from manimlib.imports import *
from ManimProjects.utils.Parabola import Parabola
from ManimProjects.utils.geometry import CText

class OpenScene(Scene):
    def construct(self):
        sub1 = CText('这将是一个')
        sub2 = CText('关于线段长度的性质')
        subs = VGroup(sub1, sub2)
        subs.arrange(DOWN)
        self.play(Write(sub1))
        self.play(Write(sub2))
        self.wait(2)
        self.play(FadeOut(subs))
    
