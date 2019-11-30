from manimlib.imports import *

class Pythagorean(Scene):
    CONFIG={
        "camera_config": {
            "background_color": WHITE,
        }
    }
    def construct(self):
        outerSquare = Square().scale(2)
        innerSquare = Square().scale(0.75).rotate(np.pi/3)
        outerSquare.set_color(PURPLE)
        outerSquare.set_fill(ORANGE, opacity=0.5)
        innerSquare.set_color(BLUE)
        innerSquare.set_fill(ORANGE, opacity=1)

        trgs = []
        for i in range(4):
            p = Polygon(
                innerSquare.points[i * 4 - 1],
                outerSquare.points[((i - 1) % 4) * 4 - 1],
                outerSquare.points[((i + 2) % 4) * 4 - 1])
            p.set_color(BLACK)
            p.set_fill(RED, opacity=1)
            p.round_corners(radius=0.005)
            trgs.append(p)

        first = trgs[0]
        edges = [TexMobject(e).set_color(BLACK) for e in ["a", "b", "c"]]
        edges[0].next_to(first, LEFT).shift([0.5, 0, 0])
        edges[1].next_to(first, RIGHT).shift([-1.5, 0.5, 0])
        edges[2].next_to(first, DOWN)

        self.play(DrawBorderThenFill(first))
        self.play(*[Write(e) for e in edges])
        self.wait()
        self.play(*[FadeOut(e) for e in edges[0:2]])
        self.play(*[ReplacementTransform(first.copy(), t) for t in trgs[1:4]])
        self.play(ShowCreation(innerSquare))

        formula = TexMobject("c^2", "=", "a^2+b^2").set_color(BLACK)
        formula.to_edge(UP)
        
        self.play(ShowCreationThenFadeOut(outerSquare))

        self.play(Transform(edges[2].copy(), formula[0]), Write(formula[1]))

        trig_area = TexMobject("\\frac12 ab").set_color(BLACK)
        trig_area.next_to(outerSquare, LEFT)

        self.play(*[WiggleOutThenIn(t) for t in trgs])
        self.play(Write(trig_area))

        inner_area = TexMobject("(b-a)^2").set_color(BLACK)
        self.play(WiggleOutThenIn(innerSquare))
        self.play(Write(inner_area))

        add_area = TexMobject("4 \\times",
            "\\frac12 ab",
            "+",
            "(b-a)^2").set_color(BLACK)
        add_area.next_to(formula[1], RIGHT, buff=0.2)
        inner_copy = inner_area.copy()
        trig_copy = trig_area.copy()
        self.play(Write(add_area[0]),
            ApplyMethod(trig_copy.move_to, add_area[1].get_center()),
            Write(add_area[2]),
            ApplyMethod(inner_copy.move_to, add_area[3].get_center()))
        self.add(add_area[3])
        self.remove(inner_copy)
        self.add(add_area[1])
        self.remove(trig_copy)
        self.wait()

        simplify = TexMobject("2", "ab", "+", "(b-a)^2").set_color(BLACK)
        simplify.next_to(formula[1], RIGHT, buff=0.2)
        self.play(ReplacementTransform(add_area, simplify))
        self.wait()

        expand = TexMobject("2", "ab", "+", "b^2-2ab+a^2").set_color(BLACK)
        expand.next_to(formula[1], RIGHT, buff=0.2)
        self.play(ReplacementTransform(simplify, expand))
        self.wait()
        self.play(Transform(expand, formula[-1]))
        self.wait()
        