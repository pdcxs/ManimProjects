from manimlib.imports import *
from ManimProjects.utils.Parabola import Parabola
from ManimProjects.utils.geometry import CText

# To Run this code, you should modify manim source files.
# In manimlib/mobject/mobject.py, add "plot_depth": 0 in the CONFIG of Mobject class
# In manimlib/camera/camera.py
# change the return line in extract_mpbject_family_members method to
# return remove_list_redundancies(list(it.chain(*[method(m) for m in (mobjects.sort(key=lambda m:m.plot_depth) if len(mobjects)>0 else [])])))

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
        'x_min': -4,
        'focus': 2
    }

    def construct(self):
        self.adjust_x_range()
        graph = self.get_graph(color=LIGHT_BROWN)
        focus = Dot(self.get_focus()).set_fill(DARK_BLUE)
        directrix = self.get_directrix()
        focusLabel = TexMobject('F').scale(0.75)
        focusLabel.next_to(focus, RIGHT, buff=SMALL_BUFF)
        self.directrix = directrix
        focus.plot_depth = 1

        sub1 = CText('在抛物线上任取不同的两点P1,P2').scale(0.4)
        sub1.to_corner(RIGHT+DOWN)

        p1_y = ValueTracker(7)
        p2_y = ValueTracker(2)

        p1 = Dot()
        p1.add_updater(lambda m: m.move_to(self.value_to_point(p1_y.get_value())))
        p1.plot_depth = 1

        p2 = Dot()
        p2.add_updater(lambda m: m.move_to(self.value_to_point(p2_y.get_value())))
        p2.plot_depth = 1

        p1.set_fill(RED)
        p2.set_fill(RED)

        p1Label = TexMobject('P_1').scale(0.75)
        p2Label = TexMobject('P_2').scale(0.75)

        p1Label.add_updater(lambda m:\
            m.next_to(p1, RIGHT, buff=SMALL_BUFF))
        p2Label.add_updater(lambda m:\
            m.next_to(p2, LEFT+UP, buff=SMALL_BUFF))

        sub2 = CText('连接两点，延长交准线于点K')
        sub2.scale(0.4).to_corner(RIGHT+DOWN)

        ppLine = Line()

        ppLine.add_updater(lambda m:\
            m.put_start_and_end_on(p1.get_center(),\
            self.get_directrix_point(p1, p2)))

        k = Dot()
        k.plot_depth = 1
        k.set_fill(DARK_BLUE)
        k.add_updater(lambda m: m.move_to(ppLine.points[-1]))

        kLabel = TexMobject('K').scale(0.75)
        kLabel.add_updater(lambda m:\
            m.next_to(k, LEFT, buff=SMALL_BUFF))

        sub3 = CText('分别连接P1F, P2F')
        sub3.scale(0.4).to_corner(RIGHT+DOWN)

        p1f = Line()
        p2f = Line()
        p1f.add_updater(lambda m:\
            m.put_start_and_end_on(p1.get_center(),\
            focus.get_center()))
        p2f.add_updater(lambda m:\
            m.put_start_and_end_on(p2.get_center(),\
            focus.get_center()))

        sub4 = CText('延长P1F交准线于D')
        sub4.scale(0.4).to_corner(RIGHT+DOWN)

        p1fd = Line()
        p1fd.add_updater(lambda m:\
            m.put_start_and_end_on(\
            focus.get_center(),\
            self.get_directrix_point(p1, focus)))
        d = Dot()
        d.plot_depth = 1
        d.set_fill(DARK_BLUE)
        d.add_updater(lambda m: m.move_to(p1fd.points[-1]))
        dLabel = TexMobject('D')
        dLabel.scale(0.75)
        dLabel.add_updater(lambda m:\
            m.next_to(d, LEFT, buff=SMALL_BUFF))

        sub5 = CText('连接KF')
        sub5.scale(0.4).to_corner(RIGHT+DOWN)

        kf = Line()
        kf.add_updater(lambda m:\
            m.put_start_and_end_on\
            (k.get_center(), focus.get_center()))

        ang1 = ArcBetweenPoints(*self.get_arc_point(
            p2.get_center(),
            focus.get_center(),
            k.get_center()
        ))
        ang1.add_updater(lambda m:\
            m.put_start_and_end_on(
                *self.get_arc_point(
                p2.get_center(),
                focus.get_center(),
                k.get_center()
            )))
        ang1Label = TexMobject('1').scale(0.5)
        ang1Label.add_updater(lambda m:\
            m.move_to(ang1.get_center()))
        
        ang2 = ArcBetweenPoints(*self.get_arc_point(
            k.get_center(),
            focus.get_center(),
            d.get_center()
        ))
        ang2.add_updater(lambda m:\
            m.put_start_and_end_on(
                *self.get_arc_point(
                k.get_center(),
                focus.get_center(),
                d.get_center()
            )))
        ang2Label = TexMobject('2').scale(0.5)
        ang2Label.add_updater(lambda m:\
            m.move_to(ang2.get_center()))

        ang1Value = DecimalNumber(self.get_angle(
            p2.get_center(),
            focus.get_center(),
            k.get_center()) / DEGREES, num_decimal_places=2)
        ang1Value.add_updater(lambda m:\
            m.set_value(self.get_angle(
                p2.get_center(),
                focus.get_center(),
                k.get_center()
            ) / DEGREES))
        ang2Value = DecimalNumber(self.get_angle(
            k.get_center(),
            focus.get_center(),
            d.get_center()) / DEGREES, num_decimal_places=2)
        ang2Value.add_updater(lambda m:\
            m.set_value(self.get_angle(
                k.get_center(),
                focus.get_center(),
                d.get_center()
            ) / DEGREES))

        ang1Tail = TexMobject('^{\circ}')
        ang2Tail = TexMobject('^{\circ}')
        
        ang1head = TexMobject('\\angle 1=')
        ang1Text = VGroup(ang1head, ang1Value, ang1Tail)
        ang1Text.arrange(buff=SMALL_BUFF)
        ang1Tail.shift(0.15*UP)

        ang2head = TexMobject('\\angle 2=')
        ang2Text = VGroup(ang2head, ang2Value, ang2Tail)
        ang2Text.arrange(buff=SMALL_BUFF)
        ang2Tail.shift(0.15*UP)

        angs = VGroup(ang1Text, ang2Text)
        angs.arrange(buff=MED_SMALL_BUFF)
        angs.shift(3*RIGHT + 2*UP)

        m1 = Dot()
        m1.plot_depth = 1
        m1.set_fill(ORANGE)
        m1.add_updater(lambda m:\
            m.move_to(self.coords_to_point(
                -self.focus, p1_y.get_value()
            )))

        m2 = Dot()
        m2.plot_depth = 1
        m2.set_fill(ORANGE)
        m2.add_updater(lambda m:\
            m.move_to(self.coords_to_point(
                -self.focus, p2_y.get_value()
            )))

        m1Label = TexMobject('M_1').scale(0.75)
        m2Label = TexMobject('M_2').scale(0.75)
        m1Label.add_updater(lambda m:\
            m.next_to(m1, LEFT, buff=SMALL_BUFF))
        m2Label.add_updater(lambda m:\
            m.next_to(m2, LEFT, buff=SMALL_BUFF))


        m1p1 = DashedLine()
        m1p1.add_updater(lambda m:\
            m.put_start_and_end_on(
                m1.get_center(), p1.get_center()
            ))
        m2p2 = DashedLine()
        m2p2.add_updater(lambda m:\
            m.put_start_and_end_on(
                m2.get_center(), p2.get_center()
            ))

        fracs = TexMobject('{KP_2', '\\over', 'KP_1}', '=',
            '{M_2P_2', '\\over', 'M_1P_1}', '=',
            '{FP_2', '\\over', 'FP_1}')
        fracs.shift(3*RIGHT + 2*UP)

        fracs2 = TexMobject('{KP_2', '\\over', 'KP_1}', '=',
            '{FP_2', '\\over', 'FP_1}')
        fracs2.move_to(fracs.get_center())
        fracs2.align_to(fracs, LEFT)

        fracs3 = TexMobject('{KP_2', '\\over', 'FP_2}', '=',
            '{KP_1', '\\over', 'FP_1}')
        fracs3.move_to(fracs2.get_center())

        explain = CText('由正弦定理').scale(0.4)
        explain.next_to(fracs3, DOWN)
        explain.align_to(fracs3, LEFT)

        fracs4 = TexMobject('{\\sin\\angle 1', '\\over', '\\sin\\angle K}', '=',
            '{\\sin\\angle KFP_1', '\\over', '\\sin\\angle K}')
        fracs4.next_to(explain, DOWN)
        fracs4.align_to(explain, LEFT)

        form = TexMobject('\\sin \\angle 1 = \\sin \\angle KFP_1')
        form.next_to(fracs4, DOWN)
        form.align_to(fracs4, LEFT)

        form2 = TexMobject('\\angle1 < \\angle KFP_1 < \\pi')
        form2.next_to(form, DOWN)
        form2.align_to(form, LEFT)

        form3 = TexMobject('\\angle1 = \pi - \\angle KFP_1 = \\angle 2')
        form3.next_to(form2, DOWN)
        form3.align_to(form2, LEFT)

        remover = Rectangle(height=FRAME_HEIGHT, width=FRAME_WIDTH)
        remover.set_color(BLACK)
        remover.set_fill(BLACK, opacity=1)
        remover.plot_depth = 2
        # kp2 = Line()
        # kp2.add_updater(lambda m:\
        #     m.put_start_and_end_on(k.get_center(),
        #     p2.get_center()))
        # kp2.set_color(YELLOW)
        ############################################
        # Animation part                           #
        ############################################
        self.play(ShowCreation(focus), ShowCreation(directrix))
        self.play(ShowCreation(graph), Write(focusLabel))

        self.play(Write(sub1))
        self.play(*[ShowCreation(e) for e in\
            [p1, p2, p1Label, p2Label]])
        self.wait()

        self.play(FadeOut(sub1))
        self.play(Write(sub2))

        self.wait()
        self.play(ShowCreation(ppLine))
        self.play(ShowCreation(k), Write(kLabel))

        self.wait()
        self.play(FadeOut(sub2))
        self.play(Write(sub3))

        self.play(*[ShowCreation(e) for e in [p1f, p2f]])

        self.wait()
        self.play(FadeOut(sub3))
        self.play(Write(sub4))

        self.play(ShowCreation(p1fd))
        self.play(*[ShowCreation(e) for e in [d, dLabel]])

        self.wait()
        self.play(FadeOut(sub4))
        self.play(Write(sub5))

        self.wait()
        self.play(ShowCreation(kf))
        self.play(ShowCreation(ang1), Write(ang1Label))
        self.play(ShowCreation(ang2), Write(ang2Label))
        self.play(FadeOut(sub5))

        self.play(Write(angs))

        self.play(*[ShowCreation(e) for e in\
            [m1, m2, m1p1, m2p2, m1Label, m2Label]])

        self.play(ApplyMethod(p2_y.set_value, -1), run_time=2)
        self.wait()
        self.play(ApplyMethod(p1_y.set_value, 5))
        self.wait()
        self.play(ApplyMethod(p1_y.set_value, 9), run_time=3)
        self.wait()
        self.play(ApplyMethod(p2_y.set_value, 3), run_time=2)

        self.play(FadeOut(angs))
        self.wait()

        self.play(Write(fracs))
        self.wait(5)
        #self.play(ReplacementTransform(fracs, fracs2))
        self.play(FadeOut(fracs[4:8]))
        self.play(*[ApplyMethod(fracs[i].move_to, fracs[i - 4].get_center()) for i in range(8, 11)])

        # self.play(FadeOut(fracs), FadeIn(fracs2), run_time=0.1)

        # self.wait(5)
        # self.play(ReplacementTransform(fracs2, fracs3))
        self.wait(5)
        pos1 = fracs[2].get_center()
        pos2 = fracs[8].get_center()
        self.play(ApplyMethod(fracs[2].move_to, pos2),
            ApplyMethod(fracs[8].move_to, pos1))

        self.wait(5)
        self.play(Write(explain))
        self.wait(3)

        self.play(ShowCreationThenDestruction(Polygon(
            k.get_center(), focus.get_center(),
            p2.get_center()
        ).set_fill(DARK_BLUE, opacity=1)), run_time=3)
        self.play(Write(fracs4[:3]))

        self.play(ShowCreationThenDestruction(Polygon(
            k.get_center(), focus.get_center(),
            p1.get_center()
        ).set_fill(DARK_BLUE, opacity=1)), run_time=3)
        self.play(Write(fracs4[3:]))

        self.wait(3)
        self.play(Write(form))
        self.wait(3)
        self.play(Write(form2))
        self.wait(3)
        self.play(Write(form3))
        self.wait(5)

        self.play(FadeIn(remover))

    def get_directrix_point(self, p1, p2):
        p1c = p1.get_center()
        p2c = p2.get_center()
        vec = p2c - p1c
        vec /= vec[0]
        p3 = p2c + (self.directrix.get_center() - p2c)[0] * vec
        return p3

    def get_arc_point(self, p1, c, p2, radius=0.3):
        v1 = normalize(p1 - c)
        v2 = normalize(p2 - c)
        return [v1 * radius + c, v2 * radius + c]

    def get_angle(self, p1, c, p2):
        v1 = p1 - c
        v2 = p2 - c
        v1n = np.sum([x**2 for x in v1])
        v2n = np.sum([x**2 for x in v2])
        ang = np.arccos(np.dot(v1, v2) /\
            np.sqrt(v1n * v2n))
        return ang

class Summary(Scene):
    def construct(self):
        text = CText('总结')
        text.set_fill(DARK_BROWN)

        content1 = CText('抛物线任意弦与准线的交点')
        content2 = CText('及该抛物线的焦点所构成的线段，')
        content3 = CText('平分该弦两端点与焦点所构成角的外角')
        contents = VGroup(content1, content2, content3)
        contents.scale(0.7)
        contents.arrange(DOWN)

        total = VGroup(text, contents)
        total.arrange(DOWN, buff=MED_LARGE_BUFF)

        self.play(Write(text))
        self.wait(2)
        self.play(Write(contents))
        self.wait(10)