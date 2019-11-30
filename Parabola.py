from manimlib.imports import *

class Parabola(Scene):
    CONFIG = {
        'focus': 1,
        'y_max': 10,
        'x_min': -2,
        'color': WHITE
    }

    def adjust_x_range(self):
        self.y_min = -self.y_max
        self.x_max = 2 * self.y_max / FRAME_HEIGHT * FRAME_WIDTH + self.x_min

    def get_graph(self, color=WHITE):
        f = self.focus
        func = lambda y: y ** 2 / (4 * f)

        def parameterized_function(alpha):
            y = interpolate(self.y_min, self.y_max, alpha)
            x = func(y)
            return self.coords_to_point(x, y)
        
        self.graph = ParametricFunction(
            parameterized_function,
            color = color
        )
        return self.graph

    def get_horizontal(self):
        return Line(FRAME_X_RADIUS * LEFT, FRAME_X_RADIUS * RIGHT)

    def get_focus(self):
        return self.coords_to_point(self.focus, 0)

    def get_directrix(self):
        f = self.coords_to_point(-self.focus, 0)
        return Line(
            f + FRAME_Y_RADIUS * UP,
            f + FRAME_Y_RADIUS * DOWN)

    def map(self, val, from_min, from_max, to_min, to_max):
        return (val - from_min) / (from_max - from_min) * (to_max - to_min) + to_min

    def coords_to_point(self, x, y):
        to_x = self.map(x, self.x_min, self.x_max,
            -FRAME_X_RADIUS, FRAME_X_RADIUS)
        to_y = self.map(y, self.y_min, self.y_max,
            -FRAME_Y_RADIUS, FRAME_Y_RADIUS)
        return to_x * RIGHT + to_y * UP


class ParabolaTest(Parabola):
    CONFIG = {
        'x_min': -10
    }
    def construct(self):
        self.adjust_x_range()
        directrix = self.get_directrix()
        graph = self.get_graph()
        focus = Circle()\
            .move_to(self.get_focus())\
            .scale(0.1)
        focus.set_color(ORANGE)
        focus.set_fill(ORANGE, opacity=1)
        self.play(
            ShowCreation(directrix),
            ShowCreation(self.get_horizontal()),
            DrawBorderThenFill(focus))
        self.play(ShowCreation(graph))

        self.focus = 5
        dir2 = self.get_directrix()
        graph2 = self.get_graph()
        foc2 = Circle()\
            .move_to(self.get_focus())\
            .scale(0.1)
        foc2.set_color(ORANGE)
        foc2.set_fill(ORANGE, opacity=1)
        self.play(Transform(directrix, dir2),
            Transform(focus, foc2),
            Transform(graph, graph2))

