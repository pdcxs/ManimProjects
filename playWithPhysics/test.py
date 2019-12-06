# to run this code, you need to use the brach:
# https://github.com/pdcxs/manim/tree/physics
from manimlib.imports import *

class FuncSurface(PhysicScene):
    def construct(self):
        form = TexMobject('y=\\frac{x^2}{6}')
        form.to_corner(RIGHT+DOWN)

        self.set_gravity(9.8 * DOWN)

        def func(alpha):
            x = interpolate(-FRAME_X_RADIUS, FRAME_X_RADIUS, alpha)
            y = x ** 2 / 6 - 2
            return x * RIGHT + y * UP

        grd_shape = ParametricFunction(func)

        grd_body = self.space.static_body

        pnts = grd_shape.points
        for i in range(len(pnts) - 1):
            x1 = pnts[i][0] * 1000
            y1 = pnts[i][1] * 1000
            x2 = pnts[i + 1][0] * 1000
            y2 = pnts[i + 1][1] * 1000
            grd_seg = pymunk.Segment(grd_body,
                (x1, y1),
                (x2, y2), 0)
            grd_seg.friction = 0.7
            grd_seg.elasticity = 0.8
            self.space.add(grd_seg)

        for i in range(30):
            mass = 10
            pos = (i * 300 - 5000), 4000
            if i % 2 == 0:
                size=(500, 500)
                moment = pymunk.moment_for_box(mass, size)
                body = pymunk.Body(mass, moment)
                body.angle = i * 0.1
                body.position = pos
                shape = pymunk.Poly.create_box(body, size)
                shape.friction = 0.5

                mobj = Square()
                mobj.stretch_to_fit_height(0.5)
                mobj.stretch_to_fit_width(0.5)
                mobj.set_fill(DARK_BLUE, opacity=1)
            else:
                radius = 0.5
                mobj = Circle(radius=radius)
                mobj.set_fill(DARK_BROWN, opacity=1)

                moment = pymunk.moment_for_circle(
                    mass, 0, radius * 1000)
                body = pymunk.Body(mass, moment)
                body.position = pos
                shape = pymunk.Circle(body, radius * 1099)
                shape.elasticity = 0.8

            pmobj = PhysicMobject(body, shape, mobj)
            pmobj.set_add_time(i * 0.5)

            self.add_physic_obj(pmobj)

        self.play(ShowCreation(grd_shape), Write(form))
        self.simulate(20)
    