from manimlib.imports import *
from ManimProjects.utils.Parabola import Parabola
from ManimProjects.utils.geometry import CText

class OpenScene(Scene):
    def construct(self):
        sub1 = CText('这将是一个')
        sub2 = CText('关于线段长度的性质')
        subs = VGroup(sub1, sub2)
        subs.arrange(DOWN)
        self.play(Write(sub1))
        self.play(Write(sub2))
        self.wait(2)
        self.play(FadeOut(subs))
    
class Prop2(Parabola):
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

        h_line = Line()
        d_loc = directrix.get_center()[0] * RIGHT
        h_line.put_start_and_end_on(d_loc, ORIGIN)
        h_line.plot_depth = -1
        self.play(ShowCreation(h_line))

        a = Dot()
        a.set_fill(LIGHT_BROWN)
        a.plot_depth = 1
        a.move_to(self.coords_to_point(0, 0))
        
        a_label = TexMobject('A').scale(0.5)
        a_label.next_to(a, DL, buff=SMALL_BUFF)

        t = Dot()
        t.set_fill(LIGHT_BROWN)
        t.plot_depth = 1
        t.move_to(d_loc)

        t_label = TexMobject('T').scale(0.5)
        t_label.next_to(t, LEFT, buff=SMALL_BUFF)
        
        y_value = ValueTracker(9)
        p = Dot()
        p.set_fill(DARK_BLUE)
        p.plot_depth = 1

        p.add_updater(lambda m:\
            m.move_to(self.value_to_point(
                y_value.get_value())))
        p_label = TexMobject('P').scale(0.5)
        p_label.add_updater(lambda m:\
            m.next_to(p, RIGHT, buff=SMALL_BUFF))
        
        m = Dot()
        m.set_fill(DARK_BLUE)
        m.plot_depth = 1
        m.add_updater(lambda t:\
            t.move_to(d_loc + p.get_center()[1] * UP))
        m_label = TexMobject('M').scale(0.5)
        m_label.add_updater(lambda l:\
            l.next_to(m, LEFT, buff=SMALL_BUFF))
        
        n = Dot()
        n.set_fill(DARK_BLUE)
        n.plot_depth = 1
        n.add_updater(lambda m:\
            m.move_to(p.get_center()[0] * RIGHT))

        n_label = TexMobject('N').scale(0.5)
        n_label.add_updater(lambda m:\
            m.next_to(n, DOWN, buff=SMALL_BUFF))
        
        self.play(*[ShowCreation(e) for e in\
            [a, p, m, n, t]])

        self.play(*[ShowCreation(e) for e in\
            [a_label, t_label, p_label, m_label, n_label]])
        self.wait()

        pn = Line()
        pn.add_updater(lambda l:\
            l.put_start_and_end_on(
                p.get_center(), n.get_center()))
        pf = Line()
        pf.add_updater(lambda l:\
            l.put_start_and_end_on(
                p.get_center(), focus.get_center()))

        pm = Line()
        pm.add_updater(lambda l:\
            l.put_start_and_end_on(
                p.get_center(), m.get_center()))
        self.play(*[ShowCreation(e) for e in\
            [pn, pf, pm]])
        self.wait()

        prop = VGroup()
        prop.add(CText('性质：')\
            .scale(0.25).set_color(DARK_BLUE))
        prop.add(TexMobject('PN^2=4AF\\cdot AN')\
            .scale(0.5)).set_color(DARK_BROWN)
        prop.arrange(RIGHT)

        proof = VGroup()
        prf = CText('证明：')\
            .scale(0.25).set_color(DARK_BLUE)
        proof.add(prf)

        details = VGroup()
        line1 = TexMobject('TN^2=', '(TA+AN)^2')\
            .scale(0.5)
        details.add(line1)

        line2 = TexMobject('TN^2=PM^2=PF^2')\
            .scale(0.5)
        details.add(line2)

        line3 = TexMobject('PF^2=PN^2+NF^2')\
            .scale(0.5)
        details.add(line3)

        line4 = TexMobject(
            'PN^2+NF^2=NF^2+4 AF\\cdot AN')\
            .scale(0.5)
        details.add(line4)

        
        line5 = TexMobject(
            'PN^2=4AF\\cdot AN'
        ).scale(0.5).set_color(DARK_BROWN)
        details.add(line5)

        proof.add(details)
        details.arrange(DOWN)

        line2.align_to(line1, LEFT)
        line3.align_to(line2, LEFT)
        line4.align_to(line3, LEFT)
        line5.align_to(line4, LEFT)

        proof.arrange(RIGHT)
        prf.align_to(details, UP)

        forms = VGroup()
        forms.add(prop)
        forms.add(proof)
        forms.arrange(DOWN)
        proof.align_to(prop, LEFT)
        forms.to_edge(RIGHT, buff=2)

        expand = TexMobject('TA',
            '^2+AN^2+2', 'TA',
            '\\cdot AN')\
            .scale(0.5)
        expand.align_to(line1[1], LEFT)
        expand.align_to(line1[1], UP)

        expand2 = TexMobject('AF',
            '^2+AN^2+2', 'AF',
            '\\cdot AN')\
            .scale(0.5)
        expand2.align_to(line1[1], LEFT)
        expand2.align_to(line1[1], UP)

        expand3 = TexMobject(
            '(AF-AN)^2+4 AF\\cdot AN')\
            .scale(0.5)
        expand3.align_to(line1[1], LEFT)
        expand3.align_to(line1[1], UP)

        expand4 = TexMobject(
            'NF^2+4 AF\\cdot AN'
        ).scale(0.5)
        expand4.align_to(line1[1], LEFT)
        expand4.align_to(line1[1], UP)

        self.play(Write(prop))
        self.wait()

        self.play(y_value.set_value, 1)
        self.wait()
        self.play(y_value.set_value, 3)
        self.wait()

        self.play(Write(prf))
        self.play(Write(line1))
        self.wait()

        self.play(ShowCreationThenDestruction(
            Line(t, n).set_color(RED)
        ))
        self.play(ShowCreationThenDestruction(
            Line(t, a).set_color(RED)
        ))
        self.play(ShowCreationThenDestruction(
            Line(a, n).set_color(RED)
        ))
        self.wait()

        self.play(ReplacementTransform(
            line1[1], expand
        ))
        self.wait(3)

        self.play(ShowCreationThenDestruction(
            Line(t, a).set_color(RED)
        ))
        self.play(ShowCreationThenDestruction(
            Line(a, focus).set_color(RED)
        ))
        self.wait()
        self.play(*[Transform(
            expand[e], expand2[e]) for e in\
            [0, 2]])
        self.wait(3)

        self.play(ReplacementTransform(
            expand, expand3
        ))
        self.wait(3)
        self.play(ReplacementTransform(
            expand3, expand4
        ))
        self.wait(3)

        self.play(Write(line2))
        self.play(ShowCreationThenDestruction(
            Line(t, n).set_color(RED)
        ))
        self.play(ShowCreationThenDestruction(
            Line(p, m).set_color(RED)
        ))
        self.play(ShowCreationThenDestruction(
            Line(p, focus).set_color(RED)
        ))
        self.wait(3)

        self.play(Write(line3))
        self.play(ShowCreationThenDestruction(Polygon(
            p.get_center(),
            n.get_center(),
            focus.get_center()
        ).set_fill(DARK_BLUE, opacity=1)))
        self.wait(3)

        self.play(
            WiggleOutThenIn(expand4),
            WiggleOutThenIn(line3))

        self.play(Write(line4))
        self.wait(3)
        self.play(Write(line5))
        self.wait(3)

        def1 = CText('AF是焦距')
        def2 = CText('AN是点P的横标线')
        def3 = CText('PN是点P的纵标线')
        defines = VGroup(def1, def2, def3)
        defines.arrange(DOWN)
        defines.scale(0.25)
        defines.next_to(proof, DOWN)

        self.play(Write(defines))
        self.wait(5)

        self.play(y_value.set_value, 8)
        self.wait(10)

class Summary(Scene):
    def construct(self):
        text = CText('总结')
        text.set_fill(DARK_BROWN)

        content1 = CText('纵标线的平方等于')
        content2 = CText('横标线与焦距乘积的四倍')
        contents = VGroup(content1, content2)
        contents.scale(0.7)
        contents.arrange(DOWN)

        total = VGroup(text, contents)
        total.arrange(DOWN, buff=MED_LARGE_BUFF)

        self.play(Write(text))
        self.wait(2)
        self.play(Write(contents))
        self.wait(10)