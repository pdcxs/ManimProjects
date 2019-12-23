from manimlib.imports import *
from ManimProjects.utils.Parabola import Parabola
from ManimProjects.utils.geometry import *

class OpenScene(Scene):
    def construct(self):
        sub1 = CText('这是一个')
        sub2 = CText('关于切线的性质')
        subs = VGroup(sub1, sub2)
        subs.arrange(DOWN)
        self.play(Write(sub1))
        self.play(Write(sub2))
        self.wait(2)
        self.play(FadeOut(subs))

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

        prop1 = TexMobject('1.\\quad KF \\perp PF')
        prop1.scale(0.5)

        prop2 = TexMobject(\
            '2.\\quad \\angle 1 = \\angle 2')
        prop2.scale(0.5)

        proofs = VGroup()
        prof1 = CText('证明思路1').scale(0.25)
        prof2 = CText('切线可以看作端点重合的弦')\
            .scale(0.25)
        prof3 = CText('再结合性质1，可证第一点')\
            .scale(0.25)
        prof4 = CText('证明思路2').scale(0.25)
        prof5 = CText('全等三角形').scale(0.25)

        proofs.add(prof1)
        for e in [prof2, prof3, prof4, prof5]:
            proofs.add(e)
        proofs.arrange(DOWN)

        for e in [prof2, prof3, prof4, prof5]:
            e.align_to(prof1, LEFT)
        
        props = VGroup(prop1, prop2, proofs)
        props.arrange(DOWN)
        prop2.align_to(prop1, LEFT)
        proofs.align_to(prop1, LEFT)

        props.to_edge(RIGHT)

        ang1 = Angle(m, p, k)
        ang1.show_edge = True
        ang1.set_fill(ORANGE, opacity=0.25)
        ang1.make_angle_dynamic()
        ang1_label = TexMobject('1').scale(0.5)
        ang1.add_label(ang1_label)

        ang2 = Angle(k, p, focus)
        ang2.show_edge = True
        ang2.set_fill(ORANGE, opacity=0.25)
        ang2.make_angle_dynamic()
        ang2_label = TexMobject('2').scale(0.5)
        ang2.add_label(ang2_label)

        self.play(
            ShowCreation(ang1),
            ShowCreation(ang2))
        self.play(
            ShowCreation(ang1_label),
            ShowCreation(ang2_label))

        self.wait(3)

        self.play(Write(prop1))
        self.wait(3)
        self.play(Write(prop2))
        self.wait(3)

        self.play(y_val.set_value, 4)

        for e in [prof1, prof2, prof3, prof4, prof5]:
            self.play(Write(e))
            self.wait(3)
