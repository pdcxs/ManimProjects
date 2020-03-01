from manimlib.imports import *
from ManimProjects.utils.geometry import *
from ManimProjects.utils.Parabola import *
from ManimProjects.utils.rate_functions import *
from ManimProjects.utils.calculation import *

TEX_SIZE = 0.65
TEXT_SIZE = 0.3

class Prob1Open(Scene):
    def construct(self):
        line1_1 = CText('抛物线')
        line1_1.set_fill(DARK_BLUE)

        line1_2 = CText('性质五')
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
    def construct(self):
        self.adjust_x_range()
        f = Dot()
        f.plot_depth = 1
        f.move_to(self.get_focus())
        f.set_fill(DARK_BROWN)

        f_label = Label(
            TexMobject('F').scale(TEX_SIZE),
            f,
            direction=DOWN
        )

        h_line = self.get_horizontal()
        directrix = self.get_directrix()
        graph = self.get_graph(DARK_BROWN)

        self.play(*[ShowCreation(e) for e in\
            [f, f_label, h_line, directrix, graph]])
        self.wait()

        y_val = ValueTracker(6)

        p = Dot()
        p.plot_depth = 1
        p.set_color(DARK_BLUE)
        p.add_updater(lambda m:\
            m.move_to(self.value_to_point(
                y_val.get_value())))
        self.play(ShowCreation(p))

        p_label = Label(
            TexMobject('P').scale(TEX_SIZE),
            p,
            direction=RIGHT
        )
        p_label.make_dynamic()
        self.play(ShowCreation(p_label))
        self.wait()

        tangent = Line()
        self.add_tangent_extent_updater(tangent, p)

        self.play(ShowCreation(tangent))
        self.wait()

        normal = Line()
        self.add_normal_updater(normal, p)
        self.play(ShowCreation(normal))
        self.wait()

        t = Dot()
        t.plot_depth = 1
        t.set_color(DARK_BLUE)
        t.add_updater(lambda m:\
            m.move_to(get_intersect(tangent, h_line, f)))
        
        self.play(ShowCreation(t))

        t_label = Label(
            TexMobject('T').scale(TEX_SIZE),
            t, direction=DOWN
        )
        t_label.make_dynamic()
        self.play(ShowCreation(t_label))
        self.wait()

        g = Dot()
        g.plot_depth = 1
        g.set_color(DARK_BLUE)
        g.add_updater(lambda m:\
            m.move_to(get_intersect(normal, h_line, f)))
        
        self.play(ShowCreation(g))

        g_label = Label(
            TexMobject('G').scale(TEX_SIZE),
            g, direction=DOWN
        )
        g_label.make_dynamic()
        self.play(ShowCreation(g_label))
        self.wait()

        pf = Line()
        pf.add_updater(lambda l:\
            l.put_start_and_end_on(
                p.get_center(),
                f.get_center()
            ))
        self.play(ShowCreation(pf))
        self.wait()

        m = Dot()
        m.plot_depth = 1
        m.set_color(DARK_BLUE)

        self.add_directrix_point_updater(p, m)
        self.play(ShowCreation(m))

        m_label = Label(
            TexMobject('M').scale(TEX_SIZE),
            m, direction=LEFT
        )
        m_label.make_dynamic()
        self.play(ShowCreation(m_label))

        mp = Line()
        mp.add_updater(lambda l:\
            l.put_start_and_end_on(
                m.get_center(),
                p.get_center()
            ))
        self.play(ShowCreation(mp))
        self.wait()

        fm = Line()
        fm.add_updater(lambda l:\
            l.put_start_and_end_on(
                f.get_center(),
                m.get_center()
            ))
        self.play(ShowCreation(fm))
        self.wait()

        o = Dot()
        o.plot_depth = 1
        o.set_color(DARK_BLUE)
        o.add_updater(lambda e:\
            e.move_to(get_intersect(
                fm, tangent, f
            )))
        self.play(ShowCreation(o))

        o_label = Label(
            TexMobject('O').scale(TEX_SIZE),
            o, direction=LEFT
        )
        o_label.make_dynamic()
        self.play(ShowCreation(o_label))
        self.wait()

        sub1_1 = TexMobject('TP, FM')
        sub1_1.scale(TEX_SIZE)
        sub1_2 = CText('相互垂直平分')
        sub1_2.scale(TEXT_SIZE)
        sub1 = VGroup(sub1_1, sub1_2)
        sub1.arrange(RIGHT, buff=SMALL_BUFF)

        sub2 = CText('证明思路：').scale(TEXT_SIZE)
        sub3 = TexMobject('\\triangle FOP \\cong \\triangle MOP')
        sub3.scale(TEX_SIZE)

        proof = VGroup(sub1, sub2, sub3)
        proof.arrange(DOWN)
        sub2.align_to(sub1, LEFT)
        sub3.align_to(sub2, LEFT)
        proof.to_corner(UR)

        self.play(ShowCreation(proof), run_time=10)
        self.wait(10)

        right = Angle(p, o, m, is_right=True)
        right.radius = 0.2
        right.make_angle_dynamic()
        self.play(ShowCreation(right))
        self.wait()

        self.play(y_val.set_value, 1, run_time=10)
        self.wait(5)

        self.play(y_val.set_value, 10, run_time=10)
        self.wait(5)

        self.play(y_val.set_value, 6, rate_func=easeOutElastic)
        self.wait(15)
