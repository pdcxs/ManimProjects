from manimlib.imports import *
from ManimProjects.utils.Parabola import Parabola
from ManimProjects.utils.geometry import *

class Prop3(Parabola):
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

        focus_label = TexMobject('F').scale(0.5)
        focus_label.next_to(focus, DOWN, buff=SMALL_BUFF)
        self.play(Write(focus_label))

        y_val = ValueTracker(8)
        
        p = Dot()
        p.plot_depth = 1
        p.set_fill(DARK_BLUE)
        p.add_updater(lambda m:\
            m.move_to(self.coords_to_point(
                self.func(y_val.get_value()),
                y_val.get_value()
            )))
        
        k = Dot()
        k.plot_depth = 1
        k.set_fill(DARK_BLUE)
        k.add_updater(lambda m:\
            m.move_to(self.get_tangent_to_directrix(
                p
            )))
        
        tangent = Line()
        self.add_tangent_line_updater(tangent, p)

        self.play(ShowCreation(p))
        self.play(ShowCreation(tangent))
        self.play(ShowCreation(k))

        ang2 = Angle(k, p, focus)
        ang2.make_angle_dynamic()
        ang2_label = TexMobject('2').scale(0.5)
        ang2.add_label(ang2_label)

        self.play(ShowCreation(ang2))
        self.play(ShowCreation(ang2_label))

        self.play(y_val.set_value, 4)