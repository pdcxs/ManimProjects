from manimlib.imports import *
from ManimProjects.utils.Parabola import Parabola
from ManimProjects.utils.geometry import CText

class Prob1Open(Scene):
    def construct(self):
        line1_1 = CText('抛物线')
        line1_1.set_fill(DARK_BLUE)

        line1_2 = CText('性质三')
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
        'x_min' : -5,
        'focus' : 2
    }
    def construct(self):
        self.adjust_x_range()
        graph = self.get_graph(color=LIGHT_BROWN)
        directrix = self.get_directrix()
        focus = Dot().move_to(self.get_focus())
        focus.set_fill(DARK_BROWN)
        focus.plot_depth = 1
        focusLabel = TexMobject('F').scale(0.5)
        focusLabel.next_to(focus, RIGHT, buff=SMALL_BUFF)

        self.play(*[ShowCreation(e) for\
            e in [graph, directrix, focus, focusLabel]])

        sub1 = CText('P1P2为抛物线正焦弦').scale(0.3)
        sub1.to_edge(RIGHT)

        self.wait(2)
        self.play(Write(sub1))

        p1 = Dot()
        p1.move_to(self.coords_to_point(
            self.focus,
            2 * self.focus
        ))
        p1.plot_depth = 1
        p1.set_fill(DARK_BROWN)

        p2 = Dot()
        p2.move_to(self.coords_to_point(
            self.focus,
            -2 * self.focus
        ))
        p2.plot_depth = 1
        p2.set_fill(DARK_BROWN)

        p1_label = TexMobject('P_1').scale(0.5)
        p1_label.next_to(p1, RIGHT)

        p2_label = TexMobject('P_2').scale(0.5)
        p2_label.next_to(p2, RIGHT)

        self.play(ShowCreation(p1), ShowCreation(p2))
        self.play(ShowCreation(Line(p1, p2)))
        self.play(
            ShowCreation(p1_label),
            ShowCreation(p2_label)
        )
        self.wait()

        x = Dot()
        x.move_to(self.coords_to_point(
            -self.focus,
            0
        ))
        x.set_fill(DARK_BROWN)
        x.plot_depth = 1

        x_label = TexMobject('X').scale(0.5)
        x_label.next_to(x, LEFT)

        sub2 = CText('X为轴与准线的交点').scale(0.3)
        sub2.to_edge(RIGHT)

        self.play(FadeOut(sub1))
        self.play(FadeIn((sub2)))
        self.wait()

        h_line = Line(focus, x)
        h_line.plot_depth = 2

        self.play(ShowCreation(h_line))
        self.play(ShowCreation(x))
        self.play(FadeOut(h_line))
        self.play(Write(x_label))
        self.wait()

        sub3 = CText('则P1与P2的切线交于X').scale(0.3)
        sub3.to_edge(RIGHT)

        self.play(FadeOut(sub2))
        self.play(Write(sub3))

        p1_tangent = Line()
        self.add_tangent_line_updater(
            p1_tangent,
            p1
        )

        p2_tangent = Line()
        self.add_tangent_line_updater(
            p2_tangent,
            p2
        )

        self.play(
            ShowCreation(p1_tangent),
            ShowCreation(p2_tangent)
        )

        self.wait()

        self.play(ShowCreation(
            DashedLine(x, focus)
        ))

        m1 = Dot()
        m1.move_to(self.coords_to_point(
            -self.focus,
            2 * self.focus
        ))
        m1.set_fill(DARK_BROWN)
        m1.plot_depth = 1

        m1_label = TexMobject('M_1').scale(0.5)
        m1_label.next_to(m1, LEFT)

        self.play(ShowCreation(m1))
        self.play(ShowCreation(m1_label))
        self.play(ShowCreation(DashedLine(p1, m1)))

        sub4 = CText('在正方形XFP1M1中，XP1是对角线')
        sub4.scale(0.3)
        sub4.to_edge(RIGHT)
        self.play(FadeOut(sub3))
        self.play(Write(sub4))

        self.wait(5)
        self.play(ShowCreationThenDestruction(
            Polygon(
                x.get_center(),
                focus.get_center(),
                p1.get_center(),
                m1.get_center()
            )
        ))

        sub5 = CText(
            'XP1也正好平分角M1P1F，因此是过P1点的切线')
        sub5.scale(0.3)
        sub5.to_edge(RIGHT)

        self.wait(5)
        self.play(FadeOut(sub4))
        self.play(Write(sub5))

        sub6 = CText('同理，P2X也为切线')
        sub6.scale(0.3)
        sub6.to_edge(RIGHT)

        self.wait(5)
        self.play(FadeOut(sub5))
        self.play(Write(sub6))

        sub7 = CText(
            '总结：抛物线正焦弦端点切线交于准线与轴的交点')
        sub7.scale(0.3)
        sub7.to_edge(RIGHT)

        self.wait(5)
        self.play(FadeOut(sub6))
        self.play(Write(sub7))

        self.wait(10)

