from manimlib.imports import *
from ManimProjects.utils.geometry import *
from ManimProjects.utils.Parabola import *

class OpenScene(Scene):
    def construct(self):
        sub1 = CText('抛物线')
        sub1.set_color(DARK_BLUE)
        sub2 = CText('性质四')

        line1 = VGroup(sub1, sub2)
        line1.arrange(RIGHT)

        line2 = CText('这是一条相当有用的性质')
        line2.scale(0.5)
        lines = VGroup(line1, line2)
        lines.arrange(DOWN, buff=LARGE_BUFF)

        self.play(Write(line1))
        self.play(WiggleOutThenIn(sub1))
        self.wait()
        self.play(Write(line2))
        self.wait(5)

        self.play(FadeOut(lines))

class Prop4(Parabola):
    CONFIG = {
        'focus': 3,
        'x_min': -10
    }

    def construct(self):
        self.adjust_x_range()
        graph = self.get_graph(ORANGE)
        f = Dot()
        f.plot_depth = 1
        f.move_to(self.get_focus())
        f.set_color(ORANGE)
        drct = self.get_directrix()
        f_label = TexMobject('F').scale(0.5)
        f_label.next_to(f, RIGHT)

        self.play(*[ShowCreation(e) for e in\
            [graph, f, drct]])
        self.play(ShowCreation(f_label))
        self.wait()

        sub1 = CText('取任一焦点弦P1P2').scale(0.3)
        sub1.to_edge(RIGHT)
        self.play(Write(sub1))

        y_val = ValueTracker(9)
        p1 = Dot()
        p1.plot_depth = 1
        p1.set_fill(DARK_BLUE)
        p1.add_updater(lambda m:\
            m.move_to(self.value_to_point(
                y_val.get_value())))
        p1_label = TexMobject('P_1').scale(0.5)
        p1_label.plot_depth = 2
        p1_label.add_updater(lambda m:\
            m.next_to(p1, RIGHT, buff=SMALL_BUFF))
        
        self.play(ShowCreation(p1))
        self.play(ShowCreation(p1_label))

        p2 = Dot()
        p2.plot_depth = 1
        p2.set_fill(DARK_BLUE)
        p2.add_updater(lambda m:\
            m.move_to(self.get_opposite(p1)))
        p2_label = TexMobject('P_2').scale(0.5)
        p2_label.plot_depth = 2
        p2_label.add_updater(lambda m:\
            m.next_to(p2, RIGHT, buff=SMALL_BUFF))

        p1p2 = Line()
        p1p2.add_updater(lambda m:\
            m.put_start_and_end_on(
                p1.get_center(),
                self.get_opposite(p1)
            ))
        
        self.play(ShowCreation(p1p2))
        self.play(ShowCreation(p2))
        self.play(ShowCreation(p2_label))
        self.wait()

        sub2 = CText('过焦点弦两端点分别做抛物线的切线')
        sub2.scale(0.3)
        sub2.to_edge(RIGHT)

        self.play(FadeOut(sub1))
        self.play(Write(sub2))
        self.wait()

        p1_tangent = Line()
        self.add_tangent_line_updater(p1_tangent, p1)

        p2_tangent = Line()
        self.add_tangent_line_updater(p2_tangent, p2)

        self.play(
            ShowCreation(p1_tangent),
            ShowCreation(p2_tangent)
        )
        self.wait()

        sub3 = CText('相交于点Z').scale(0.3)
        sub3.to_edge(RIGHT)
        self.play(FadeOut(sub2))
        self.play(Write(sub3))

        z = Dot()
        z.plot_depth = 1
        z.set_fill(DARK_BLUE)
        z.add_updater(lambda m:\
            m.move_to(self.get_tangent_to_directrix(p1)))
        
        z_label = TexMobject('Z').scale(0.5)
        z_label.add_updater(lambda m:\
            m.next_to(z, LEFT, buff=SMALL_BUFF))

        self.play(ShowCreation(z))
        self.play(ShowCreation(z_label))
        self.wait()

        sub4_line1 = VGroup(
            CText('则').scale(0.3),
            TexMobject('P_1Z\\perp P_2Z').scale(0.5)
        )
        sub4_line1.arrange(RIGHT, buff=SMALL_BUFF)
        sub4_line2 = CText('且Z在准线上').scale(0.3)
        sub4 = VGroup(
            sub4_line1,
            sub4_line2
        )
        sub4.arrange(DOWN)
        sub4.to_edge(RIGHT)
        sub4_line2.align_to(sub4_line1, LEFT)

        self.play(FadeOut(sub3))
        self.play(Write(sub4))
        self.wait()

        angle_z = Angle(p2, z, p1, radius=0.2, show_edge=True)
        angle_z.set_fill(RED, opacity=0.7)
        angle_z.set_color(RED)
        angle_z.plot_depth = -1
        angle_z.make_angle_dynamic()
        self.play(ShowCreation(angle_z))

        self.play(y_val.set_value, 4)
        self.wait()
        self.play(y_val.set_value, 9)
        self.wait(5)

        self.play(FadeOut(sub4))
        
        m1 = Dot()
        m1.set_fill(DARK_BLUE)
        m1.plot_depth = 1
        m1.add_updater(lambda m:\
            m.move_to(
                self.coords_to_point(
                    -self.focus,
                    y_val.get_value()
                )
            ))

        m1_label = TexMobject('M_1').scale(0.5)
        m1_label.add_updater(lambda m:\
            m.next_to(m1, LEFT, buff=SMALL_BUFF))

        p1m1 = Line()
        p1m1.put_start_and_end_on(
            m1.get_center(),
            p1.get_center())
        
        self.play(ShowCreation(p1m1))
        self.play(ShowCreation(m1))
        self.play(ShowCreation(m1_label))
        self.wait()

        p1m1.add_updater(lambda m:\
            m.put_start_and_end_on(
                m1.get_center(),
                p1.get_center()
            ))

        zf = Line()
        zf.add_updater(lambda m:\
            m.put_start_and_end_on(
                z.get_center(),
                f.get_center()
            ))
        self.play(ShowCreation(zf))
        self.wait()

        m2 = Dot()
        m2.set_fill(DARK_BLUE)
        m2.plot_depth = 1
        m2.align_to(m1, LEFT)
        m2.add_updater(lambda m:\
            m.align_to(p2, UP))

        m2_label = TexMobject('M_2').scale(0.5)
        m2_label.add_updater(lambda m:\
            m.next_to(m2, LEFT, buff=SMALL_BUFF))

        p2m2 = Line()
        p2m2.put_start_and_end_on(
            m2.get_center(),
            p2.get_center())
        
        self.play(ShowCreation(p2m2))
        self.play(ShowCreation(m2))
        self.play(ShowCreation(m2_label))
        self.wait()

        p2m2.add_updater(lambda m:\
            m.put_start_and_end_on(
                m2.get_center(),
                p2.get_center()
            ))

        angle1 = Angle(
            p1, z, m1,
            show_edge = True,
            radius=0.3
        )
        angle1.set_fill(GREEN_E, opacity=0.8)
        angle1.make_angle_dynamic()
        angle1_label = TexMobject('1').scale(0.5)
        angle1.add_label(angle1_label, buff=MED_SMALL_BUFF)
        self.play(ShowCreation(angle1))
        self.play(ShowCreation(angle1_label))
        self.wait()

        angle2 = Angle(
            f, z, p1,
            show_edge = True,
            radius=0.3
        )
        angle2.set_fill(GREEN_E, opacity=0.8)
        angle2.make_angle_dynamic()
        angle2_label = TexMobject('2').scale(0.5)
        angle2.add_label(angle2_label, buff=MED_SMALL_BUFF)
        self.play(ShowCreation(angle2))
        self.play(ShowCreation(angle2_label))
        self.wait()

        angle3 = Angle(
            p2, z, f,
            show_edge = True,
            radius=0.5
        )
        angle3.set_fill(GOLD_E, opacity=0.8)
        angle3.make_angle_dynamic()
        angle3_label = TexMobject('3').scale(0.5)
        angle3.add_label(angle3_label, buff=MED_SMALL_BUFF)
        self.play(ShowCreation(angle3))
        self.play(ShowCreation(angle3_label))
        self.wait()

        angle4 = Angle(
            m2, z, p2,
            show_edge = True,
            radius=0.5
        )
        angle4.set_fill(GOLD_E, opacity=0.8)
        angle4.make_angle_dynamic()
        angle4_label = TexMobject('4').scale(0.5)
        angle4.add_label(angle4_label, buff=MED_SMALL_BUFF)
        self.play(ShowCreation(angle4))
        self.play(ShowCreation(angle4_label))
        self.wait()

        proof1 = CText('设Z为P1切线与准线交点')
        proof1.scale(0.3)

        proof2 = TexMobject('ZF \\perp P_1P_2')
        proof2.scale(0.65)

        proof3 = CText('显然Z也是P2与准线的交点')
        proof3.scale(0.3)

        proof4 = TexMobject('\\angle 1 = \\angle2, \\angle 3 = \\angle 4')
        proof4.scale(0.65)

        proof5 = CText('所以P1Z垂直于P2Z')
        proof5.scale(0.3)

        proof = VGroup()
        proof.add(proof1, proof2, proof3, proof4, proof5)
        proof.arrange(DOWN)
        proof.to_edge(RIGHT)

        for i in [proof2, proof3, proof4, proof5]:
            i.align_to(proof1, LEFT)
        
        self.play(Write(proof1))
        self.wait(5)
        self.play(Write(proof2))

        right_angle = Angle(p1, f, z)
        right_angle.radius = 0.2
        right_angle.show_edge = True
        right_angle.set_fill(MAROON_E, opacity=0.8)
        right_angle.plot_depth = -1
        right_angle.make_angle_dynamic()
        self.play(ShowCreation(right_angle))
        self.wait()
        self.play(WiggleOutThenIn(right_angle))
        self.wait(5)

        self.play(Write(proof3))
        self.wait(5)

        self.play(Write(proof4))
        self.wait()
        self.play(
            WiggleOutThenIn(angle1),
            WiggleOutThenIn(angle2)
        )
        self.wait()
        self.play(
            WiggleOutThenIn(angle3),
            WiggleOutThenIn(angle4)
        )
        self.wait(5)
        self.play(Write(proof5))
        self.wait(10)

        self.play(y_val.set_value, 6)
        self.wait(3)

        self.play(y_val.set_value, 3)
        self.wait(3)

        self.play(y_val.set_value, 7)
        self.wait(15)
