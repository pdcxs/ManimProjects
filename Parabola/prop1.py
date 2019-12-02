from manimlib.imports import *
from ManimProjects.utils.Parabola import Parabola
from ManimProjects.utils.geometry import CText

class OpenScene(Scene):
    def construct(self):
        text1 = CText('这是一条重要的性质')
        text2 = CText('后面会经常用到')

        group = VGroup(text1, text2)
        group.arrange(DOWN)

        self.play(Write(text1))
        self.wait()
        self.play(Write(text2))
        self.wait()
        self.play(FadeOut(group))

class Prop1(Parabola):
    CONFIG = {
        'x_min': -3.5,
        'focus': 2
    }

    def construct(self):
        self.adjust_x_range()
        graph = self.get_graph(color=LIGHT_BROWN)
        focus = Dot(self.get_focus()).set_fill(DARK_BLUE)
        directrix = self.get_directrix()
        focusLabel = TexMobject('F').scale(0.75)
        focusLabel.next_to(focus, RIGHT+UP, buff=SMALL_BUFF)
        self.directrix = directrix

        self.play(ShowCreation(focus), ShowCreation(directrix))
        self.play(ShowCreation(graph), Write(focusLabel))

        sub1 = CText('在抛物线上任取不同的两点P1,P2').scale(0.4)
        sub1.to_corner(RIGHT+DOWN)
        self.play(Write(sub1))

        p1_y = ValueTracker(7)
        p2_y = ValueTracker(2)

        p1 = Dot()
        p1.add_updater(lambda m: m.move_to(self.value_to_point(p1_y.get_value())))

        p2 = Dot()
        p2.add_updater(lambda m: m.move_to(self.value_to_point(p2_y.get_value())))

        p1.set_fill(RED)
        p2.set_fill(RED)

        p1Label = TexMobject('P_1').scale(0.75)
        p2Label = TexMobject('P_2').scale(0.75)

        p1Label.add_updater(lambda m:\
            m.next_to(p1, LEFT+UP, buff=SMALL_BUFF))
        p2Label.add_updater(lambda m:\
            m.next_to(p2, LEFT+UP, buff=SMALL_BUFF))

        self.play(*[ShowCreation(e) for e in\
            [p1, p2, p1Label, p2Label]])

        self.wait()

        sub2 = CText('连接两点，延长交准线与点K')
        sub2.scale(0.4).to_corner(RIGHT+DOWN)
        self.play(FadeOut(sub1))
        self.play(Write(sub2))

        ppLine = Line()

        ppLine.add_updater(lambda m:\
            m.put_start_and_end_on(p1.get_center(),\
            self.get_directrix_point(p1, p2)))

        k = Dot()
        k.set_fill(DARK_BLUE)
        k.add_updater(lambda m: m.move_to(ppLine.points[-1]))

        kLabel = TexMobject('K').scale(0.75)
        kLabel.add_updater(lambda m: m.next_to(k, LEFT, buff=SMALL_BUFF))
        
        self.wait()
        self.play(ShowCreation(ppLine))
        self.play(ShowCreation(k), Write(kLabel))

        sub3 = CText('分别连接P1F, P2F')
        sub3.scale(0.4).to_corner(RIGHT+DOWN)
        self.wait()
        self.play(FadeOut(sub2))
        self.play(Write(sub3))

        p1f = Line()
        p2f = Line()
        p1f.add_updater(lambda m:\
            m.put_start_and_end_on(p1.get_center(),\
            focus.get_center()))
        p2f.add_updater(lambda m:\
            m.put_start_and_end_on(p2.get_center(),\
            focus.get_center()))
        self.play(*[ShowCreation(e) for e in [p1f, p2f]])

        self.wait()
        sub4 = CText('延长P1F交准备与D')
        sub4.scale(0.4).to_corner(RIGHT+DOWN)
        self.play(FadeOut(sub3))
        self.play(Write(sub4))

        p1fd = Line()
        p1fd.add_updater(lambda m:\
            m.put_start_and_end_on(\
            focus.get_center(),\
            self.get_directrix_point(p1, focus)))
        d = Dot()
        d.set_fill(DARK_BLUE)
        d.add_updater(lambda m: m.move_to(p1fd.points[-1]))
        dLabel = TexMobject('D')
        dLabel.scale(0.75)
        dLabel.add_updater(lambda m:\
            m.next_to(d, LEFT, buff=SMALL_BUFF))
        self.play(ShowCreation(p1fd))
        self.play(*[ShowCreation(e) for e in [d, dLabel]])

        sub5 = CText('连接KF')
        sub5.scale(0.4).to_corner(RIGHT+DOWN)
        self.wait()
        self.play(FadeOut(sub4))
        self.play(Write(sub5))

        kf = Line()
        kf.add_updater(lambda m:\
            m.put_start_and_end_on\
            (k.get_center(), focus.get_center()))
        self.play(ShowCreation(kf))

    def get_directrix_point(self, p1, p2):
        p1c = p1.get_center()
        p2c = p2.get_center()
        vec = p2c - p1c
        vec /= vec[0]
        p3 = p2c + (self.directrix.get_center() - p2c)[0] * vec
        return p3