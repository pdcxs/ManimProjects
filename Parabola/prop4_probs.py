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
        
class Prob2Open(Scene):
    def construct(self):
        line1_1 = CText('抛物线')
        line1_1.set_fill(DARK_BLUE)

        line1_2 = CText('性质四')
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
            f, direction=DOWN)
        f_label.plot_depth = 1
        directrix = self.get_directrix()

        self.play(
            *[ShowCreation(e) for e in\
                [f, f_label, graph, directrix]]
        )
        self.wait()

        y_val = ValueTracker(8)

        sub1 = CText('作焦点弦PQ')
        sub1.scale(TEXT_SIZE)
        sub1.to_edge(RIGHT)
        self.play(Write(sub1))

        p = Dot()
        p.set_color(DARK_BLUE)
        p.plot_depth = 1
        p.add_updater(lambda m:\
            m.move_to(self.value_to_point(
                y_val.get_value())))
        
        p_label = Label(TexMobject('P').scale(TEX_SIZE), p, direction=UL)
        p_label.plot_depth = 1

        self.play(ShowCreation(p), ShowCreation(p_label))

        p_label.make_dynamic()

        q = Dot()
        q.set_color(DARK_BLUE)
        q.plot_depth = 1
        q.add_updater(lambda m:\
            m.move_to(self.get_opposite(p)))
        
        q_label = Label(TexMobject('Q').scale(TEX_SIZE), q, direction=RIGHT)
        q_label.plot_depth = 1

        pq = Line()
        pq.add_updater(lambda l:\
            l.put_start_and_end_on(
                p.get_center(),
                self.get_opposite(p)
            ))
        self.play(ShowCreation(pq))
        self.play(ShowCreation(q), ShowCreation(q_label))
        q_label.make_dynamic()
        self.wait()

        sub2 = CText('过P、Q作抛物线切线')
        sub2.scale(TEXT_SIZE)
        sub2.to_edge(RIGHT)
        self.play(FadeOut(sub1))
        self.play(Write(sub2))

        tangent_p = Line()
        self.add_tangent_extent_updater(tangent_p, p)

        tangent_q = Line()
        self.add_tangent_extent_updater(tangent_q, q)

        self.play(ShowCreation(tangent_p))
        self.play(ShowCreation(tangent_q))

        self.wait()

        n = Dot()
        n.set_color(DARK_BLUE)
        n.plot_depth = 1
        n.add_updater(lambda m:\
            m.move_to(self.get_tangent_to_directrix(p)))
        
        n_label = Label(TexMobject('N').scale(TEX_SIZE), n, direction=LEFT)
        n_label.plot_depth = 1
        
        self.play(ShowCreation(n))
        self.play(ShowCreation(n_label))
        self.wait()

        n_label.make_dynamic()

        sub3 = CText('过Q点作切线的垂线，即法线')
        sub3.scale(TEXT_SIZE)
        sub3.to_edge(RIGHT)

        self.play(FadeOut(sub2))
        self.play(Write(sub3))
        self.wait()

        normal_q = Line()
        self.add_normal_updater(normal_q, q)

        self.play(ShowCreation(normal_q))
        self.wait()

        sub4 = CText('过Q点的法线交轴于点G')
        sub4.scale(TEXT_SIZE)
        sub4.to_edge(RIGHT)
        
        self.play(FadeOut(sub3))
        self.play(Write(sub4))
        self.wait()

        h_line = Line(LEFT * FRAME_X_RADIUS, RIGHT)
        h_line.plot_depth = -1
        self.play(ShowCreation(h_line))
        self.wait()

        def normal_to_horizontal(point):
            [x, y] = self.point_to_coords(point)
            if y == 0:
                return self.value_to_point(0)
            d = -y / (2 * self.focus)
            dx = y / d
            return self.coords_to_point(
                x - dx, 0
            )
        
        g = Dot()
        g.set_color(DARK_BLUE)
        g.plot_depth = 1
        g.add_updater(lambda m:\
            m.move_to(normal_to_horizontal(q)))

        g_label = Label(TexMobject('G').scale(TEX_SIZE), g, direction=UL)
        
        self.play(ShowCreation(g))
        self.play(ShowCreation(g_label))
        self.wait()

        g_label.make_dynamic()

        gqn = Angle(g, q, n, radius=0.2)
        gqn.make_angle_dynamic()
        self.play(ShowCreation(gqn))

        sub5 = CText('GZ垂直于PN于Z')
        sub5.scale(TEXT_SIZE)
        sub5.to_edge(RIGHT)
        self.play(FadeOut(sub4))
        self.play(Write(sub5))
        self.wait()

        def get_z():
            p1 = n.get_center()
            p2 = g.get_center()
            p3 = q.get_center()
            vec = p2 - p3
            return p1 + vec
        
        gz = Line()
        gz.add_updater(lambda m:\
            m.put_start_and_end_on(
                g.get_center(),
                get_z()
            ))
        self.play(ShowCreation(gz))

        z = Dot()
        z.set_color(DARK_BLUE)
        z.plot_depth = 1
        z.add_updater(lambda m:\
            m.move_to(get_z()))
        
        z_label = Label(TexMobject('Z').scale(TEX_SIZE), z, direction=UP)
        z_label.plot_depth = 1

        self.play(ShowCreation(z))
        self.play(ShowCreation(z_label))
        self.wait()

        z_label.make_dynamic()

        nzg = Angle(n, z, g, radius=0.2)
        nzg.make_angle_dynamic()

        self.play(ShowCreation(nzg))
        self.wait()

        sub6 = CText('则ZF垂直于FG')
        sub6.scale(TEXT_SIZE)
        sub6.to_edge(RIGHT)

        self.play(FadeOut(sub5))
        self.play(Write(sub6))
        self.wait()

        zf = Line()
        zf.add_updater(lambda m:\
            m.put_start_and_end_on(
                z.get_center(),
                f.get_center()
            ))
        gfz = Angle(g, f, z, radius=0.2)

        self.play(ShowCreation(zf))
        self.play(ShowCreation(gfz))
        self.wait(5)

        self.play(y_val.set_value, 3)
        self.wait(5)
        
        m = Dot()
        m.set_color(DARK_BLUE)
        m.plot_depth = 1
        self.add_directrix_point_updater(q, m)

        m_label = Label(TexMobject('M').scale(TEX_SIZE), m, direction=LEFT)
        m_label.plot_depth = 1

        mq = Line()
        mq.add_updater(lambda l:\
            l.put_start_and_end_on(
                m.get_center(),
                q.get_center()
            ))
        
        self.play(
            ShowCreation(m),
            ShowCreation(m_label)
        )
        self.play(ShowCreation(mq))

        self.wait()
        m_label.make_dynamic()

        proof1 = CText('证明思路：')
        proof1.scale(TEXT_SIZE)

        proof2 = TexMobject('\\triangle NMQ \\cong \\triangle ZFG')
        proof2.scale(TEX_SIZE)

        proof = VGroup(proof1, proof2)
        proof.arrange(DOWN)
        proof1.align_to(proof2, LEFT)

        proof.to_edge(RIGHT)

        self.play(FadeOut(sub6))
        self.play(Write(proof))
        self.wait(15)

        self.play(y_val.set_value, 9)
        self.wait(5)

        self.play(y_val.set_value, 6)
        self.wait(15)

