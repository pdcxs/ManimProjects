from manimlib.imports import *

class Test(Scene):
    def construct(self):
        text = Text("字体测试", font="Microsoft YaHei")
        self.play(Write(text))
        
class Plot1(GraphScene):
    CONFIG = {
        "y_max" : 50,
        "y_min" : 0,
        "x_max" : 7,
        "x_min" : 0,
        "y_tick_frequency": 5,
        "x_tick_frequency": 0.5,
        "axes_color": BLUE,
        "y_labeled_nums" : range(0, 60, 10),
        "x_labeled_nums" : list(np.arange(2, 7.0+0.5, 0.5)),
        "x_label_decimal": 3,
        "y_label_direction": RIGHT,
        "x_label_direction": UP,
        "y_label_decimal": 3
    }
    def construct(self):
        self.setup_axes(animate=True)
        graph = self.get_graph(lambda  x: x**2,
            color = GREEN,
            x_min = 2,
            x_max = 4)
        lab = self.get_graph_label(graph)
        self.add(lab)
        self.play(ShowCreation(graph), run_time=2)
        self.wait()

class TextTest(Scene):
    def construct(self):
        text1 = Text("这是中文", font="Microsoft YaHei")
        text2 = Text("这是中文", font="Microsoft YaHei", weight=BOLD)
        text3 = Text("这是中文", font="Microsoft YaHei", stroke_width=0)
        group = VGroup(text1, text2, text3)
        text2.next_to(text1, DOWN)
        text3.next_to(text2, DOWN)
        group.shift(-group.get_center())
        self.play(Write(group))

class SquarePoints(Scene):
    def construct(self):
        outerSquare = Square().scale(2)
        innerSquare = Square().scale(0.75).rotate(np.pi/3)
        outerSquare.set_color(PURPLE)
        outerSquare.set_fill(ORANGE, opacity=0.5)
        innerSquare.set_color(BLUE)
        innerSquare.set_fill(ORANGE, opacity=1)

        self.play(ShowCreation(innerSquare), ShowCreation(outerSquare))
        count = 0
        for i, j in zip(outerSquare.points, innerSquare.points):
            self.play(*[ShowCreation(Dot().move_to(e)) for e in [i, j]])
            self.play(*[Write(TexMobject(str(count)).move_to(e)) for e in [i, j]])
            count += 1
        self.wait()

class TwoCircleInter(VMobject):
    def __init__(self, left_down=ORIGIN, radius=1, **kwargs):
        self.top_arc = Arc(PI / 2, PI/2)\
            .move_arc_center_to(ORIGIN + RIGHT * radius)
        self.down_arc = Arc(3 * PI / 2, PI/2)\
            .move_arc_center_to(ORIGIN + UP * radius)
        VMobject.__init__(self, **kwargs)

    def generate_points(self):
        self.append_points(self.top_arc.points)
        self.append_points(self.down_arc.points)

class TwoCircleTest(Scene):
    def construct(self):
        a = TwoCircleInter()
        a.set_fill(LIGHT_BROWN, opacity=1)
        self.play(ShowCreation(a))

class IrregularSector(Arc):
    CONFIG = {
        "inner_radius": 1,
    }

    def generate_points(self):
        self.outter_radius = 2 * self.inner_radius
        inner_arc = Arc(
                start_angle=PI,
                angle=PI/2,
                radius=self.inner_radius,
                arc_center=self.inner_radius * UP + self.inner_radius * RIGHT,
            )
        outer_arc = Arc(
                start_angle=PI,
                angle=PI/2,
                radius=self.outter_radius,
                arc_center=self.outter_radius * UP + self.outter_radius * RIGHT,
            )
        outer_arc.reverse_points()
        self.append_points(inner_arc.points)
        self.add_line_to(outer_arc.points[0])
        self.append_points(outer_arc.points)
        self.add_line_to(inner_arc.points[0])

class IrregularSectorTest(Scene):
    def construct(self):
        shape = IrregularSector()
        shape.set_fill(DARK_BLUE, opacity=1)
        self.play(ShowCreation(shape))
class GetCorner(Scene):
    def construct(self):
        poly = RegularPolygon(5)
        poly.scale(2)
        angle_n = 1
        l1 = Line()
        l1.add_updater(lambda l:
            l.put_start_and_end_on(
                poly.get_vertices()[angle_n - 1],
                poly.get_vertices()[angle_n]
            ))
        l1.set_color(RED)

        l2 = Line()
        l2.add_updater(lambda l:
            l.put_start_and_end_on(
                poly.get_vertices()[angle_n + 1],
                poly.get_vertices()[angle_n]
            ))
        l2.set_color(RED)

        ang = ArcBetweenPoints(LEFT, RIGHT)
        ang.add_updater(lambda a: a.put_start_and_end_on(
            poly.get_vertices()[angle_n] + 0.5 * normalize(
                poly.get_vertices()[angle_n + 1] -\
                poly.get_vertices()[angle_n]),
            poly.get_vertices()[angle_n] + 0.5 * normalize(
                poly.get_vertices()[angle_n - 1] -\
                poly.get_vertices()[angle_n]),
        ))

        self.play(ShowCreation(poly))
        self.play(ShowCreation(l1), ShowCreation(l2))
        self.play(ShowCreation(ang))
        self.play(Rotate(poly, PI))

class MovingCameraTest(MovingCameraScene):
    def construct(self):
        for i in range(500):
            d = Dot()
            x = random.randint(
                -2 * int(FRAME_X_RADIUS),
                2 * int(FRAME_X_RADIUS))
            y = random.randint(
                -2 * int(FRAME_Y_RADIUS),
                2 * int(FRAME_Y_RADIUS))
            d.move_to(x * RIGHT + y * UP)
            self.add(d)
        
        self.play(ApplyMethod(
            self.camera.frame.scale,
            2), run_time=10, rate_func=linear)