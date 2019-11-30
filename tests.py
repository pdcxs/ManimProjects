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
