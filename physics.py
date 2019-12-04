from manimlib.imports import *
import pymunk

class PhysicsBody(Animation):
    CONFIG = {
        "rate_func" : linear
    }

    def __init__(self, mobject, pos_and_rot, **kwargs):
        self.run_nums = len(pos_and_rot) - 1
        self.pos_and_rot = pos_and_rot
        self.angle = pos_and_rot[0][1]
        mobject.rotate(self.angle)
        super().__init__(mobject, **kwargs)

    def interpolate_mobject(self, alpha):
        pos, rot = self.pos_and_rot[int(self.run_nums * alpha)]
        x, y = pos
        self.mobject.move_to(np.array([x, y, 0]))
        self.mobject.rotate(rot - self.angle)
        self.angle = rot

class PhysicTest(Scene):
    def construct(self):
        space = pymunk.Space()
        space.gravity = 0,-9820

        ground = space.static_body
        grd_seg = pymunk.Segment(ground, (-10000, -2000), (10000, -2000), 0)
        grd_seg.friction = 0.8
        space.add(grd_seg)
        #space.add(ground, grd_box)

        mass = 10
        size=(1000,1000)
        moment = pymunk.moment_for_box(mass, size)
        body = pymunk.Body(mass, moment)
        body.angle = 0.1
        body.position = 0, 3000
        
        box = pymunk.Poly.create_box(body, size)
        box.elasticity = 0
        box.friction = 0.5
        space.add(body, box)
        
        shape = Square()
        shape.stretch_to_fit_height(1)
        shape.stretch_to_fit_width(1)

        body2 = pymunk.Body(mass, moment)
        body2.angle = -0.1
        body2.position = 800, 4500
        
        box2 = pymunk.Poly.create_box(body2, size)
        box2.elasticity = 0
        box2.friction = 0.5
        space.add(body2, box2)
        
        shape = Square()
        shape.stretch_to_fit_height(1)
        shape.stretch_to_fit_width(1)
        shape.set_fill(DARK_BLUE, opacity=1)

        shape2 = Square()
        shape2.stretch_to_fit_height(1)
        shape2.stretch_to_fit_width(1)
        shape2.set_fill(DARK_BROWN, opacity=1)

        self.add(shape)
        self.add(shape2)
        self.add(Line(FRAME_X_RADIUS * LEFT, FRAME_X_RADIUS * RIGHT).shift(2 * DOWN))

        run_time = 5
        last_t = 0
        shape_cons = []
        shape2_cons = []
        step = 1 / self.camera.frame_rate
        for t in range(int(run_time / step)):
            space.step(step)
            shape_cons.append((body.position/1000, body.angle))
            shape2_cons.append((body2.position/1000, body2.angle))

        self.play(PhysicsBody(shape, shape_cons),
            PhysicsBody(shape2, shape2_cons),
            run_time=run_time)
