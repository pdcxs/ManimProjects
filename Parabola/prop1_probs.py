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
