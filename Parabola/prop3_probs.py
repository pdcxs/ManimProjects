from manimlib.imports import *
from ManimProjects.utils.Parabola import Parabola
from ManimProjects.utils.geometry import CText
from ManimProjects.utils.calculation import get_intersect

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

class Prob3Open(Scene):
    def construct(self):
        line1_1 = CText('抛物线')
        line1_1.set_fill(DARK_BLUE)

        line1_2 = CText('性质三')
        line1 = VGroup(line1_1, line1_2)
        line1.arrange(RIGHT)
        line2 = CText('推论三')
        lines = VGroup(line1, line2)
        lines.arrange(DOWN, buff=LARGE_BUFF)
        self.play(Write(line1))
        self.wait(3)
        self.play(Write(line2))
        self.wait(3)
        
        self.play(FadeOut(lines))

class Prob3(Parabola):
    CONFIG = {
        'x_min' : -10,
        'focus' : 2
    }
    def construct(self):
        self.adjust_x_range()
        graph = self.get_graph(color=LIGHT_BROWN)
        directrix = self.get_directrix()
        focus = Dot().move_to(self.get_focus())
        focus.set_fill(DARK_BROWN)
        focus.plot_depth = 2
        focusLabel = TexMobject('F').scale(0.5)
        focusLabel.next_to(focus, RIGHT, buff=SMALL_BUFF)

        self.play(*[ShowCreation(e) for\
            e in [graph, directrix, focus, focusLabel]])

        y1_val = ValueTracker(8)
        
        p1 = Dot()
        p1.plot_depth = 1
        p1.set_fill(DARK_BLUE)
        p1.add_updater(lambda m:\
            m.move_to(self.coords_to_point(
                self.func(y1_val.get_value()),
                y1_val.get_value()
            )))

        p1_label = TexMobject('P_1').scale(0.5)
        p1_label.plot_depth = 1
        p1_label.add_updater(lambda m:\
            m.next_to(p1, RIGHT, buff=SMALL_BUFF))
        
        tangent1 = Line()
        self.add_tangent_line_updater(tangent1, p1)

        self.play(ShowCreation(p1))
        self.play(ShowCreation(p1_label))
        self.play(ShowCreation(tangent1))
        # self.play(ShowCreation(k1))
        # self.play(ShowCreation(k1_label))
        
        def get_extent(l, p, t):
            l.put_start_and_end_on(LEFT * 10,
                RIGHT * 10)
            l.set_angle(t.get_angle() + PI)
            l.move_to(p.get_center())
        tangent1_extent = Line()
        tangent1_extent.add_updater(lambda l:\
            get_extent(l, p1, tangent1))

        self.play(ShowCreation(tangent1_extent))
        self.wait()

        m1 = Dot()
        m1.set_fill(DARK_BLUE)
        m1.plot_depth = 1
        m1.add_updater(lambda e:\
            e.move_to(self.coords_to_point(
                -self.focus,
                y1_val.get_value()
            )))
        
        m1_label = TexMobject('M_1').scale(0.5)
        m1_label.add_updater(lambda e:\
            e.next_to(m1, LEFT, buff=SMALL_BUFF))
        
        m1p1 = Line()
        m1p1.add_updater(lambda l:\
            l.put_start_and_end_on(
                p1.get_center(),
                self.coords_to_point(
                    -self.focus,
                    y1_val.get_value()
            )))

        fp1 = Line()
        fp1.add_updater(lambda l:\
            l.put_start_and_end_on(
                focus.get_center(),
                p1.get_center()
            ))

        self.play(ShowCreation(m1p1), ShowCreation(fp1))
        self.play(ShowCreation(m1))
        self.play(ShowCreation(m1_label))

        y2_val = ValueTracker(-6)
        
        p2 = Dot()
        p2.plot_depth = 1
        p2.set_fill(DARK_BLUE)
        p2.add_updater(lambda m:\
            m.move_to(self.coords_to_point(
                self.func(y2_val.get_value()),
                y2_val.get_value()
            )))

        p2_label = TexMobject('P_2').scale(0.5)
        p2_label.plot_depth = 1
        p2_label.add_updater(lambda m:\
            m.next_to(p2, RIGHT, buff=SMALL_BUFF))
        
        tangent2 = Line()
        self.add_tangent_line_updater(tangent2, p2)

        self.play(ShowCreation(p2))
        self.play(ShowCreation(p2_label))
        self.play(ShowCreation(tangent2))
        
        tangent2_extent = Line()
        tangent2_extent.add_updater(lambda l:\
            get_extent(l, p2, tangent2))

        self.play(ShowCreation(tangent2_extent))
        self.wait()

        m2 = Dot()
        m2.set_fill(DARK_BLUE)
        m2.plot_depth = 1
        m2.add_updater(lambda e:\
            e.move_to(self.coords_to_point(
                -self.focus,
                y2_val.get_value()
            )))
        
        m2_label = TexMobject('M_2').scale(0.5)
        m2_label.add_updater(lambda e:\
            e.next_to(m2, LEFT, buff=SMALL_BUFF))
        
        m2p2 = Line()
        m2p2.add_updater(lambda l:\
            l.put_start_and_end_on(
                p2.get_center(),
                self.coords_to_point(
                    -self.focus,
                    y2_val.get_value()
            )))

        fp2 = Line()
        fp2.add_updater(lambda l:\
            l.put_start_and_end_on(
                focus.get_center(),
                p2.get_center()
            ))

        self.play(ShowCreation(m2p2), ShowCreation(fp2))
        self.play(ShowCreation(m2))
        self.play(ShowCreation(m2_label))

        o = Dot()
        o.plot_depth = 1
        o.set_fill(DARK_BROWN)
        o.add_updater(lambda m:\
            m.move_to(get_intersect(tangent1, tangent2, focus)))
        
        self.play(ShowCreation(o))

        o_label = TexMobject('O').scale(0.5)
        o_label.add_updater(lambda m:\
            m.next_to(o, LEFT, buff=SMALL_BUFF))

        self.play(ShowCreation(o_label))
        self.wait(3)

        om1 = Line()
        om1.add_updater(lambda l:\
            l.put_start_and_end_on(
                o.get_center(),
                m1.get_center()
            ))
        
        om2 = Line()
        om2.add_updater(lambda l:\
            l.put_start_and_end_on(
                o.get_center(),
                m2.get_center()
            ))
        
        of = Line()
        of.add_updater(lambda l:\
            l.put_start_and_end_on(
                o.get_center(),
                focus.get_center()
            ))

        om1.set_color(RED)
        om2.set_color(RED)
        of.set_color(RED)
        
        self.play(ShowCreation(om1))
        self.play(ShowCreation(om2))
        self.play(ShowCreation(of))

        self.wait(3)

        sub = TexMobject("OM_1=OF=OM_2").scale(0.5)
        sub.to_edge(RIGHT)
        sub.shift(LEFT * 3)
        self.play(Write(sub))

        self.wait(3)

        self.play(y1_val.set_value, 2)
        self.wait(3)
        self.play(y2_val.set_value, -1)
        self.wait(3)
        self.play(
            ApplyMethod(y1_val.set_value, 6),
            ApplyMethod(y2_val.set_value, -8)
        )
        self.wait(6)

