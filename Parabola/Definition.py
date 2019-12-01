from manimlib.imports import *
from ManimProjects.Parabola.Parabola import Parabola

class OpenScene(Scene):
    def construct(self):
        text1head = Text('高中时期的解析几何都用', font='Microsoft YaHei')
        text1body = Text('坐标系', font='Microsoft YaHei')
        text1tail = Text('进行研究', font='Microsoft YaHei')
        text1 = VGroup(text1head, text1body, text1tail, buff=SMALL_BUFF)
        text1.arrange()
        text1body.set_fill(DARK_BLUE)

        text2 = Text('计算繁杂，且不优雅', font='Microsoft YaHei')
        
        text3head = Text('那么，是否可以用', font='Microsoft YaHei')
        text3body = Text('纯几何', font='Microsoft YaHei')
        text3tail = Text('的方法', font='Microsoft YaHei')
        text3 = VGroup(text3head, text3body, text3tail, buff=SMALL_BUFF)
        text3body.set_fill(DARK_BLUE)
        text3.arrange()

        # text2[1].set_fill(DARK_BLUE)
        text4 = Text('来得到一些圆锥曲线的性质？',
            font='Microsoft YaHei')
        
        group = VGroup(text1, text2, text3, text4)
        group.arrange_submobjects(direction=DOWN, buff=1)
        group.scale(0.5)
        self.play(Write(text1))
        self.play(WiggleOutThenIn(text1body))
        self.wait()
        self.play(Write(text2))
        self.wait()
        self.play(Write(text3))
        self.play(WiggleOutThenIn(text3body))
        self.wait()
        self.play(Write(text4))
        self.wait(2)

        self.play(FadeOut(group))

        explan1 = Text('本系列将试图用几何方法研究圆锥曲线', font='Microsoft YaHei')
        explan2h = Text('主要参考', font='Microsoft YaHei')
        explan2t = Text('《圆锥曲线的几何性质》', font='Microsoft YaHei')
        explan2 = VGroup(explan2h, explan2t)
        explan2.arrange()
        explan2t.set_fill(DARK_BLUE)

        explan3 = Text('希望能有所帮助', font='Microsoft YaHei')

        explan = VGroup(explan1, explan2, explan3)
        explan.arrange_submobjects(direction=DOWN, buff=1)
        explan.scale(0.5)

        self.play(Write(explan1))
        self.wait()
        self.play(Write(explan2))
        self.play(WiggleOutThenIn(explan2t))
        self.wait()
        self.play(Write(explan3))
        self.wait(2)
        self.play(FadeOut(explan))

        jokeh = Text('视频使用', font='Microsoft YaHei')
        jokeb = Text('manim', font='Microsoft YaHei')
        joket = Text('制作', font='Microsoft YaHei')

        jokeb.set_fill(DARK_BLUE)

        joked = Text('边学边做，随缘更新', font='Microsoft YaHei')
        jokeT = VGroup(jokeh, jokeb, joket, buff=SMALL_BUFF)
        jokeT.arrange()

        joke = VGroup(jokeT, joked)
        joke.arrange_submobjects(direction=DOWN, buff=1)

        self.play(Write(jokeT))
        self.play(WiggleOutThenIn(jokeb))
        self.wait()
        self.play(Write(joked))
        self.wait(2)
        self.play(FadeOut(joke))

        last = Text('从抛物线开始', font='Microsoft YaHei')
        self.play(Write(last))
        self.wait()
        self.play(FadeOut(last))