class Prob3Open(Scene):
    def construct(self):
        line1_1 = CText('抛物线')
        line1_1.set_fill(DARK_BLUE)

        line1_2 = CText('性质四')
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
            f, direction=RIGHT)
        f_label.plot_depth = 1
        directrix = self.get_directrix()

        self.play(
            *[ShowCreation(e) for e in\
                [f, f_label, graph, directrix]]
        )
        self.wait()

        y_val = ValueTracker(8)

        p = Dot()
        p.set_color(DARK_BLUE)
        p.plot_depth = 1
        p.add_updater(lambda m:\
            m.move_to(self.value_to_point(
                y_val.get_value())))
        
        p_label = Label(TexMobject('P').scale(TEX_SIZE), p, direction=UL)
        p_label.plot_depth = 1

        self.play(ShowCreation(p), ShowCreation(p_label))

        p_label.make_dynamic()

        q = Dot()
        q.set_color(DARK_BLUE)
        q.plot_depth = 1
        q.add_updater(lambda m:\
            m.move_to(self.get_opposite(p)))
        
        q_label = Label(TexMobject('Q').scale(TEX_SIZE), q, direction=RIGHT)
        q_label.plot_depth = 1

        pq = Line()
        pq.add_updater(lambda l:\
            l.put_start_and_end_on(
                p.get_center(),
                self.get_opposite(p)
            ))
        self.play(ShowCreation(pq))
        self.play(ShowCreation(q), ShowCreation(q_label))
        q_label.make_dynamic()
        self.wait()

        tangent_p = Line()
        self.add_tangent_extent_updater(tangent_p, p)

        tangent_q = Line()
        self.add_tangent_extent_updater(tangent_q, q)

        self.play(ShowCreation(tangent_p))
        self.play(ShowCreation(tangent_q))

        self.wait()

        vertical_line = Line()
        f_x = f.get_center()[0]
        vertical_line.put_start_and_end_on(
            f_x * RIGHT + FRAME_Y_RADIUS * UP,
            f_x * RIGHT + FRAME_Y_RADIUS * DOWN,
        )
        self.play(ShowCreation(vertical_line))

        p1 = Dot()
        p1.plot_depth = 1
        p1.set_color(DARK_BLUE)

        p1.add_updater(lambda m:\
            m.move_to(get_intersect(
                tangent_p, vertical_line, f
            )))
        
        self.play(ShowCreation(p1))

        p1_label = Label(
            TexMobject('P_1').scale(TEX_SIZE),
            p1, direction=UL
        )
        p1_label.make_dynamic()
        self.play(ShowCreation(p1_label))
        self.wait()

        q1 = Dot()
        q1.plot_depth = 1
        q1.set_color(DARK_BLUE)

        q1.add_updater(lambda m:\
            m.move_to(get_intersect(
                tangent_q, vertical_line, f
            )))
        
        self.play(ShowCreation(q1))

        q1_label = Label(
            TexMobject('Q_1').scale(TEX_SIZE),
            q1, direction=RIGHT
        )
        q1_label.make_dynamic()
        self.play(ShowCreation(q1_label))
        self.wait()

        proof = CText('证明思路：')
        sub_1 = TexMobject('M_1NFP_1')
        sub_2 = CText('与')
        sub_3 = TexMobject('M_2NFQ_1')
        sub_4 = CText('是菱形')

        for e in [proof, sub_2, sub_4]:
            e.scale(TEXT_SIZE)
        for e in [sub_1, sub_3]:
            e.scale(TEX_SIZE)
        
        idea = VGroup(sub_1, sub_2, sub_3, sub_4)
        idea.arrange(RIGHT, buff=SMALL_BUFF)

        prf = VGroup(proof, idea)
        prf.arrange(DOWN)
        idea.align_to(proof, LEFT)
        prf.move_to(RIGHT * 4 + 1 * DOWN)

        prob3 = TexMobject('P_1F=Q_1F')
        prob3.scale(TEX_SIZE)
        prob3.align_to(prf, LEFT)

        self.play(ShowCreation(prob3))

        p1f = Line()
        p1f.set_color(RED)
        p1f.add_updater(lambda m:\
            m.put_start_and_end_on(
                p1.get_center(),
                f.get_center()
            ))
        self.play(ShowCreation(p1f))

        q1f = Line()
        q1f.set_color(RED)
        q1f.add_updater(lambda m:\
            m.put_start_and_end_on(
                q1.get_center(),
                f.get_center()
            ))
        self.play(ShowCreation(q1f))
        self.wait()

        self.play(
            WiggleOutThenIn(p1f),
            WiggleOutThenIn(q1f))
        
        self.play(y_val.set_value, 2)
        self.wait(5)

        self.play(y_val.set_value, 5)
        self.wait(5)

        self.play(y_val.set_value, 9)
        self.wait(5)

        n = Dot()
        n.set_color(DARK_BLUE)
        n.plot_depth = 1
        n.add_updater(lambda m:\
            m.move_to(get_intersect(
                tangent_p,
                tangent_q, f
            )))
        
        self.play(ShowCreation(n))

        n_label = Label(
            TexMobject('N').scale(TEX_SIZE),
            n, direction=LEFT
        )
        n_label.make_dynamic()
        self.play(ShowCreation(n_label))
        self.wait()

        m1 = Dot()
        m1.plot_depth = 1
        m1.set_color(DARK_BLUE)
        self.add_directrix_point_updater(p, m1)

        self.play(ShowCreation(m1))

        m1_label = Label(
            TexMobject('M_1').scale(TEX_SIZE),
            m1, direction=LEFT
        )
        m1_label.make_dynamic()
        self.play(ShowCreation(m1_label))
        self.wait()

        pm1 = Line()
        pm1.add_updater(lambda m:\
            m.put_start_and_end_on(
                p.get_center(),
                m1.get_center()
            ))
        
        self.play(ShowCreation(pm1))

        m2 = Dot()
        m2.plot_depth = 1
        m2.set_color(DARK_BLUE)
        self.add_directrix_point_updater(q, m2)

        self.play(ShowCreation(m2))

        m2_label = Label(
            TexMobject('M_2').scale(TEX_SIZE),
            m2, direction=LEFT
        )
        m2_label.make_dynamic()
        self.play(ShowCreation(m2_label))
        self.wait()

        qm2 = Line()
        qm2.add_updater(lambda m:\
            m.put_start_and_end_on(
                q.get_center(),
                m2.get_center()
            ))
        
        self.play(ShowCreation(qm2))
        self.wait()

        nf = Line()
        nf.add_updater(lambda m:\
            m.put_start_and_end_on(
                n.get_center(),
                f.get_center()
            ))
        self.play(ShowCreation(nf))
        self.wait()

        m1p1 = Line()
        m1p1.add_updater(lambda m:\
            m.put_start_and_end_on(
                m1.get_center(),
                p1.get_center()
            ))
        self.play(ShowCreation(m1p1))
        self.wait()

        m2q1 = Line()
        m2q1.add_updater(lambda m:\
            m.put_start_and_end_on(
                m2.get_center(),
                q1.get_center()
            ))
        self.play(ShowCreation(m2q1))
        self.wait()

        m1nfp1 = Polygon(
            *[e.get_center() for e in\
                [m1, n, f, p1]]
        )
        m1nfp1.add_updater(lambda m:\
            m.set_points_as_corners(
                [e.get_center() for e in\
                    [m1, n, f, p1]]
            ))
        m1nfp1.stroke_width = 0
        m1nfp1.set_fill(ORANGE, opacity=0.5)
        self.play(ShowCreation(m1nfp1))
        self.wait()

        m2nfq1 = Polygon(
            *[e.get_center() for e in\
                [m2, n, f, q1]]
        )
        m2nfq1.add_updater(lambda m:\
            m.set_points_as_corners(
                [e.get_center() for e in\
                    [m2, n, f, q1]]
            ))
        m2nfq1.stroke_width = 0
        m2nfq1.set_fill(BLUE, opacity=0.5)
        self.play(ShowCreation(m2nfq1))
        self.wait()

        self.play(ShowCreation(prf))

        self.wait(10)

        self.play(y_val.set_value, 6)
        self.wait(5)

        self.play(y_val.set_value, 2)
        self.wait(5)

        self.play(y_val.set_value, 4)
        self.wait(5)

        self.play(y_val.set_value, 9)
        self.wait(15)

