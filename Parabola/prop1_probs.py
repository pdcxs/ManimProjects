from manimlib.imports import *
from ManimProjects.utils.Parabola import Parabola
from ManimProjects.utils.geometry import CText

class Prob1(Parabola):
    CONFIG = {
        'x_min' : -5
    }
    def construct(self):
        self.adjust_x_range()
        graph = self.get_graph(color=LIGHT_BROWN)
        directrix = self.get_directrix()
        focus = Dot().move_to(self.get_focus())
        focus.set_fill(DARK_BROWN)
        focus.plot_depth = 1
        focusLabel = TexMobject('F').scale(0.7)
        focusLabel.next_to(focus, RIGHT)

        self.play(*[ShowCreation(e) for\
            e in [graph, directrix, focus, focusLabel]])

        y_val = ValueTracker(8)

        p1 = Dot()
        p1.set_color(DARK_BLUE)
        p1.add_updater(lambda m:\
            m.move_to(self.coords_to_point(
                self.func(y_val.get_value()),
                y_val.get_value()
            )))
        p1.plot_depth = 1

        p1Label = TexMobject('P_1').scale(0.7)
        p1Label.add_updater(lambda m:\
            m.next_to(p1, RIGHT, buff=SMALL_BUFF))

        p2 = Dot()
        p2.set_color(DARK_BLUE)
        p2.add_updater(lambda m:\
            m.move_to(self.get_opposite(p1)))
        p2.plot_depth = 1

        p2Label = TexMobject('P_2').scale(0.7)
        p2Label.add_updater(lambda m:\
            m.next_to(p2, RIGHT, buff=SMALL_BUFF))

        focus_chord = Line()
        focus_chord.add_updater(lambda m:\
            m.put_start_and_end_on(
                p1.get_center(),
                self.get_opposite(p1)
            ))

        self.play(ShowCreation(p1), ShowCreation(p1Label))
        self.play(ShowCreation(focus_chord))
        self.play(ShowCreation(p2), ShowCreation(p2Label))

        fc_def = CText('焦点弦')
        fc_def.move_to(focus_chord.get_center())
        fc_def.shift(0.2 * RIGHT + 0.1 * DOWN)
        self.play(Write(fc_def))
        self.wait(2)
        self.play(FadeOut(fc_def))
        
        q_y = ValueTracker(2)
        q = Dot()
        q.set_fill(DARK_BLUE)
        q.plot_depth = 1

        q.add_updater(lambda m:\
            m.move_to(self.coords_to_point(
                self.func(q_y.get_value()),
                q_y.get_value()
            )))

        qLabel = TexMobject('Q').scale(0.7)
        qLabel.add_updater(lambda m:\
            m.next_to(q, LEFT, buff=SMALL_BUFF))
        
        k1 = Dot()
        k1.set_fill(BLUE_E)
        k1.plot_depth = 1
        k1.add_updater(lambda m:\
            m.move_to(self.chord_to_directrix(p1, q)))

        k1Label = TexMobject('K_1').scale(0.7)
        k1Label.add_updater(lambda m:\
            m.next_to(k1, LEFT, buff=SMALL_BUFF))

        k2 = Dot()
        k2.set_fill(BLUE_E)
        k2.plot_depth = 1
        k2.add_updater(lambda m:\
            m.move_to(self.chord_to_directrix(p2, q)))

        k2Label = TexMobject('K_2').scale(0.7)
        k2Label.add_updater(lambda m:\
            m.next_to(k2, LEFT, buff=SMALL_BUFF))
        
        l1 = Line()
        l1.add_updater(lambda m:\
            m.put_start_and_end_on(
                self.right(p1, q),
                self.chord_to_directrix(p1, q)
            ))

        l2 = Line()
        l2.add_updater(lambda m:\
            m.put_start_and_end_on(
                self.right(p2, q),
                self.chord_to_directrix(p2, q)
            ))
        
        self.play(ShowCreation(q), ShowCreation(qLabel))
        self.play(ShowCreation(l1), ShowCreation(l2))
        self.play(*[ShowCreation(e) for e in [k1, k2, k1Label, k2Label]])

        k1f = Line()
        k1f.add_updater(lambda m:\
            m.put_start_and_end_on(
                k1.get_center(), focus.get_center()
            ))

        k2f = Line()
        k2f.add_updater(lambda m:\
            m.put_start_and_end_on(
                k2.get_center(), focus.get_center()
            ))

        self.play(ShowCreation(k1f), ShowCreation(k2f))

        self.wait(1)
        self.play(ApplyMethod(y_val.set_value,
            5))

        summary = TexMobject('K_1F \\perp K_2F').scale(2)
        summary.to_edge(RIGHT)

        self.wait(1)
        self.play(Write(summary))
        self.wait(5)

        qf = Line()
        qf.add_updater(lambda m:\
            m.put_start_and_end_on(q.get_center(),
                focus.get_center()))
        self.play(ShowCreation(qf))

        self.wait(1)
        self.play(ApplyMethod(q_y.set_value,
            -1))

        self.wait(1)
        self.play(ApplyMethod(y_val.set_value,
            0.5))

        self.wait(1)
        self.play(ApplyMethod(y_val.set_value,
            3),
            ApplyMethod(q_y.set_value, 0.5))
        self.wait(10)

