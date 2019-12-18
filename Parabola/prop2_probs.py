from manimlib.imports import *
from ManimProjects.utils.Parabola import Parabola
from ManimProjects.utils.geometry import CText

class Prob1Open(Scene):
    def construct(self):
        line1_1 = CText('抛物线')
        line1_1.set_fill(DARK_BLUE)

        line1_2 = CText('性质二')
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
        focusLabel.next_to(focus, DOWN, buff=SMALL_BUFF)

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

        p1_label = TexMobject('P_1').scale(0.5)
        p1_label.plot_depth = 1
        p1_label.add_updater(lambda m:\
            m.next_to(p1, RIGHT, buff=SMALL_BUFF))

        p2 = Dot()
        p2.plot_depth = 1
        p2.set_color(DARK_BLUE)
        p2.add_updater(lambda m:\
            m.move_to(self.coords_to_point(
                self.func(-y_val.get_value()),
                -y_val.get_value()
            )))

        p2_label = TexMobject('P_2').scale(0.5)
        p2_label.plot_depth = 1
        p2_label.add_updater(lambda m:\
            m.next_to(p2, RIGHT, buff=SMALL_BUFF))

        a = Dot()
        a.set_color(DARK_BLUE)
        a.plot_depth = 1
        a.move_to(self.coords_to_point(0, 0))

        a_label = TexMobject('A').scale(0.5)
        a_label.next_to(a, DL, buff=SMALL_BUFF)

        h_line = Line(LEFT*6, RIGHT*2)

        self.play(*[ShowCreation(e) for e in\
            [h_line, a, a_label]])
        self.wait()

        sub1 = CText('取任意双纵标线P1P2')\
            .scale(0.3).to_edge(RIGHT)
        self.play(Write(sub1))
        self.wait()
        self.play(*[ShowCreation(e) for e in\
            [p1, p1_label, p2, p2_label]])

        p1p2 = Line()
        p1p2.add_updater(lambda l:\
            l.put_start_and_end_on(
                p1.get_center(), p2.get_center()
            ))
        self.play(ShowCreation(p1p2))
        self.wait()

        n = Dot()
        n.set_color(DARK_BLUE)
        n.plot_depth = 1
        n.add_updater(lambda m:\
            m.move_to(self.coords_to_point(
                self.func(y_val.get_value()), 0
            )))
        n_label = TexMobject('N').scale(0.5)
        n_label.plot_depth = 1
        n_label.add_updater(lambda m:\
            m.next_to(n, DR, buff=SMALL_BUFF))
        self.play(
            ShowCreation(n),
            ShowCreation(n_label)
        )
        self.wait()

        sub2 = CText('做P1、P2、A的外接圆')\
            .scale(0.3).to_edge(RIGHT)
        self.play(FadeOut(sub1))
        self.play(Write(sub2))

        def set_circle(c):
            pos1 = a.get_center()
            pos2 = p1.get_center()
            pos3 = p2.get_center()

            p = self.focus
            y = y_val.get_value()
            o = self.coords_to_point(
                (16*p*p+y*y)/(8*p), 0
            )

            r = o[0] - pos1[0]
            c.move_to(o)
            c.stretch_to_fit_height(2 * r)
            c.stretch_to_fit_width(2 * r)
            
        circle = Circle()
        circle.set_color(MAROON_E)
        circle.add_updater(lambda m: set_circle(m))
        self.play(ShowCreation(circle))

        self.wait()

        sub3 = CText('交轴于点Q')\
            .scale(0.3).to_edge(RIGHT)
        self.play(FadeOut(sub2))
        self.play(Write(sub3))

        q = Dot()
        q.set_fill(DARK_BLUE)
        q.plot_depth = 1
        q.add_updater(lambda m:\
            m.move_to(n.get_center() +\
            4 * (focus.get_center() - a.get_center())))
        
        q_label = TexMobject('Q').scale(0.5)
        q_label.plot_depth = 1
        q_label.add_updater(lambda m:\
            m.next_to(q, DR, buff=SMALL_BUFF))
        
        self.play(
            ShowCreation(q),
            ShowCreation(q_label)
        )
        self.wait()

        corollary = VGroup()

        head = CText('推论：').scale(0.25)
        head.set_fill(DARK_BLUE)
        
        crlly = TexMobject('NQ=4AF').scale(0.5)

        head_line = VGroup(head, crlly)
        head_line.arrange(RIGHT)

        proof = VGroup()
        proof_head = CText('证明：').scale(0.25)
        proof_head.set_fill(DARK_BLUE)
        proof.add(proof_head)

        proof_details = VGroup()
        prf1 = CText('在直角三角形AQP1中')\
            .scale(0.25)
        prf2 = TexMobject('P_1N^2=AN\\cdot NQ')\
            .scale(0.5)
        prf3 = VGroup()
        prf3_1 = CText('又').scale(0.25)
        prf3_2 = TexMobject(
            '\\because P_1N^2=4AF\\cdot AN')\
            .scale(0.5)
        prf3.add(prf3_1, prf3_2)
        prf3.arrange(RIGHT, buff=SMALL_BUFF)

        prf4 = TexMobject(
            '\\therefore AN\\cdot NQ=4AF\\cdot AN'
        ).scale(0.5)

        prf5 = TexMobject(
            '\\therefore NQ=4AF'
        ).scale(0.5)

        proof_details.add(prf1, prf2, prf3,
            prf4, prf5)
        proof_details.arrange(DOWN)
        proof.add(proof_details)
        proof.arrange(RIGHT)
        proof_details.align_to(proof_head, UP)
        for e in [prf2, prf3, prf4, prf5]:
            e.align_to(prf1, LEFT)

        corollary.add(head_line)
        corollary.add(proof)
        corollary.arrange(DOWN)
        head_line.align_to(proof, LEFT)
        corollary.to_edge(RIGHT)

        self.play(FadeOut(sub3))
        self.play(ShowCreation(head_line))
        self.play(Write(proof_head))
        self.wait(5)

        self.play(Write(prf1))

        ap1 = DashedLine()
        ap1.add_updater(lambda l:\
            l.put_start_and_end_on(
                a.get_center(), p1.get_center()
            ))

        qp1 = DashedLine()
        qp1.add_updater(lambda l:\
            l.put_start_and_end_on(
                q.get_center(), p1.get_center()
            ))
        self.play(
            ShowCreation(ap1),
            ShowCreation(qp1)
        )
        self.play(ShowCreationThenDestruction(
            Polygon(
                a.get_center(),
                q.get_center(),
                p1.get_center()
            ).set_fill(ORANGE, opacity=1)
        ))
        self.wait(5)
        self.play(Write(prf2))

        self.wait(5)
        self.play(Write(prf3))

        self.wait(3)
        self.play(Write(prf4))
        self.wait(3)
        self.play(Write(prf5))
        self.wait(5)

        self.play(y_val.set_value, 4)
        self.wait(3)
        self.play(y_val.set_value, 2)
        self.wait(10)