class Definition(Parabola):
    CONFIG = {
        'x_min': -10,
        'focus': 2
    }
    def construct(self):
        self.adjust_x_range()
        lineText = Text('设有一固定直线l', font='Microsoft YaHei')
        directrix = self.get_directrix()
        self.play(Write(lineText))
        self.play(
            ApplyMethod(lineText.scale, 0.3),
            ShowCreation(directrix)
        )
        self.play(
            ApplyMethod(lineText.move_to, self.coords_to_point(-self.focus + 3, self.y_max - 2)),
        )

        self.wait()

        focusText = Text('有一固定点F', font='Microsoft YaHei')
        focus = Circle()\
            .move_to(self.get_focus())\
            .scale(0.1)\
            .set_fill(ORANGE, opacity=1)
        self.play(Write(focusText))
        self.wait()
        self.play(ApplyMethod(focusText.scale, 0.3))
        self.play(
            ApplyMethod(focusText.move_to,
            self.coords_to_point(self.focus+3, 0)),
            ShowCreation(focus)
        )
        self.wait()

        question = Text('求到直线距离l与到\n点P距离相等的点的轨迹', font='Microsoft YaHei')
        question.scale(0.4)
        question.to_edge(RIGHT)
        
        self.play(Write(question))
        self.wait()

        pickPoint = Text('在l上任取一点P', font='Microsoft YaHei')
        pickPoint.scale(0.4)
        pickPoint.to_edge(DOWN)

        self.play(Write(pickPoint))

        y = ValueTracker(5)
        point = Circle()\
            .scale(0.1)\
            .set_fill(ORANGE, opacity=1)\
            .move_to(self.coords_to_point(-self.focus, y.get_value()))
        self.play(ShowCreation(point))

        self.wait()
        self.play(FadeOut(pickPoint))

        connect = Text('连接FP', font='Microsoft YaHei')
        connect.scale((0.4))
        connect.to_edge(DOWN)
        fp = DashedLine(point.get_center(), focus.get_center())

        self.play(Write(connect))
        self.play(ShowCreation(fp))
        self.wait()

        midRight = Text('做FP中垂线', font='Microsoft YaHei')
        midRight.scale(0.4)
        midRight.to_edge(DOWN)
        midPoint = Circle()\
            .scale(0.1)\
            .move_to((point.get_center() + focus.get_center())/2)\
            .set_fill(DARK_BLUE, opacity=1).set_color(DARK_BLUE)
        
        midRightLine = DashedLine(LEFT*FRAME_WIDTH, RIGHT*FRAME_WIDTH)
        midRightLine.rotate(fp.get_angle() + np.pi/2, about_point=midRight.get_center())
        midRightLine.move_to(midPoint.get_center())

        self.play(FadeOut(connect))
        self.play(Write(midRight))
        self.play(ShowCreation(midPoint))
        self.play(ShowCreation(midRightLine))
        self.wait()

        right = Text('过P点做l的垂线', font='Microsoft YaHei')
        right.scale(0.4)
        right.to_edge(DOWN)

        rightLine = DashedLine(LEFT*FRAME_WIDTH, RIGHT*FRAME_WIDTH)
        rightLine.shift(UP * (point.get_center()[1]))

        self.play(FadeOut(midRight))
        self.play(Write(right))
        self.play(ShowCreation(rightLine))

        targetText = Text('垂线与中垂线交点即为曲线上的点', font='Microsoft YaHei')
        targetText.scale(0.4).to_edge(DOWN)
        target = Circle()\
            .scale(0.1)\
            .set_fill(RED, opacity=1)\
            .set_color(ORANGE)\
            .move_to(self.value_to_point(y.get_value()))
            

        self.play(FadeOut(right))
        self.play(Write(targetText))
        self.play(DrawBorderThenFill(target))

        point.add_updater(lambda m: m.move_to(self.coords_to_point(-self.focus, y.get_value())))
        fp.add_updater(lambda m: m.put_start_and_end_on(point.get_center(), focus.get_center()))
        midPoint.add_updater(lambda m: m.move_to((point.get_center() + focus.get_center())/2))
        rightLine.add_updater(lambda m: m.move_to(point.get_center()))
        target.add_updater(lambda m: m.move_to(self.value_to_point(y.get_value())))

        def setRight(line):
            line.put_start_and_end_on(LEFT*FRAME_WIDTH, RIGHT*FRAME_WIDTH)
            line.rotate(fp.get_angle() + np.pi/2, about_point=midRight.get_center())
            line.move_to(midPoint.get_center())
        
        midRightLine.add_updater(setRight)

        self.play(
            ApplyMethod(y.set_value, -2)
        )

        graph = self.get_graph(color=LIGHT_BROWN)
        self.play(
            ApplyMethod(y.set_value, -8),
            ShowCreation(graph)
        )
        self.wait()
        self.play(ApplyMethod(y.set_value, 8, run_time=2))
        self.wait()

        self.play(ApplyMethod(y.set_value, 2, run_time=2))

        directDef = Text('直线l称为准线', font='Microsoft YaHei')
        directDef.scale(0.4)
        directDef.to_edge(DOWN)

        dire = Text('准线', font='Microsoft YaHei')
        dire.scale(0.3).move_to(lineText.get_center())
        dire.align_to(lineText, LEFT)

        self.play(FadeOut(targetText))
        self.play(Write(directDef))
        self.play(Transform(lineText, dire))

        self.wait()
        self.play(FadeOut(directDef))

        focDef = Text('点F称为焦点', font='Microsoft YaHei')
        focDef.scale(0.4).to_edge(DOWN)
        foc = Text('焦点', font='Microsoft YaHei')
        foc.scale(0.3).move_to(focusText.get_center())\
            .align_to(focusText, LEFT)

        self.play(Write(focDef))
        self.play(Transform(focusText, foc))
        self.wait(3)

        self.play(ShowCreation(self.get_horizontal()))
        self.play(Write(Text('轴', font='Microsoft YaHei')\
            .scale(0.3).move_to(self.coords_to_point(5, 0.5))))
        self.play(ShowCreation(
            Circle()\
                .scale(0.1)\
                .set_color(DARK_BLUE)\
                .set_fill(DARK_BLUE, opacity=1)\
                .move_to(self.coords_to_point(0, 0))
        ))
        self.play(Write(Text('顶点', font='Microsoft YaHei')\
            .scale(0.3).move_to(self.coords_to_point(0.5, 0.5))))
        self.wait(3)