class Prob2(Parabola):
    CONFIG = {
        'focus': 2,
        'x_min': -4
    }
    def construct(self):
        self.adjust_x_range()
        graph = self.get_graph(color=LIGHT_BROWN)
        directrix = self.get_directrix()
        focus = Dot().move_to(self.get_focus())
        focus.set_fill(DARK_BROWN)
        focus.plot_depth = 1
        focusLabel = TexMobject('F').scale(0.7)
        focusLabel.next_to(focus, RIGHT)

        self.play(*[ShowCreation(e) for\
            e in [graph, directrix, focus, focusLabel]])

        q1_y = ValueTracker(9)
        q1 = Dot()
        q1.set_fill(DARK_BLUE)
        q1.plot_depth = 1

        q1.add_updater(lambda m:\
            m.move_to(self.coords_to_point(
                self.func(q1_y.get_value()),
                q1_y.get_value()
            )))

        q1_label = TexMobject('Q_1').scale(0.5)
        q1_label.add_updater(lambda m:\
            m.next_to(q1, RIGHT, buff=SMALL_BUFF))
        
        self.play(ShowCreation(q1), ShowCreation(q1_label))

        q2 = Dot()
        q2.set_fill(DARK_BLUE)
        q2.plot_depth = 1

        q2.add_updater(lambda m:\
            m.move_to(self.get_opposite(q1)))

        q2_label = TexMobject('Q_2').scale(0.5)
        q2_label.add_updater(lambda m:\
            m.next_to(q2, RIGHT, buff=SMALL_BUFF))

        q1q2 = Line()
        q1q2.add_updater(lambda m:\
            m.put_start_and_end_on(
                q1.get_center(),
                self.get_opposite(q1)
            ))

        self.play(*[ShowCreation(e) for e in\
            [q2, q2_label, q1q2]])

        p1_y = ValueTracker(2)
        p1 = Dot()
        p1.set_fill(DARK_BLUE)
        p1.plot_depth = 1

        p1.add_updater(lambda m:\
            m.move_to(self.coords_to_point(
                self.func(p1_y.get_value()),
                p1_y.get_value()
            )))

        p1_label = TexMobject('P_1').scale(0.5)
        p1_label.add_updater(lambda m:\
            m.next_to(p1, RIGHT, buff=SMALL_BUFF))
        
        self.play(ShowCreation(p1), ShowCreation(p1_label))

        p2 = Dot()
        p2.set_fill(DARK_BLUE)
        p2.plot_depth = 1

        p2.add_updater(lambda m:\
            m.move_to(self.get_opposite(p1)))

        p2_label = TexMobject('P_2').scale(0.5)
        p2_label.add_updater(lambda m:\
            m.next_to(p2, RIGHT, buff=SMALL_BUFF))

        p1p2 = Line()
        p1p2.add_updater(lambda m:\
            m.put_start_and_end_on(
                p1.get_center(),
                self.get_opposite(p1)
            ))

        self.play(*[ShowCreation(e) for e in\
            [p2, p2_label, p1p2]])

        k1 = Dot()
        k1.set_fill(DARK_BROWN)
        k1.plot_depth = 1
        k1.add_updater(lambda m:\
            m.move_to(self.chord_to_directrix(p1, q1)))

        k1_label = TexMobject('K_1').scale(0.5)
        k1_label.add_updater(lambda m:\
            m.next_to(k1, LEFT, buff=SMALL_BUFF))

        p1q1 = Line()
        p1q1.add_updater(lambda m:\
            m.put_start_and_end_on(
                self.right(p1, q1),
                self.chord_to_directrix(p1, q1)
            ))
        p2q2 = Line()
        p2q2.add_updater(lambda m:\
            m.put_start_and_end_on(
                self.right(p2, q2),
                self.chord_to_directrix(p2, q2)
            ))

        self.play(*[ShowCreation(e) for e in \
            [k1, k1_label, p1q1, p2q2]])

        k2 = Dot()
        k2.set_fill(DARK_BROWN)
        k2.plot_depth = 1
        k2.add_updater(lambda m:\
            m.move_to(self.chord_to_directrix(p2, q1)))

        k2_label = TexMobject('K_2').scale(0.5)
        k2_label.add_updater(lambda m:\
            m.next_to(k2, LEFT, buff=SMALL_BUFF))

        p2q1 = Line()
        p2q1.add_updater(lambda m:\
            m.put_start_and_end_on(
                self.right(p2, q1),
                self.chord_to_directrix(p2, q1)
            ))
        p1q2 = Line()
        p1q2.add_updater(lambda m:\
            m.put_start_and_end_on(
                self.right(p1, q2),
                self.chord_to_directrix(p1, q2)
            ))

        self.play(*[ShowCreation(e) for e in \
            [k2, k2_label, p2q1, p1q2]])

        explain = CText('这些交点在准线上').scale(0.3)
        explain.to_edge(RIGHT)

        self.wait(2)
        self.play(Write(explain))
        self.wait(5)

        self.play(ApplyMethod(q1_y.set_value, 0.5),
            ApplyMethod(p1_y.set_value, -3))

        self.wait(3)
        self.play(ApplyMethod(q1_y.set_value, 3),
            ApplyMethod(p1_y.set_value, -9))
        self.wait(10)


