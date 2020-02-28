from manimlib.imports import *
from ManimProjects.utils.geometry import *
from ManimProjects.utils.Parabola import *
from ManimProjects.utils.calculation import *
from ManimProjects.utils.rate_functions import *

TEX_SIZE = 0.65
TEXT_SIZE = 0.3

class OpenScene(Scene):
    def construct(self):
        sub1 = CText('抛物线')
        sub1.set_color(DARK_BLUE)
        sub2 = CText('性质五')

        line1 = VGroup(sub1, sub2)
        line1.arrange(RIGHT)

        line2 = CText('切线与法线有一定的关系')
        line2.scale(0.5)
        lines = VGroup(line1, line2)
        lines.arrange(DOWN, buff=LARGE_BUFF)

        self.play(Write(line1))
        self.play(WiggleOutThenIn(sub1))
        self.wait()
        self.play(Write(line2))
        self.wait(5)

        self.play(FadeOut(lines))

class Prop5(Parabola):
    def construct(self):
        self.adjust_x_range()
        f = Dot()
        f.plot_depth = 1
        f.move_to(self.get_focus())
        f.set_fill(DARK_BROWN)

        f_label = Label(
            TexMobject('F').scale(TEX_SIZE),
            f,
            direction=DOWN
        )

        h_line = self.get_horizontal()
        directrix = self.get_directrix()
        graph = self.get_graph(DARK_BROWN)

        self.play(*[ShowCreation(e) for e in\
            [f, f_label, h_line, directrix, graph]])
        self.wait()

        sub1 = CText('任取一点P')
        sub1.scale(TEXT_SIZE)
        sub1.to_corner(UR)
        self.play(Write(sub1))
        self.wait()

        y_val = ValueTracker(7.5)

        p = Dot()
        p.plot_depth = 1
        p.set_color(DARK_BLUE)
        p.add_updater(lambda m:\
            m.move_to(self.value_to_point(
                y_val.get_value())))
        self.play(ShowCreation(p))

        p_label = Label(
            TexMobject('P').scale(TEX_SIZE),
            p,
            direction=UP
        )
        p_label.make_dynamic()
        self.play(ShowCreation(p_label))
        self.wait()

        sub2 = CText('过点P分别做抛物线的法线和切线')
        sub2.scale(TEXT_SIZE)
        sub2.to_corner(UR)

        self.play(FadeOut(sub1))
        self.play(Write(sub2))
        self.wait()

        tangent = Line()
        self.add_tangent_extent_updater(tangent, p)

        self.play(ShowCreation(tangent))
        self.wait()

        normal = Line()
        self.add_normal_updater(normal, p)
        self.play(ShowCreation(normal))
        self.wait()

        sub3 = CText('分别交轴于点T和点G')
        sub3.scale(TEXT_SIZE)
        sub3.to_corner(UR)
        self.play(FadeOut(sub2))
        self.play(Write(sub3))

        t = Dot()
        t.plot_depth = 1
        t.set_color(DARK_BLUE)
        t.add_updater(lambda m:\
            m.move_to(get_intersect(tangent, h_line, f)))
        
        self.play(ShowCreation(t))

        t_label = Label(
            TexMobject('T').scale(TEX_SIZE),
            t, direction=DOWN
        )
        t_label.make_dynamic()
        self.play(ShowCreation(t_label))
        self.wait()

        g = Dot()
        g.plot_depth = 1
        g.set_color(DARK_BLUE)
        g.add_updater(lambda m:\
            m.move_to(get_intersect(normal, h_line, f)))
        
        self.play(ShowCreation(g))

        g_label = Label(
            TexMobject('G').scale(TEX_SIZE),
            g, direction=DOWN
        )
        g_label.make_dynamic()
        self.play(ShowCreation(g_label))
        self.wait()

        pf = Line()
        pf.add_updater(lambda l:\
            l.put_start_and_end_on(
                p.get_center(),
                f.get_center()
            ))
        self.play(ShowCreation(pf))
        self.wait()

        sub4_1 = CText('则')
        sub4_1.scale(TEXT_SIZE)
        sub4_2 = TexMobject('TF=PF=GF')
        sub4_2.scale(TEX_SIZE)
        sub4 = VGroup(sub4_1, sub4_2)
        sub4.arrange(RIGHT)
        sub4.to_corner(UR)
        sub4.shift(LEFT)

        self.play(FadeOut(sub3))
        self.play(Write(sub4))

        gf = Line()
        gf.add_updater(lambda l:\
            l.put_start_and_end_on(
                g.get_center(),
                f.get_center()
            ))
        
        tf = Line()
        tf.add_updater(lambda l:\
            l.put_start_and_end_on(
                t.get_center(),
                f.get_center()
            ))
        self.add(gf, tf)

        self.play(tf.set_color, RED)
        self.play(pf.set_color, GREEN)
        self.play(gf.set_color, BLUE)
        self.wait(5)

        self.play(y_val.set_value, 2)
        self.wait()

        self.play(y_val.set_value, 8)
        self.wait()

        self.play(y_val.set_value, 7)
        self.wait()

        m = Dot()
        m.plot_depth = 1
        m.set_color(DARK_BLUE)

        self.add_directrix_point_updater(p, m)
        self.play(ShowCreation(m))

        m_label = Label(
            TexMobject('M').scale(TEX_SIZE),
            m, direction=LEFT
        )
        m_label.make_dynamic()
        self.play(ShowCreation(m_label))

        mp = Line()
        mp.add_updater(lambda l:\
            l.put_start_and_end_on(
                m.get_center(),
                p.get_center()
            ))
        self.play(ShowCreation(mp))

        mpt = Angle(m, p, t,
            radius=0.5, show_edge=True)
        mpt_label = TexMobject('1').scale(0.5)
        mpt.add_label(mpt_label)
        mpt.make_angle_dynamic()
        mpt.set_fill(RED, opacity=0.6)
        self.play(ShowCreation(mpt))
        self.play(ShowCreation(mpt_label))

        tpf = Angle(t, p, f,
            radius=0.5, show_edge=True)
        tpf_label = TexMobject('2').scale(0.5)
        tpf.add_label(tpf_label)
        tpf.make_angle_dynamic()
        tpf.set_fill(GREEN, opacity=0.6)
        self.play(ShowCreation(tpf))
        self.play(ShowCreation(tpf_label))

        ftp = Angle(f, t, p,
            radius=0.5, show_edge=True)
        ftp_label = TexMobject('3').scale(0.5)
        ftp.add_label(ftp_label)
        ftp.make_angle_dynamic()
        ftp.set_fill(BLUE, opacity=0.6)
        self.play(ShowCreation(ftp))
        self.play(ShowCreation(ftp_label))

        right_angle = Angle(t, p, g, radius=0.2)
        right_angle.is_right = True
        right_angle.make_angle_dynamic()
        self.play(ShowCreation(right_angle))
        self.wait(5)

        proof1 = TexMobject('\\because MP \\parallel TG')
        proof2 = TexMobject('\\therefore \\angle 1 = \\angle 3')
        proof3 = TexMobject('\\because \\angle 1 = \\angle 2')
        proof4 = TexMobject('\\therefore \\angle 2 = \\angle 3')
        proof5 = TexMobject('\\because TP \\perp GP')
        proof6 = TexMobject('\\therefore TF=PF=GF')

        proofs = [proof1, proof2, proof3, proof4, proof5, proof6]
        proof = VGroup()

        for e in proofs:
            e.scale(TEX_SIZE)
            proof.add(e)
        
        proof.arrange(DOWN)

        for e in proofs:
            if e != proof1:
                e.align_to(proof1, LEFT)

        proof.next_to(sub4, DOWN)
        proof.align_to(sub4, LEFT)

        for e in proofs:
            self.play(Write(e))
            self.wait(5)
        self.wait(10)

        self.play(y_val.set_value, 3)
        self.wait(5)

        self.play(y_val.set_value, 4,
            rate_func=easeOutBounce)
        self.wait(5)

        self.play(y_val.set_value, 8,
            rate_func=easeOutBounce)
        self.wait(5)

        self.play(y_val.set_value, 6,
            rate_func=easeOutBounce)
        self.wait(15)
