from manimlib.imports import *
from random import random

class Plinko(PhysicScene):
    def construct(self):
        self.set_gravity(3 * DOWN)
        
        stc_body = self.space.static_body

        segs = []
        bd_x = FRAME_X_RADIUS - 0.5
        bd_y = FRAME_Y_RADIUS - 0.5
        left = Line(
            bd_x * LEFT + bd_y * UP,
            bd_x * LEFT + bd_y * DOWN)
        right = Line(
            bd_x * RIGHT + bd_y * UP,
            bd_x * RIGHT + bd_y * DOWN)
        bottom = Line(
            bd_x * LEFT + bd_y * DOWN,
            bd_x * RIGHT + bd_y * DOWN
        )
        segs.append(left)
        segs.append(right)
        segs.append(bottom)

        for i in range(-14, 12):
            x = i * 0.5 + 0.4
            seg = Line(x * LEFT + bd_y * DOWN,
                x * LEFT + (bd_y - 1.5) * DOWN )
            segs.append(seg)
        
        start_x = 0

        for i in range(-13, 13):
            for j in range(10):
                pos = i * 0.5 * RIGHT +\
                    j * 0.5 * UP + 1.5 * DOWN
                if j % 2 == 0:
                    pos += 0.25 * RIGHT
                pos += 0.1 * RIGHT
                plk_mobj = Circle(radius = 0.15)
                plk_mobj.set_fill(WHITE, opacity=1)
                plk_mobj.move_to(pos)

                plk_body = pymunk.Body(body_type=pymunk.Body.STATIC)
                plk_body.position = pos[0] * 1000, pos[1] * 1000

                plk_shape = pymunk.Circle(
                    plk_body,
                    plk_mobj.radius * 1000)
                plk_shape.elasticity = 0
                plk_shape.friction = 0
                self.space.add(plk_shape, plk_body)
                self.add(plk_mobj)

                if i == 0 and j == 5:
                    start_x = plk_body.position[0]

        for seg in segs:
            pos_s = seg.points[0]
            pos_e = seg.points[-1]
            seg = pymunk.Segment(
                stc_body,
                (pos_s[0] * 1000, pos_s[1] * 1000),
                (pos_e[0] * 1000, pos_e[1] * 1000),
                0
            )
            seg.friction = 0
            seg.elasticity = 0
            self.space.add(seg)

        for i in range(80):
            mass = 10
            radius = 90
            moment = pymunk.moment_for_circle(mass, 0, radius)
            ball_body = pymunk.Body(mass, moment)
            ball_body.position = (2*random() - 1) + start_x, 4000
            ball_shape = pymunk.Circle(ball_body, radius)
            ball_shape.elasticity = 0
            ball_mobj = Circle(radius = radius / 1000)
            ball_mobj.set_fill(DARK_BLUE, opacity=1)
            ball = PhysicMobject(
                ball_body, ball_shape, ball_mobj)
            ball.set_add_time(i * 0.1)
            self.add_physic_obj(ball)

        self.add(*segs)
        self.simulate(25)