class Prob3(Parabola):
    CONFIG = {
        'focus': 2,
        'x_min': -4
    }
    def construct(self):
        self.adjust_x_range()
        graph = self.get_graph(color=LIGHT_BROWN)
        directrix = self.get_directrix()
        focus = Dot().move_to(self.get_focus())
        focus.set_fill(DARK_BROWN)
        focus.plot_depth = 1
        focusLabel = TexMobject('F').scale(0.7)
        focusLabel.next_to(focus, RIGHT)

        self.play(*[ShowCreation(e) for\
            e in [graph, directrix, focus, focusLabel]])

        q1_y = ValueTracker(9)
        q1 = Dot()
        q1.set_fill(DARK_BLUE)
        q1.plot_depth = 1

        q1.add_updater(lambda m:\
            m.move_to(self.coords_to_point(
                self.func(q1_y.get_value()),
                q1_y.get_value()
            )))

        q1_label = TexMobject('Q_1').scale(0.5)
        q1_label.add_updater(lambda m:\
            m.next_to(q1, RIGHT, buff=SMALL_BUFF))
        
        self.play(ShowCreation(q1), ShowCreation(q1_label))

        q2 = Dot()
        q2.set_fill(DARK_BLUE)
        q2.plot_depth = 1

        q2.add_updater(lambda m:\
            m.move_to(self.get_opposite(q1)))

        q2_label = TexMobject('Q_2').scale(0.5)
        q2_label.add_updater(lambda m:\
            m.next_to(q2, RIGHT, buff=SMALL_BUFF))

        q1q2 = Line()
        q1q2.add_updater(lambda m:\
            m.put_start_and_end_on(
                q1.get_center(),
                self.get_opposite(q1)
            ))

        self.play(*[ShowCreation(e) for e in\
            [q2, q2_label, q1q2]])

        p1_y = ValueTracker(2)
        p1 = Dot()
        p1.set_fill(DARK_BLUE)
        p1.plot_depth = 1

        p1.add_updater(lambda m:\
            m.move_to(self.coords_to_point(
                self.func(p1_y.get_value()),
                p1_y.get_value()
            )))

        p1_label = TexMobject('P_1').scale(0.5)
        p1_label.add_updater(lambda m:\
            m.next_to(p1, RIGHT, buff=SMALL_BUFF))
        
        self.play(ShowCreation(p1), ShowCreation(p1_label))

        p2 = Dot()
        p2.set_fill(DARK_BLUE)
        p2.plot_depth = 1

        p2.add_updater(lambda m:\
            m.move_to(self.get_opposite(p1)))

        p2_label = TexMobject('P_2').scale(0.5)
        p2_label.add_updater(lambda m:\
            m.next_to(p2, RIGHT, buff=SMALL_BUFF))

        p1p2 = Line()
        p1p2.add_updater(lambda m:\
            m.put_start_and_end_on(
                p1.get_center(),
                self.get_opposite(p1)
            ))

        self.play(*[ShowCreation(e) for e in\
            [p2, p2_label, p1p2]])

        k1 = Dot()
        k1.set_fill(DARK_BROWN)
        k1.plot_depth = 1
        k1.add_updater(lambda m:\
            m.move_to(self.chord_to_directrix(p1, q1)))

        k1_label = TexMobject('K_1').scale(0.5)
        k1_label.add_updater(lambda m:\
            m.next_to(k1, LEFT, buff=SMALL_BUFF))

        p1q1 = Line()
        p1q1.add_updater(lambda m:\
            m.put_start_and_end_on(
                self.right(p1, q1),
                self.chord_to_directrix(p1, q1)
            ))
        p2q2 = Line()
        p2q2.add_updater(lambda m:\
            m.put_start_and_end_on(
                self.right(p2, q2),
                self.chord_to_directrix(p2, q2)
            ))

        self.play(*[ShowCreation(e) for e in \
            [k1, k1_label, p1q1, p2q2]])

        k2 = Dot()
        k2.set_fill(DARK_BROWN)
        k2.plot_depth = 1
        k2.add_updater(lambda m:\
            m.move_to(self.chord_to_directrix(p2, q1)))

        k2_label = TexMobject('K_2').scale(0.5)
        k2_label.add_updater(lambda m:\
            m.next_to(k2, LEFT, buff=SMALL_BUFF))

        p2q1 = Line()
        p2q1.add_updater(lambda m:\
            m.put_start_and_end_on(
                self.right(p2, q1),
                self.chord_to_directrix(p2, q1)
            ))
        p1q2 = Line()
        p1q2.add_updater(lambda m:\
            m.put_start_and_end_on(
                self.right(p1, q2),
                self.chord_to_directrix(p1, q2)
            ))

        self.play(*[ShowCreation(e) for e in \
            [k2, k2_label, p2q1, p1q2]])

        k1f = Line()
        k1f.add_updater(lambda m:\
            m.put_start_and_end_on(
                k1.get_center(),
                focus.get_center()
            ))

        k2f = Line()
        k2f.add_updater(lambda m:\
            m.put_start_and_end_on(
                k2.get_center(),
                focus.get_center()
            ))

        explain = TexMobject('K_1F \\perp K_2F')
        explain.to_edge(RIGHT)

        self.wait(2)
        self.play(ShowCreation(k1f), ShowCreation(k2f))
        self.wait(3)
        self.play(Write(explain))
        self.wait(5)

        self.play(ApplyMethod(q1_y.set_value, 0.5),
            ApplyMethod(p1_y.set_value, -3))

        self.wait(3)
        self.play(ApplyMethod(q1_y.set_value, 3),
            ApplyMethod(p1_y.set_value, -9))
        self.wait(10)