class Prob4Open(Scene):
    def construct(self):
        line1_1 = CText('抛物线')
        line1_1.set_fill(DARK_BLUE)

        line1_2 = CText('性质三')
        line1 = VGroup(line1_1, line1_2)
        line1.arrange(RIGHT)
        line2 = CText('推论四')
        lines = VGroup(line1, line2)
        lines.arrange(DOWN, buff=LARGE_BUFF)
        self.play(Write(line1))
        self.wait(3)
        self.play(Write(line2))
        self.wait(3)
        
        self.play(FadeOut(lines))

from ManimProjects.utils.rate_functions import *

class Prob4(Parabola):
    CONFIG = {
        'x_min' : -10,
        'focus' : 2
    }
    def construct(self):
        self.adjust_x_range()
        graph = self.get_graph(color=LIGHT_BROWN)
        directrix = self.get_directrix()
        focus = Dot().move_to(self.get_focus())
        focus.set_fill(DARK_BROWN)
        focus.plot_depth = 2
        focusLabel = TexMobject('F').scale(0.5)
        focusLabel.next_to(focus, RIGHT, buff=SMALL_BUFF)

        self.play(*[ShowCreation(e) for\
            e in [graph, directrix, focus, focusLabel]])
        self.wait()

        sub1 = CText('任取一点P').scale(0.3)
        sub1.to_edge(RIGHT)
        self.play(ShowCreation(sub1))

        y_val = ValueTracker(6)

        p = Dot()
        p.plot_depth = 1
        p.set_fill(DARK_BLUE)
        p.add_updater(lambda m:\
            m.move_to(self.coords_to_point(
                self.func(y_val.get_value()),
                y_val.get_value()
            )))

        self.play(ShowCreation(p))

        p_label = TexMobject('P').scale(0.5)
        p_label.plot_depth = 1
        p_label.add_updater(lambda m:\
            m.next_to(p, RIGHT, buff=SMALL_BUFF))
        self.play(ShowCreation(p_label))
        self.wait()

        self.play(FadeOut(sub1))

        sub2 = CText('过点P做抛物线的切线')
        sub2.scale(0.3)
        sub2.to_edge(RIGHT)
        self.play(ShowCreation(sub2))
        self.wait()

        tangent = Line()
        self.add_tangent_line_updater(tangent, p)
        # self.play(ShowCreation(tangent))
        # self.wait()

        tangent_extent = Line()
        def get_extent(l, p, t):
            l.put_start_and_end_on(LEFT * 10,
                RIGHT * 10)
            l.set_angle(t.get_angle() + PI)
            l.move_to(p.get_center())
        tangent_extent.add_updater(lambda l:\
            get_extent(l, p, tangent))
        tangent_line = VGroup()
        tangent_line.add(tangent)
        tangent_line.add(tangent_extent)
        self.play(ShowCreation(tangent_extent))
        self.add(tangent_line)
        
        self.wait()

        self.play(FadeOut(sub2))
        
        sub3 = CText('交准线于Z').scale(0.3)
        sub3.to_edge(RIGHT)
        self.play(ShowCreation(sub3))
        self.wait()

        z = Dot()
        z.plot_depth = 1
        z.set_fill(DARK_BLUE)
        z.add_updater(lambda m:\
            m.move_to(self.get_tangent_to_directrix(p)))
        self.play(ShowCreation(z))
        
        z_label = TexMobject('Z').scale(0.5)
        z_label.plot_depth = 1
        z_label.add_updater(lambda m:\
            m.next_to(z, LEFT, buff=SMALL_BUFF))
        self.play(ShowCreation(z_label))
        self.wait()

        self.play(FadeOut(sub3))
        sub4 = CText('交正焦弦于点K').scale(0.3)
        sub4.to_edge(RIGHT)
        self.play(ShowCreation(sub4))
        self.wait()

        def find_k():
            start = z.get_center()
            vec = p.get_center() - start
            vec /= vec[0]
            d = focus.get_center()[0] - start[0]
            vec *= d
            return start + vec
        
        k = Dot()
        k.plot_depth = 1
        k.set_fill(DARK_BLUE)
        k.add_updater(lambda m:\
            m.move_to(find_k()))

        k_label = TexMobject('K').scale(0.5)
        k_label.plot_depth = 1
        k_label.add_updater(lambda m:\
            m.next_to(k, RIGHT, buff=SMALL_BUFF))
        
        def find_opp():
            pos = find_k()
            fac = -1
            if pos[1] < 0:
                fac = 1
            return self.coords_to_point(
                self.func(self.focus * 2),
                fac * self.focus * 2
            )
        k_line = Line()
        k_line.add_updater(lambda m:\
            m.put_start_and_end_on(
                find_k(),
                find_opp()
            ))

        self.play(ShowCreation(k_line))
        self.play(ShowCreation(k))
        self.play(ShowCreation(k_label))

        self.wait()

        self.play(FadeOut(sub4))
        sub5 = CText('则ZF=KF').scale(0.3)
        sub5.to_edge(RIGHT)
        self.play(ShowCreation(sub5))
        self.wait()

        zf = Line()
        zf.set_color(RED)
        zf.add_updater(lambda m:\
            m.put_start_and_end_on(
                z.get_center(),
                focus.get_center()
            ))
        kf = Line()
        kf.set_color(RED)
        kf.add_updater(lambda m:\
            m.put_start_and_end_on(
                k.get_center(),
                focus.get_center()
            ))
        self.play(
            ShowCreation(zf),
            ShowCreation(kf))
        self.wait()

        self.play(y_val.set_value, 9,
            rate_func=easeOutElastic,
            run_time=2)
        self.wait()

        self.play(y_val.set_value, 1,
            rate_func=easeOutBounce,
            run_time=2)
        self.wait()

        self.play(y_val.set_value, -6,
            rate_func=easeOutElastic,
            run_time=2)
        self.wait()

        self.play(y_val.set_value, 8,
            rate_func=easeOutBounce,
            run_time=2)
        self.wait()

        self.play(FadeOut(sub5))

        m = Dot()
        m.plot_depth = 1
        m.set_fill(YELLOW)
        m.add_updater(lambda e:\
            e.move_to(z.get_center()[0] * RIGHT +
                p.get_center()[1] * UP))

        m_label = TexMobject('M').scale(0.5)
        m_label.add_updater(lambda e:\
            e.next_to(m, LEFT, buff=SMALL_BUFF))
        
        self.play(ShowCreation(m))
        self.play(ShowCreation(m_label))

        mp = DashedLine()
        mp.add_updater(lambda l:\
            l.put_start_and_end_on(
                m.get_center(),
                p.get_center()
            ))
        self.play(ShowCreation(mp))

        fp = DashedLine()
        fp.add_updater(lambda l:\
            l.put_start_and_end_on(
                focus.get_center(),
                p.get_center()
            ))
        self.play(ShowCreation(fp))
        self.wait()

        km = DashedLine()
        km.add_updater(lambda l:\
            l.put_start_and_end_on(
                k.get_center(),
                m.get_center()
            ))
        self.play(ShowCreation(km))

        k2 = Dot()
        k2.plot_depth = 1
        k2.set_fill(YELLOW)
        k2.add_updater(lambda m:\
            m.move_to(
                k.get_center()[1] * UP +
                z.get_center()[0] * RIGHT
            ))
        self.play(ShowCreation(k2))

        k2_label = TexMobject('K\'').scale(0.5)
        k2_label.add_updater(lambda m:\
            m.next_to(k2, LEFT, buff=SMALL_BUFF))
        self.play(ShowCreation(k2_label))

        kk2 = DashedLine()
        kk2.add_updater(lambda l:\
            l.put_start_and_end_on(
                k.get_center(),
                k2.get_center()
            ))
        self.play(ShowCreation(kk2))

        z2 = Dot()
        z2.plot_depth = 1
        z2.set_fill(YELLOW)
        z2.add_updater(lambda m:\
            m.move_to(
                z.get_center()[1] * UP +
                focus.get_center()[0] * RIGHT
            ))
        self.play(ShowCreation(z2))

        z2f = Line()
        z2f.plot_depth = -1
        z2f.add_updater(lambda l:\
            l.put_start_and_end_on(
                z2.get_center(),
                focus.get_center()
            ))
        self.add(z2f)

        z2_label = TexMobject('Z\'').scale(0.5)
        z2_label.add_updater(lambda m:\
            m.next_to(z2, UR, buff=SMALL_BUFF))
        self.play(ShowCreation(z2_label))

        zz2 = DashedLine()
        zz2.add_updater(lambda l:\
            l.put_start_and_end_on(
                z.get_center(),
                z2.get_center()
            ))
        self.play(ShowCreation(zz2))
        self.wait()

        self.play(
            kk2.set_color, RED
        )
        self.play(
            zz2.set_color, RED
        )

        proof = VGroup()
        proof1 = CText('证明思路').scale(0.3)
        proof2 = TexMobject('KK\'=ZZ\'').scale(0.5)
        proof3 = TexMobject('\\triangle ZKM \\cong \\triangle ZKF')
        proof3.scale(0.5)
        proof.add(proof1)
        proof.add(proof2)
        proof.add(proof3)
        proof.arrange(DOWN)
        proof.to_edge(RIGHT, buff=LARGE_BUFF)
        proof2.align_to(proof1, LEFT)
        proof3.align_to(proof2, LEFT)
        self.play(ShowCreation(proof))
        self.wait(5)

        zkm = Polygon(
            z.get_center(),
            k.get_center(),
            m.get_center()
        )
        zkm.set_fill(DARK_BLUE, opacity=0.5)

        zkf = Polygon(
            z.get_center(),
            k.get_center(),
            focus.get_center()
        )
        zkf.set_fill(DARK_BLUE, opacity=0.5)

        self.play(
            ShowCreationThenDestruction(zkm),
            ShowCreationThenDestruction(zkf)
        )
        self.wait(15)

        self.play(y_val.set_value, 1,
            rate_func=easeOutBounce)
        self.wait(5)

        self.play(y_val.set_value, -1,
            rate_func=easeOutElastic)
        self.wait(5)

        self.play(y_val.set_value, -8,
            rate_func=easeOutBounce)
        self.wait(5)
