from manimlib.imports import *
from ManimProjects.utils.geometry import *
from ManimProjects.utils.Parabola import *
from ManimProjects.utils.rate_functions import *

TEX_SIZE = 0.65
TEXT_SIZE = 0.3

class Prob1Open(Scene):
    def construct(self):
        line1_1 = CText('抛物线')
        line1_1.set_fill(DARK_BLUE)

        line1_2 = CText('性质四')
        line1 = VGroup(line1_1, line1_2)
        line1.arrange(RIGHT)
        line2 = CText('推论一')
        lines = VGroup(line1, line2)
        lines.arrange(DOWN, buff=LARGE_BUFF)
        self.play(Write(line1))
        self.wait(3)
        self.play(Write(line2))
        self.wait(3)
        
        self.play(FadeOut(lines))

class Prob1(Parabola):
    CONFIG = {
        "x_min": -8,
        "focus": 2
    }
    def construct(self):
        self.adjust_x_range()
        graph = self.get_graph(color=DARK_BROWN)
        f = Dot()
        f.move_to(self.get_focus())
        f.plot_depth = 1
        f.set_color(DARK_BROWN)
        f_label = Label(
            TexMobject('F').scale(TEX_SIZE),
            f)
        f_label.next_to(f, RIGHT, buff=SMALL_BUFF)
        f_label.plot_depth = 1
        directrix = self.get_directrix()

        self.play(
            *[ShowCreation(e) for e in\
                [f, f_label, graph, directrix]]
        )
        self.wait()

        y_val = ValueTracker(8)

        p1 = Dot()
        p1.plot_depth = 1
        p1.set_color(DARK_BLUE)
        p1.add_updater(lambda m:\
            m.move_to(self.value_to_point(
                y_val.get_value()
            )))
        
        p1_label = Label(
            TexMobject('P_1').scale(TEX_SIZE),
            p1)
        
        self.play(
            ShowCreation(p1),
            ShowCreation(p1_label)
        )

        p1_label.make_dynamic()
        
        p2 = Dot()
        p2.plot_depth = 1
        p2.set_color(DARK_BLUE)
        p2.add_updater(lambda m:\
            m.move_to(self.get_opposite(p1)))
        
        p2_label = Label(
            TexMobject('P_2').scale(TEX_SIZE),
            p2)

        p1p2 = Line()
        p1p2.add_updater(lambda m:\
            m.put_start_and_end_on(
                p1.get_center(),
                self.get_opposite(p1)
            ))
        
        self.play(ShowCreation(p1p2))
        
        self.play(
            ShowCreation(p2),
            ShowCreation(p2_label)
        )
        self.wait()

        p2_label.make_dynamic()

        tangent1 = Line()
        self.add_tangent_extent_updater(tangent1, p1)

        self.play(ShowCreation(tangent1))
        self.wait()

        tangent2 = Line()
        self.add_tangent_extent_updater(tangent2, p2)

        self.play(ShowCreation(tangent2))
        self.wait()

        z = Dot()
        z.plot_depth = 1
        z.set_color(DARK_BLUE)
        z.add_updater(lambda m:\
            m.move_to(self.get_tangent_to_directrix(p1)))
        
        z_label = TexMobject('Z').scale(TEX_SIZE)
        z_label.next_to(z, LEFT, buff=SMALL_BUFF)

        self.play(
            ShowCreation(z),
            ShowCreation(z_label)
        )
        self.wait()

        z_label.add_updater(lambda m:\
            m.next_to(z, LEFT, buff=SMALL_BUFF))
        
        m1 = Dot()
        m1.plot_depth = 1
        m1.set_color(DARK_BLUE)
        self.add_directrix_point_updater(p1, m1)

        p1m1 = Line()
        p1m1.put_start_and_end_on(
                p1.get_center(),
                m1.get_center()
            )

        m1_label = Label(
            TexMobject('M_1').scale(TEX_SIZE),
            m1,
            direction = LEFT
        )
        m1_label.plot_depth = 1

        self.play(ShowCreation(p1m1))

        self.play(
            ShowCreation(m1),
            ShowCreation(m1_label)
        )
        self.wait()
        m1_label.make_dynamic()
        p1m1.add_updater(lambda l:\
            l.put_start_and_end_on(
                p1.get_center(),
                m1.get_center()
            ))

        m2 = Dot()
        m2.plot_depth = 1
        m2.set_color(DARK_BLUE)
        self.add_directrix_point_updater(p2, m2)

        p2m2 = Line()
        p2m2.put_start_and_end_on(
                p2.get_center(),
                m2.get_center()
            )

        m2_label = Label(
            TexMobject('M_2').scale(TEX_SIZE),
            m2,
            direction = LEFT
        )
        m2_label.plot_depth = 1

        self.play(ShowCreation(p2m2))

        self.play(
            ShowCreation(m2),
            ShowCreation(m2_label)
        )
        self.wait()
        m2_label.make_dynamic()
        p2m2.add_updater(lambda l:\
            l.put_start_and_end_on(
                p2.get_center(),
                m2.get_center()
            ))

        zm1 = Line()
        zm1.set_color(RED)
        zm1.add_updater(lambda l:\
            l.put_start_and_end_on(
                z.get_center(),
                m1.get_center()
            ))
        self.play(ShowCreation(zm1))

        zm2 = Line()
        zm2.set_color(MAROON_E)
        zm2.add_updater(lambda l:\
            l.put_start_and_end_on(
                z.get_center(),
                m2.get_center()
            ))
        self.play(ShowCreation(zm2))
        self.wait()

        circle = Circle()

        def update_circle(c):
            pos1 = p1.get_center()
            pos2 = p2.get_center()
            o = (pos1 + pos2) / 2
            d = np.linalg.norm(pos2 - pos1)
            c.move_to(o)
            c.set_width(d)
        
        circle.add_updater(lambda m:\
            update_circle(m))
        
        self.play(ShowCreation(circle))
        self.wait()

        sub1 = TexMobject('ZM_1=ZM_2').scale(TEX_SIZE)
        sub2 = CText('以P1P2为直径的圆切准线于点Z')
        sub2.scale(TEXT_SIZE)

        sub = VGroup(sub1, sub2)
        sub.arrange(DOWN)
        sub.to_edge(RIGHT)

        self.play(Write(sub))
        self.wait(5)

        self.play(
            y_val.set_value, 3,
            rate_func=easeOutElastic
        )
        self.wait(5)

        self.play(
            y_val.set_value, 1,
            rate_func=easeOutBounce
        )
        self.wait(5)

        self.play(
            y_val.set_value, 9,
            rate_func=easeOutElastic
        )
        self.wait(5)
        