class Prob4(Parabola):
    CONFIG = {
        'focus': 3,
        'x_min': -10
    }
    def construct(self):
        self.adjust_x_range()
        graph = self.get_graph(color=LIGHT_BROWN)
        directrix = self.get_directrix()
        focus = Dot().move_to(self.get_focus())
        focus.set_fill(DARK_BROWN)
        focus.plot_depth = 1
        focusLabel = TexMobject('F').scale(0.5)
        focusLabel.next_to(focus, RIGHT)

        self.play(*[ShowCreation(e) for\
            e in [graph, directrix, focus, focusLabel]])

        a = Dot()
        a.set_fill(DARK_BROWN)
        a.move_to(self.coords_to_point(0, 0))
        a.plot_depth = 1
        a_label = TexMobject('A').scale(0.5)
        a_label.next_to(a, RIGHT)

        self.play(*[ShowCreation(e) for e in [a, a_label]])

        y_val = ValueTracker(8)

        m = Dot()
        m.set_fill(DARK_BLUE)
        m.plot_depth = 1
        m.add_updater(lambda m:\
            m.move_to(self.coords_to_point(
                -self.focus, y_val.get_value()
            )))
        m_label = TexMobject('M').scale(0.5)
        m_label.add_updater(lambda l:\
            l.next_to(m, LEFT))

        p = Dot()
        p.set_fill(DARK_BLUE)
        p.plot_depth = 1
        p.add_updater(lambda m:\
            m.move_to(self.coords_to_point(
                self.func(y_val.get_value()),
                y_val.get_value()
            )))
        p_label = TexMobject('P').scale(0.5)
        p_label.add_updater(lambda m:\
            m.next_to(p, RIGHT))
        self.play(*[ShowCreation(e) for e in\
            [m, m_label, p, p_label]])

        k = Dot()
        k.set_fill(DARK_BLUE)
        k.plot_depth = 1
        k.add_updater(lambda m:\
            m.move_to(self.chord_to_directrix(
                p, a
            )))
        k_label = TexMobject('K').scale(0.5)
        k_label.add_updater(lambda m:\
            m.next_to(k, LEFT))
        
        pk = Line()
        pk.add_updater(lambda l:\
            l.put_start_and_end_on(
                p.get_center(),
                self.chord_to_directrix(p, a)
            ))
        mp = Line()
        mp.add_updater(lambda l:\
            l.put_start_and_end_on(
                m.get_center(),
                p.get_center()
            ))
        self.play(*[ShowCreation(e) for e in\
            [k, k_label, pk, mp]])

        kf = Line()
        kf.add_updater(lambda l:\
            l.put_start_and_end_on(
                k.get_center(),
                focus.get_center()
            ))
        mf = Line()
        mf.add_updater(lambda l:\
            l.put_start_and_end_on(
                m.get_center(),
                focus.get_center()
            ))

        self.play(ShowCreation(kf), ShowCreation(mf))

        form = TexMobject('KF \\perp MF')
        form.scale(0.7)
        form.to_edge(RIGHT)
        self.play(Write(form))

        af = DashedLine(a.get_center(), focus.get_center())
        pf = DashedLine()

        def get_pf_extent():
            vec = focus.get_center() - p.get_center()
            vec = normalize(vec)
            return focus.get_center() + 2 * vec

        pf.add_updater(lambda m:\
            m.put_start_and_end_on(
                p.get_center(),
                get_pf_extent()
            ))
        self.play(ShowCreation(af), ShowCreation(pf))

        self.wait(3)
        self.play(ApplyMethod(y_val.set_value, 2))
        self.wait(3)
        self.play(ApplyMethod(y_val.set_value, -2))
        self.wait(3)
        self.play(ApplyMethod(y_val.set_value, -8))
        self.wait(10)