class Prob2Open(Scene):
    def construct(self):
        line1_1 = CText('抛物线')
        line1_1.set_fill(DARK_BLUE)

        line1_2 = CText('性质二')
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
        'focus' : 3
    }
    def construct(self):
        self.adjust_x_range()
        graph = self.get_graph(color=LIGHT_BROWN)
        focus = Dot().move_to(self.get_focus())
        focus.set_fill(DARK_BROWN)
        focus.plot_depth = 1
        focusLabel = TexMobject('F').scale(0.5)
        focusLabel.next_to(focus, DOWN, buff=SMALL_BUFF)
        focusLabel.plot_depth = 1

        self.play(*[ShowCreation(e) for\
            e in [graph, focus, focusLabel]])

        h_line = Line(self.coords_to_point(0, 0), ORIGIN)
        h_line.plot_depth = -1
        self.play(ShowCreation(h_line))

        a = Dot()
        a.move_to(self.coords_to_point(0, 0))
        a.plot_depth = 1
        a.set_fill(DARK_BROWN)
        a_label = TexMobject('A').scale(0.5)
        a_label.next_to(a, DL, buff=SMALL_BUFF)
        a_label.plot_depth = 1

        self.play(
            ShowCreation(a),
            Write(a_label)
        )
        self.wait()

        y_val = ValueTracker(6.5)

        p1 = Dot()
        p1.set_fill(DARK_BLUE)
        p1.plot_depth = 1
        p1.add_updater(lambda m:\
            m.move_to(self.coords_to_point(
                self.func(y_val.get_value()),
                y_val.get_value()
            )))
        p1_label = TexMobject('P_1').scale(0.5)
        p1_label.plot_depth = 1
        p1_label.add_updater(lambda m:\
            m.next_to(p1, RIGHT, buff=SMALL_BUFF))

        p2 = Dot()
        p2.set_fill(DARK_BLUE)
        p2.plot_depth = 1
        p2.add_updater(lambda m:\
            m.move_to(self.coords_to_point(
                self.func(-y_val.get_value()),
                -y_val.get_value()
            )))
        p2_label = TexMobject('P_2').scale(0.5)
        p2_label.plot_depth = 1
        p2_label.add_updater(lambda m:\
            m.next_to(p2, RIGHT, buff=SMALL_BUFF))

        p1p2 = Line()
        p1p2.add_updater(lambda m:\
            m.put_start_and_end_on(
                self.coords_to_point(
                    self.func(y_val.get_value()),
                    y_val.get_value()
                ),
                self.coords_to_point(
                    self.func(-y_val.get_value()),
                    -y_val.get_value()
            )))
        self.play(
            ShowCreation(p1),
            Write(p1_label)
        )
        self.play(ShowCreation(p1p2))
        self.play(
            ShowCreation(p2),
            Write(p2_label)
        )
        self.wait()

        n1 = Dot()
        n1.set_fill(DARK_BLUE)
        n1.plot_depth = 1
        n1.add_updater(lambda m:\
            m.move_to(p1.get_center()[0] * RIGHT))
        n1_label = TexMobject('N').scale(0.5)
        n1_label.add_updater(lambda m:\
            m.next_to(n1, DR, buff=SMALL_BUFF))
        self.play(
            ShowCreation(n1),
            Write(n1_label)
        )
        self.wait()

        q_y = ValueTracker(5)

        q = Dot()
        q.set_fill(DARK_BLUE)
        q.plot_depth = 1
        q.add_updater(lambda m:\
            m.move_to(self.coords_to_point(
                self.func(q_y.get_value()),
                q_y.get_value()
            )))
        q_label = TexMobject('Q').scale(0.5)
        q_label.plot_depth = 1
        q_label.add_updater(lambda m:\
            m.next_to(q, LEFT, buff=SMALL_BUFF))
        self.play(
            ShowCreation(q),
            Write(q_label)
        )

        self.wait()

        def get_l():
            qy = q_y.get_value()
            qx = self.func(qy)
            py = y_val.get_value()
            px = self.func(py)

            l = qy / qx * px
            return self.coords_to_point(px, l)

        l = Dot()
        l.set_fill(DARK_BLUE)
        l.plot_depth = 1
        l.add_updater(lambda m:\
            m.move_to(get_l()))
        l_label = TexMobject('L').scale(0.5)
        l_label.add_updater(lambda m:\
            m.next_to(l, RIGHT, buff=SMALL_BUFF))

        al = Line()
        al.add_updater(lambda m:\
            m.put_start_and_end_on(
                a.get_center(),
                get_l() if\
                    q_y.get_value() < y_val.get_value()\
                    else q.get_center()
            ))
        p1l = Line()
        p1l.add_updater(lambda m:\
            m.put_start_and_end_on(
                p1.get_center(),
                get_l()
            ))
        self.play(
            ShowCreation(al),
            ShowCreation(p1l))
        self.play(
            ShowCreation(l),
            Write(l_label)
        )

        self.wait()

        def get_l2():
            qy = q.get_center()[1]
            px = p1.get_center()[0]

            return px * RIGHT + qy * UP
        
        l2 = Dot()
        l2.set_fill(DARK_BLUE)
        l2.plot_depth = 1
        l2.add_updater(lambda m:\
            m.move_to(get_l2()))
        l2_label = TexMobject("L'").scale(0.5)
        l2_label.add_updater(lambda m:\
            m.next_to(l2, RIGHT, buff=SMALL_BUFF))
        
        ql2 = Line()
        ql2.add_updater(lambda m:\
            m.put_start_and_end_on(
                q.get_center(),
                get_l2()
            ))
        p1l2 = Line()
        p1l2.add_updater(lambda m:\
            m.put_start_and_end_on(
                p1.get_center(),
                get_l2()
            ))
        self.play(
            ShowCreation(ql2),
            ShowCreation(p1l2))
        self.play(
            ShowCreation(l2),
            Write(l2_label)
        )

        corollary = VGroup()

        head = CText('推论：').scale(0.25)
        head.set_fill(DARK_BLUE)
        
        crlly = TexMobject("P_1N^2=LN\\cdot L'N").scale(0.5)

        head_line = VGroup(head, crlly)
        head_line.arrange(RIGHT)

        proof = VGroup()
        proof_head = CText('证明：').scale(0.25)
        proof_head.set_fill(DARK_BLUE)
        proof.add(proof_head)

        proof_details = VGroup()
        prf1 = TexMobject("\\frac{LN}{AN}=\\frac{QN'}{AN'}")\
            .scale(0.5)

        prf2 = VGroup()
        prf2_1 = CText('又').scale(0.25)
        prf2_2 = TexMobject(
            "\\because L'N=QN'")\
            .scale(0.5)
        prf2.add(prf2_1, prf2_2)
        prf2.arrange(RIGHT, buff=SMALL_BUFF)

        prf3 = TexMobject(
            "\\therefore LN\\cdot L'N=\\frac{QN'\
                \\cdot AN}{AN'}\\cdot QN' =\
                \\frac{QN'^2\\cdot AN}{AN'}"
        ).scale(0.5)

        prf4 = VGroup()
        prf4_1 = CText('又').scale(0.25)
        prf4_2 = TexMobject(
            "\\because QN'^2=4AN'\\cdot AF")\
            .scale(0.5)
        prf4.add(prf4_1, prf4_2)
        prf4.arrange(RIGHT, buff=SMALL_BUFF)

        prf5 = TexMobject(
            "\\therefore LN\\cdot L'N=\\frac{4AN'\\cdot AF\
                \\cdot AN}{AN'} = 4AN\\cdot AF = P_1N^2"
        ).scale(0.5)

        proof_details.add(prf1, prf2, prf3,
            prf4, prf5)
        proof_details.arrange(DOWN)
        proof.add(proof_details)
        proof.arrange(RIGHT)
        proof_details.align_to(proof_head, UP)

        corollary.add(head_line)
        corollary.add(proof)
        corollary.arrange(DOWN)

        head_line.align_to(proof, LEFT)
        prf1.align_to(crlly, LEFT)
        for e in [prf2, prf3, prf4, prf5]:
            e.align_to(prf1, LEFT)

        corollary.to_edge(RIGHT)

        self.play(Write(head_line))
        self.wait()

        def get_n2():
            qx = q.get_center()[0]
            return qx * RIGHT

        n2 = Dot()
        n2.plot_depth = 1
        n2.set_fill(DARK_BLUE)
        n2.add_updater(lambda m:\
            m.move_to(get_n2()))

        n2_label = TexMobject("N'").scale(0.5)
        n2_label.add_updater(lambda m:\
            m.next_to(n2, DOWN, buff=SMALL_BUFF))
        
        qn2 = DashedLine()
        qn2.add_updater(lambda m:\
            m.put_start_and_end_on(
                q.get_center(),
                get_n2()
            ))
        self.play(ShowCreation(qn2))
        self.play(
            ShowCreation(n2),
            Write(n2_label)
        )
        self.wait()

        self.play(
            Write(proof_head),
            Write(prf1))
        self.wait(3)

        self.play(ShowCreationThenDestruction(
            Polygon(
                a.get_center(),
                n2.get_center(),
                q.get_center())
        ))
        self.wait()

        self.play(ShowCreationThenDestruction(
            Polygon(
                a.get_center(),
                n1.get_center(),
                l.get_center())
        ))

        for e in [prf2, prf3, prf4, prf5]:
            self.wait(3)
            self.play(Write(e))

        self.wait(10)

        self.play(y_val.set_value, 4)
        self.play(q_y.set_value, 8)

        self.wait(10)
