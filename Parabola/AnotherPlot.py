from manimlib.imports import *
from ManimProjects.utils.Parabola import Parabola
from ManimProjects.utils.geometry import CText

class OpenScene(Scene):
    def construct(self):
        sub1 = CText('根据性质1')
        sub2 = CText('可以用另一种方法找到')
        sub3 = CText('抛物线上的点')

        subs = VGroup(sub1, sub2, sub3)
        subs.arrange(DOWN)

        self.play(Write(sub1))
        self.wait()
        self.play(Write(sub2))
        self.wait()
        self.play(Write(sub3))
        self.wait(5)
        self.play(FadeOut(subs))

class Definition(Parabola):
    CONFIG = {
        'x_min': -10,
        'focus': 3
    }
    def construct(self):
        self.adjust_x_range()
        sub1 = CText('已知准线与焦点')
        sub1.scale(0.3)
        sub1.to_edge(RIGHT)
        self.play(Write(sub1))
        directrix = self.get_directrix()
        focus = Dot()
        focus.move_to(self.get_focus())
        focus.set_fill(DARK_BROWN)
        focus.plot_depth = 1
        focus_label = TexMobject('F').scale(0.5)
        focus_label.next_to(focus, RIGHT + UP,\
            buff=SMALL_BUFF)
        self.play(*[ShowCreation(e) for e in
            [directrix, focus, focus_label]])

        sub2 = CText('先找到顶点A')
        sub2.scale(0.3)
        sub2.to_edge(RIGHT)

        self.wait()
        self.play(FadeOut(sub1))
        self.play(Write(sub2))

        fl = Line(
            directrix.get_center(),
            focus.get_center()
        )
        a = Dot()
        a.move_to(fl.get_center())
        a.set_fill(DARK_BROWN)
        a.plot_depth = 1
        a_label = TexMobject('A').scale(0.5)
        a_label.next_to(a, RIGHT + UP,\
            buff=SMALL_BUFF)
        self.play(ShowCreation(fl))
        self.play(ShowCreation(a))
        self.play(FadeOut(fl), ShowCreation(a_label))

        y_val = ValueTracker(4)

        sub3 = CText('在准线上任取一点')
        sub3.scale(0.3)
        sub3.to_edge(RIGHT)
        self.play(FadeOut(sub2))
        self.play(Write(sub3))

        m = Dot()
        m.set_fill(DARK_BLUE)
        m.plot_depth = 1
        m.add_updater(lambda m:\
            m.move_to(self.coords_to_point(
                -self.focus, y_val.get_value()
            )))
        m_label = TexMobject('M').scale(0.5)
        m_label.add_updater(lambda l: l.next_to(m, LEFT))
        self.play(ShowCreation(m), ShowCreation(m_label))

        self.wait()
        sub4 = CText('连接相应的点')
        sub4.scale(0.3)
        sub4.to_edge(RIGHT)
        self.play(FadeOut(sub3))
        self.play(Write(sub4))

        ma = Line()
        ma.add_updater(lambda l:\
            l.put_start_and_end_on(
                m.get_center(),
                a.get_center()
            ))

        af = Line(a.get_center(), focus.get_center() + RIGHT)

        mf = Line()
        mf.add_updater(lambda l:\
            l.put_start_and_end_on(
                m.get_center(),
                focus.get_center()
            ))

        self.play(*[ShowCreation(e) for e in
            [af, mf, ma]])
        self.wait()
        
        sub5 = CText('延长MA, MF')
        sub5.scale(0.3)
        sub5.to_edge(RIGHT)
        self.play(FadeOut(sub4))
        self.play(Write(sub5))

        def get_ma_extent():
            vec = a.get_center() - m.get_center()
            vec *= FRAME_WIDTH
            return a.get_center() + vec

        ma_extent = Line()
        ma_extent.add_updater(lambda l:\
            l.put_start_and_end_on(
                a.get_center(),
                get_ma_extent()
            ))

        def get_mf_extent():
            vec = focus.get_center() - m.get_center()
            return focus.get_center() + normalize(vec)

        mf_extent = Line()
        mf_extent.add_updater(lambda l:\
            l.put_start_and_end_on(
                focus.get_center(),
                get_mf_extent()
            ))

        self.play(
            ShowCreation(mf_extent),
            ShowCreation(ma_extent))
        
        self.wait()
        sub6 = CText('做对称线(相等的角)')
        sub6.scale(0.3)
        sub6.to_edge(RIGHT)
        self.play(FadeOut(sub5))
        self.play(Write(sub6))

        def get_flip():
            loc = get_mf_extent()
            f = focus.get_center()
            x = loc[0] - f[0]
            y = loc[1] - f[1]
            ang = 2 * np.arctan2(y, x)
            vec = np.cos(ang) * RIGHT + np.sin(ang) * UP
            return vec

        mf_flip = Line()
        mf_flip.add_updater(lambda l:\
            l.put_start_and_end_on(
                focus.get_center(),
                get_flip() + focus.get_center()
            ))

        self.play(ShowCreation(mf_flip))

        sub7 = CText('交MA于点P')
        sub7.scale(0.3)
        sub7.to_edge(RIGHT)
        self.play(FadeOut(sub6))
        self.play(Write(sub7))

        mf_flip_extent = Line()
        mf_flip_extent.add_updater(lambda l:\
            l.put_start_and_end_on(
                focus.get_center(),
                get_flip() * FRAME_WIDTH\
                    + focus.get_center()
            ))
        self.play(ShowCreation(mf_flip_extent))

        def get_p():
            x1 = m.get_center()[0]
            y1 = m.get_center()[1]
            x2 = a.get_center()[0]
            y2 = a.get_center()[1]
            x3 = focus.get_center()[0]
            y3 = focus.get_center()[1]
            vec = get_flip()
            x4 = x3 + vec[0]
            y4 = y3 + vec[1]

            a1 = y2 - y1
            b1 = x1 - x2
            c1 = a1 * x1 + b1 * y1

            a2 = y4 - y3
            b2 = x3 - x4
            c2 = a2 * x3 + b2 * y3

            determinant = a1*b2 - a2*b1

            if determinant == 0:
                return a.get_center()

            x = (b2 * c1 - b1 * c2) / determinant
            y = (a1 * c2 - a2 * c1) / determinant
            return x * RIGHT + y * UP

        p = Dot()
        p.set_fill(DARK_BLUE)
        p.plot_depth = 1
        p.add_updater(lambda m: m.move_to(get_p()))

        p_label = TexMobject('P').scale(0.5)
        p_label.add_updater(lambda m:\
            m.next_to(p, RIGHT, buff=SMALL_BUFF))
        self.play(ShowCreation(p), ShowCreation(p_label))

        self.wait(3)
        self.play(ApplyMethod(y_val.set_value, -4))

        graph = self.get_graph(color=LIGHT_BROWN)
        self.play(ShowCreation(graph))

        self.wait(3)
        self.play(ApplyMethod(y_val.set_value, -8))

        self.wait(3)
        self.play(ApplyMethod(y_val.set_value, -6))

        self.wait(3)
        self.play(ApplyMethod(y_val.set_value, 6))

        self.wait(3)
        self.play(ApplyMethod(y_val.set_value, 8))
        self.wait(10)