class Prob5(Parabola):
    CONFIG = {
        'focus': 3,
        'x_min': -10
    }
    def construct(self):
        self.adjust_x_range()
        graph = self.get_graph(color=LIGHT_BROWN)
        directrix = self.get_directrix()
        focus = Dot().move_to(self.get_focus())
        focus.set_fill(DARK_BROWN)
        focus.plot_depth = 1
        focusLabel = TexMobject('F').scale(0.5)
        focusLabel.next_to(focus, RIGHT + UP)

        self.play(*[ShowCreation(e) for\
            e in [graph, directrix, focus, focusLabel]])

        h_line = self.get_horizontal()
        x = Dot()
        x.set_fill(DARK_BROWN)
        x.plot_depth = 1
        x.move_to(self.coords_to_point(-self.focus, 0))
        x_label = TexMobject('X').scale(0.5)
        x_label.next_to(x, LEFT + UP)

        self.play(ShowCreation(h_line))
        self.play(ShowCreation(x), ShowCreation(x_label))

        y_val = ValueTracker(8)
        p = Dot()
        p.set_fill(DARK_BLUE)
        p.plot_depth = 1
        p.add_updater(lambda m:\
            m.move_to(self.coords_to_point(
                self.func(y_val.get_value()),
                y_val.get_value()
            )))
        
        q = Dot()
        q.set_fill(DARK_BLUE)
        q.plot_depth = 1
        q.add_updater(lambda m:\
            m.move_to(self.coords_to_point(
                self.func(-y_val.get_value()),
                -y_val.get_value()
            )))

        t = Dot()
        t.set_fill(DARK_BLUE)
        t.plot_depth = 1
        t.add_updater(lambda m:\
            m.move_to(self.coords_to_point(
                self.func(y_val.get_value()), 0
            )))

        p_label = TexMobject('P').scale(0.5)
        p_label.add_updater(lambda m:\
            m.next_to(p, RIGHT))
        q_label = TexMobject('Q').scale(0.5)
        q_label.add_updater(lambda m:\
            m.next_to(q, RIGHT))
        t_label = TexMobject('T').scale(0.5)
        t_label.add_updater(lambda m:\
            m.next_to(t, RIGHT + UP))

        pq = Line()
        pq.add_updater(lambda m:\
            m.put_start_and_end_on(
                p.get_center(),
                self.coords_to_point(
                    self.func(-y_val.get_value()),
                    -y_val.get_value()
            )))
        pt = Line()
        pt.add_updater(lambda m:\
            m.put_start_and_end_on(
                p.get_center(),
                self.coords_to_point(
                    self.func(y_val.get_value()), 0
                )))
        self.play(ShowCreation(p), ShowCreation(p_label))
        self.play(ShowCreation(pt))
        self.play(ShowCreation(t), ShowCreation(t_label))
        label1 = CText('纵标线').scale(0.3)\
                .next_to(pt, RIGHT)
        self.play(ShowCreation(label1))
        self.wait()
        self.play(FadeOut(label1))
        self.play(ShowCreation(pq))
        self.remove(pt)
        self.play(ShowCreation(q), ShowCreation(q_label))
        label2 = CText('双纵标线').scale(0.3)\
                .next_to(t, RIGHT+DOWN)
        self.play(ShowCreation(label2))
        self.wait()
        self.play(FadeOut(label2))
        self.wait()
        
        inter = Dot()
        inter.set_fill(DARK_BLUE)
        inter.plot_depth = 1
        inter.add_updater(lambda m:\
            m.move_to(
                self.coords_to_point(
                    4*(self.focus**3)/(y_val.get_value()**2),
                    4*self.focus**2/y_val.get_value()
                ) if y_val.get_value() != 0 else
                    self.coords_to_point(0, 0)
            ))

        inter_label = TexMobject("P'").scale(0.5)
        inter_label.add_updater(lambda m:\
            m.next_to(inter, LEFT + UP, buff=SMALL_BUFF))

        px = Line()
        px.add_updater(lambda m:\
            m.put_start_and_end_on(
                self.right(p, inter),
                x.get_center()
            ))
        
        self.play(ShowCreation(px))
        self.play(ShowCreation(inter),
            ShowCreation(inter_label))
        self.wait()

        form = CText("P'Q经过焦点").shift(UP)
        form.scale(0.5)
        form.to_edge(RIGHT)
        self.play(Write(form))
        
        interq = Line()
        interq.add_updater(lambda m:\
            m.put_start_and_end_on(
                inter.get_center(),
                q.get_center()
            ))
        self.play(ShowCreation(interq))

        self.wait(2)
        self.play(ApplyMethod(y_val.set_value, 4))

        self.wait(2)
        self.play(ApplyMethod(y_val.set_value, -4))

        self.wait(2)
        self.play(ApplyMethod(y_val.set_value, -9))

        self.wait(2)
        self.play(ApplyMethod(y_val.set_value, 9))

        self.wait(10)