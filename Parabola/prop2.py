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
    
class Prop2(Parabola):
    CONFIG = {
        'focus': 3,
        'x_min': -5
    }
    def construct(self):
        self.adjust_x_range()
        graph = self.get_graph(color=DARK_BROWN)
        directrix = self.get_directrix()
        focus = Dot().move_to(self.get_focus())
        focus.set_fill(DARK_BROWN)
        focus.plot_depth = 1

        self.play(ShowCreation(graph),
            ShowCreation(directrix),
            ShowCreation(focus))

        h_line = Line()
        d_loc = directrix.get_center()[0] * RIGHT
        h_line.put_start_and_end_on(d_loc, ORIGIN)
        h_line.plot_depth = -1
        self.play(ShowCreation(h_line))

        a = Dot()
        a.set_fill(LIGHT_BROWN)
        a.plot_depth = 1
        a.move_to(self.coords_to_point(0, 0))

        t = Dot()
        t.set_fill(LIGHT_BROWN)
        t.plot_depth = 1
        t.move_to(d_loc)
        
        y_value = ValueTracker(9)
        p = Dot()
        p.set_fill(DARK_BLUE)
        p.plot_depth = 1

        p.add_updater(lambda m:\
            m.move_to(self.value_to_point(
                y_value.get_value())))
        
        m = Dot()
        m.set_fill(DARK_BLUE)
        m.plot_depth = 1
        m.add_updater(lambda t:\
            t.move_to(d_loc + p.get_center()[1] * UP))
        
        n = Dot()
        n.set_fill(DARK_BLUE)
        n.plot_depth = 1
        n.add_updater(lambda m:\
            m.move_to(p.get_center()[0] * RIGHT))
        
        self.play(*[ShowCreation(e) for e in\
            [a, p, m, n, t]])