class Prob2Open(Scene):
    def construct(self):
        line1_1 = CText('抛物线')
        line1_1.set_fill(DARK_BLUE)

        line1_2 = CText('性质三')
        line1 = VGroup(line1_1, line1_2)
        line1.arrange(RIGHT)
        line2 = CText('推论二')
        lines = VGroup(line1, line2)
        lines.arrange(DOWN, buff=LARGE_BUFF)
        self.play(Write(line1))
        self.wait(3)
        self.play(Write(line2))
        self.wait(3)
        
        self.play(FadeOut(lines))

class Prob2(Parabola):
    CONFIG = {
        'x_min' : -5,
        'focus' : 2
    }
    def construct(self):
        self.adjust_x_range()
        graph = self.get_graph(color=LIGHT_BROWN)
        directrix = self.get_directrix()
        focus = Dot().move_to(self.get_focus())
        focus.set_fill(DARK_BROWN)
        focus.plot_depth = 1
        focusLabel = TexMobject('F').scale(0.5)
        focusLabel.next_to(focus, RIGHT, buff=SMALL_BUFF)

        self.play(*[ShowCreation(e) for\
            e in [graph, directrix, focus, focusLabel]])

        y_val = ValueTracker(8)
        
        p = Dot()
        p.plot_depth = 1
        p.set_fill(DARK_BLUE)
        p.add_updater(lambda m:\
            m.move_to(self.coords_to_point(
                self.func(y_val.get_value()),
                y_val.get_value()
            )))

        p_label = TexMobject('P').scale(0.5)
        p_label.plot_depth = 1
        p_label.add_updater(lambda m:\
            m.next_to(p, RIGHT, buff=SMALL_BUFF))

        k = Dot()
        k.plot_depth = 1
        k.set_fill(DARK_BLUE)
        k.add_updater(lambda m:\
            m.move_to(self.get_tangent_to_directrix(
                p
            )))
        
        k_label = TexMobject('K').scale(0.5)
        k_label.plot_depth = 1
        k_label.add_updater(lambda m:\
            m.next_to(k, LEFT, buff=SMALL_BUFF))
        
        tangent = Line()
        self.add_tangent_line_updater(tangent, p)

        self.play(ShowCreation(p))
        self.play(ShowCreation(p_label))
        self.play(ShowCreation(tangent))
        self.play(ShowCreation(k))
        self.play(ShowCreation(k_label))
        
        def get_extent(l):
            l.put_start_and_end_on(p.get_center(),
                RIGHT * 10)
            l.set_angle(tangent.get_angle() + PI)
        tangent_extent = Line()
        tangent_extent.add_updater(lambda l:\
            get_extent(l))

        self.play(ShowCreation(tangent_extent))
        self.wait()

        m = Dot()
        m.set_fill(DARK_BLUE)
        m.plot_depth = 1
        m.add_updater(lambda e:\
            e.move_to(self.coords_to_point(
                -self.focus,
                y_val.get_value()
            )))
        
        m_label = TexMobject('M').scale(0.5)
        m_label.add_updater(lambda e:\
            e.next_to(m, LEFT, buff=SMALL_BUFF))
        
        mp = Line()
        mp.add_updater(lambda l:\
            l.put_start_and_end_on(
                p.get_center(),
                self.coords_to_point(
                    -self.focus,
                    y_val.get_value()
            )))

        fp = Line()
        fp.add_updater(lambda l:\
            l.put_start_and_end_on(
                focus.get_center(),
                p.get_center()
            ))

        self.play(ShowCreation(mp), ShowCreation(fp))
        self.play(ShowCreation(m))
        self.play(ShowCreation(m_label))

        kf = Line()
        kf.add_updater(lambda l:\
            l.put_start_and_end_on(
                k.get_center(),
                focus.get_center()
            ))
        self.play(ShowCreation(kf))
        self.wait()

        sub1 = CText('在切线上任取一点O')
        sub1.scale(0.3)
        sub1.to_edge(RIGHT)

        self.play(Write(sub1))
        self.wait()

        ot = ValueTracker(0.2)
        vec_kp = p.get_center() - k.get_center()

        o = Dot()
        o.plot_depth = 1
        o.set_fill(RED)
        o.add_updater(lambda m:\
            m.move_to(k.get_center() +\
                vec_kp * ot.get_value()))
        
        o_label = TexMobject('O').scale(0.5)
        o_label.plot_depth = 1
        o_label.add_updater(lambda m:\
            m.next_to(o, DR, buff=SMALL_BUFF))
        
        self.play(ShowCreation(o))
        self.play(ShowCreation(o_label))
        self.wait()

        sub2 = CText('则OM=OF')
        sub2.scale(0.3)
        sub2.to_edge(RIGHT)

        self.play(FadeOut(sub1))
        self.play(Write(sub2))
        self.wait()

        om = Line()
        om.add_updater(lambda l:\
            l.put_start_and_end_on(
                o.get_center(),
                m.get_center()
            ))
        of = Line()
        of.add_updater(lambda l:\
            l.put_start_and_end_on(
                o.get_center(),
                focus.get_center()
            ))
        
        self.play(ShowCreation(om), ShowCreation(of))
        self.wait()

        self.play(ot.set_value, 0.05)
        self.wait()
        self.play(ot.set_value, 0.8)
        self.wait()
        self.play(ot.set_value, 1.2)
        self.wait()
        self.play(ot.set_value, 0.6)
        self.wait(3)
