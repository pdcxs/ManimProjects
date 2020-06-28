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

class ParametricTest(Scene):
    def construct(self):
        t = ValueTracker(0)
        def get_rad():
            return np.sin(t.get_value()) + 2

        graph = ParametricFunction(lambda alpha:\
            get_rad() * (\
                np.cos(alpha * TAU) * RIGHT +\
                np.sin(alpha * TAU) * UP))

        def set_func(m):
            m.function = lambda alpha:\
            get_rad() * (\
                np.cos(alpha * TAU) * RIGHT +\
                np.sin(alpha * TAU) * UP)
            m.clear_points()
            m.generate_points()

        graph.add_updater(set_func)

        self.add(graph)
        self.play(t.set_value, 3 * TAU,\
            rate_func=linear,
            run_time = 3)

class LaggedStartTest(Scene):
    def construct(self):
        circles = VGroup()
        for i in range(5):
            c = Circle(radius=0.3)
            c.move_to((i - 2) * RIGHT)
            circles.add(c)
        self.play(LaggedStartMap(
            ShowCreation,
            circles,
            lag_ratio=0.2))

class DoubleDashedArrow(Scene):
    def construct(self):
        a = DashedLine(LEFT * 3, RIGHT * 3)

        tip = a.create_tip(tip_length=0.5, at_start=True)
        tip2 = a.create_tip(tip_length=0.5, at_start=False)
        a.reset_endpoints_based_on_tip(tip, at_start=True)
        a.reset_endpoints_based_on_tip(tip2, at_start=False)
        a.asign_tip_attr(tip, at_start=True)
        a.asign_tip_attr(tip2, at_start=False)
        a.add(tip)
        a.add(tip2)
        self.play(ShowCreation(a))

class TangentLine(Scene):
    def construct(self):
        ellipse = Ellipse()
        ellipse.set_width(5)
        ellipse.set_height(3)
        
        dot = Dot()
        proportion = ValueTracker(0)

        dot.add_updater(lambda m:\
            m.move_to(
                ellipse.point_from_proportion(
                    proportion.get_value()
                )
            ))

        tangent_line = Line()

        def move_tangent_line(line):
            p = proportion.get_value()
            p1 = ellipse.point_from_proportion(
                    p)
            p2 = ellipse.point_from_proportion(
                    (p + 0.001) % 1)
            vec = normalize(p2 - p1)
            line.put_start_and_end_on(
                p1 + vec * FRAME_X_RADIUS,
                p1 - vec * FRAME_X_RADIUS
            )
        
        tangent_line.add_updater(lambda l:\
            move_tangent_line(l))
        
        self.add(tangent_line)
        self.add(ellipse)
        self.add(dot)

        self.play(proportion.set_value, 1,
            rate_func = linear,
            run_time = 5)
        self.wait()

from ManimProjects.utils.rate_functions import *

class EaseTest(Scene):
    def construct(self):
        path = Line(LEFT * 3, RIGHT * 3)
        dot = Dot(path.get_start())

        self.add(path)
        self.add(dot)

        self.play(
            MoveAlongPath(dot, path),
            rate_func=easeOutBounce,
            run_time=2
        )
        self.wait()

        # Because easeOutElastic function will return
        # value greater than 1
        # There has some requirements:
        # 1. Cannot use MoveAlongPath, because points_from_proportion
        #    will crash.
        # 2. Need to remove all the np.clip functions in
        #    manimlib/animation/animation.py, i.e. change
        #    the code of get_sub_alpha and interpolate methods
        #    from `return np.clip((value - lower), 0, 1)`
        #    to `value - lower`
        #    and remove `alpha = np.clip(alpha, 0, 1)`, respectively.`

        self.play(dot.move_to, path.get_start(),
            rate_func=easeOutElastic)
        self.wait()

from ManimProjects.utils.geometry import *

class AngleTest(Scene):
    def construct(self):
        radius = 3
        ang = ValueTracker(0.1)
        p1 = Dot(RIGHT * radius)
        o = Dot()
        p2 = Dot()
        p2.add_updater(lambda m: m.move_to(
            math.cos(ang.get_value()) * radius * RIGHT +
            math.sin(ang.get_value()) * radius * UP))
        
        op1 = Line()
        op2 = Line()
        op1.add_updater(lambda l:\
            l.put_start_and_end_on(
                o.get_center(),
                p1.get_center()
            ))
        op2.add_updater(lambda l:\
            l.put_start_and_end_on(
                o.get_center(),
                p2.get_center()
            ))
        self.add(op1, op2, p1, o, p2)

        angle = Angle(p1, o, p2,
            show_edge=True,
        )
        angle.make_angle_dynamic()
        label = TexMobject('\\alpha').scale(0.65)
        angle.add_label(label)
        angle.set_fill(DARK_BLUE, opacity=0.8)
        self.add(label, angle)

        self.play(ang.set_value, 2*PI-0.1,
            run_time=5,
            rate_func=linear)
        self.wait()

        self.play(ang.set_value, PI/2,)
        self.wait(3)

class Spring():
    def __init__(self, obj1, obj2, length, k):
        self.start = obj1
        self.end = obj2
        self.length = length
        self.k = k
        self.line = Line()
        self.line.add_updater(lambda m:\
            m.put_start_and_end_on(
                obj1.get_center(),
                obj2.get_center())
        )
    
    def get_force(self):
        pos1 = self.start.get_center()
        pos2 = self.end.get_center()
        v = pos2 - pos1
        dist = get_norm(v)
        return normalize(v) * (self.length - dist) * self.k

class MultiSpring(Scene):
    def construct(self):
        def move_ball(ball, dt):
            force = DOWN * 20
            force += ball.spring.get_force()
            ball.velocity += force * dt
            ball.velocity *= 0.95
            ball.shift(ball.velocity * dt)
        
        balls = []
        fix_point = Dot().move_to(UP * FRAME_Y_RADIUS)
        for i in range(4):
            ball = Circle(radius=0.3)
            ball.move_to((3 - i) * UP + random.random() * RIGHT)
            ball.set_fill(RED, opacity=1)

            start = fix_point if i == 0 else balls[i-1]
            end = ball

            spring = Spring(start, end, 1, 40)
            ball.spring = spring
            ball.velocity = 0
            ball.add_updater(move_ball)
            self.add(spring.line)
            self.add(ball)

            balls.append(ball)

        self.wait(10)
        self.play(fix_point.shift, RIGHT * 3)
        self.wait(10)
        self.play(fix_point.shift, LEFT * 6, run_time=2)
        self.wait(15)
