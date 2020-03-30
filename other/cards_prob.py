from manimlib.imports import *
from ManimProjects.utils.geometry import *

class Question(Scene):
    def construct(self):
        sub1 = CText('在很多场景（特别是游戏）中，会碰到一类有趣的问题：')
        sub2 = CText('如果要抽奖N种类型的物品，每次只能抽一个物品')
        sub3 = CText('抽到各个物品的概率相同，每次抽奖相互独立')
        sub4 = CText('问：抽了T次之后得到了所有类型物品的概率是多少？')

        sub4.set_color(RED)
        subs = VGroup(sub1, sub2, sub3, sub4)

        subs.arrange(DOWN, buff=LARGE_BUFF)
        subs.scale(0.5)

        self.play(Write(sub1))
        self.wait(5)
        self.play(Write(sub2))
        self.wait(5)
        self.play(Write(sub3))
        self.wait(5)
        self.play(Write(sub4))
        self.wait(15)

        self.play(FadeOut(subs))
        
class ExampleQuestion(Scene):
    def construct(self):
        sub1 = CText('以卡牌游戏为例')
        sub2 = CText('我们有四种花色的牌：')
        sub1.scale(0.5)
        sub2.scale(0.5)
        sub1.to_edge(UP)
        sub2.next_to(sub1, DOWN)

        self.play(Write(sub1))
        self.play(Write(sub2))
        self.wait(5)

        spade = ImageMobject('spade')
        heart = ImageMobject('heart')
        club  = ImageMobject('club')
        diamond  = ImageMobject('diamond')

        pool = Group(spade, heart, club, diamond)
        pool.arrange(RIGHT, buff=LARGE_BUFF)
        pool.next_to(sub2, DOWN, buff=MED_LARGE_BUFF)

        for c in pool:
            self.play(FadeInFromDown(c))
        sub3 = TexMobject('N=4')
        sub3.scale(0.8)
        sub3.next_to(pool, RIGHT)
        self.play(Write(sub3))
        self.wait(5)

        select = [0, 0, 1, 3, 2, 1, 3]
        cards = [deepcopy(pool[v]) for v in select]

        for i, s in enumerate(select):
            c = cards[i]
            c.move_to(6 * LEFT + 2 * DOWN + 2 * i * RIGHT)
            self.play(TransformFromCopy(pool[s], c))
        
        finish = Group(*cards[0:5])
        box = Rectangle()
        box.set_color(DARK_BROWN)
        box.surround(finish, buff=0)
        box.stretch_to_fit_height(2.1)
        self.play(ShowCreation(box))

        sub4 = TexMobject('T=5')
        sub4.scale(0.8)
        sub4.next_to(box, DOWN)
        self.play(Write(sub4))
        self.wait(10)

class BasicEvent(Scene):
    def construct(self):
        sub1 = CText('先来分析一个基本问题')
        sub1.scale(0.5)
        sub2 = CText('n次抽牌中没有第i种牌的概率')
        sub2.scale(0.5)
        
        sub3_1 = CText('记该事件为').scale(0.5)
        sub3_2 = TexMobject('A_i')
        sub3 = VGroup(sub3_1, sub3_2)
        sub3.arrange(RIGHT)

        sub4 = CText('则易知：')
        sub4.scale(0.5)

        sub5 = TexMobject('P(A_i)=\\left(1-\\frac{1}{N}\\right)^n')
        # sub5.scale(0.8)

        sub1.to_corner(UL, buff=LARGE_BUFF)
        sub2.next_to(sub1, DOWN)
        sub2.align_to(sub1, LEFT)

        sub3.next_to(sub2, DOWN)
        sub3.align_to(sub2, LEFT)

        sub4.next_to(sub3, DOWN)
        sub4.align_to(sub3, LEFT)

        sub5.to_edge(DOWN)
        sub5.shift(UP * 1.5)

        self.play(ShowCreation(sub1))
        self.wait()
        self.play(ShowCreation(sub2))
        self.wait()
        self.play(ShowCreation(sub3))
        self.wait()
        self.play(ShowCreation(sub4))
        self.wait()
        self.play(ShowCreation(sub5))
        self.wait(10)

class InitialAnalyse(Scene):
    def construct(self):
        sub1 = CText('先来分析前n次抽卡没有抽到所有卡牌的概率')
        sub1.scale(0.5)
        sub1.to_corner(UL, buff=LARGE_BUFF)

        sub2 = TexMobject('P\{T>n\}=P\\left(\\bigcup_{i=1}^N A_i\\right)')
        sub2.next_to(sub1, DOWN)
        sub2.align_to(sub1, LEFT)

        sub3 = CText('由容斥原理').scale(0.5)
        sub3.next_to(sub2, RIGHT)

        sub4 = TexMobject(r'\begin{array}{ll}\
            P\{T>n\}= & \displaystyle\sum_{i}P(A_i)-\
            \underset{i_1<i_2}{\sum\sum}\
            P(A_{i_1}A_{i_2})+\cdots\\ \
            & \displaystyle+(-1)^{k+1}\
            \underset{i_1<i_2<\cdots<i_k}{\sum\sum\sum}\
            P(A_{i_1}A_{i_2}\cdots A_{i_k})+\cdots\\ \
            & \displaystyle +(-1)^{N+1}P(A_1A_2\cdots A_N)\
            \end{array}')
        sub4.next_to(sub2, DOWN, buff=LARGE_BUFF)
        sub4.align_to(sub2, LEFT)
        
        self.play(Write(sub1))
        self.wait()
        self.play(Write(sub2))
        self.wait(5)
        self.play(Write(sub3))
        self.wait()
        self.play(Write(sub4), run_time=5)
        self.wait(15)

class JointProb(Scene):
    def construct(self):
        sub1 = CText('由于各个事件是独立的，所以可以得到：')
        sub1.scale(0.5)
        sub1.to_corner(UL, buff=LARGE_BUFF)

        sub2 = TexMobject('P(A_{i_1}A_{i_2}\\cdots A_{i_k})=\
            \left(\\frac{N-k}{N}\\right)^n')
        sub2.to_corner(UP)
        sub2.shift(DOWN * 1.5)

        sub3 = CText('带入前式，得：')
        sub3.scale(0.5)
        sub3.next_to(sub2, DOWN)
        sub3.align_to(sub1, LEFT)

        sub4 = TexMobject(r'P\{T>n\}=\sum_{i=1}^{N-1}\
            \binom{N}{i}\left(\frac{N-i}{N}\
            \right)^n(-1)^{i+1}')
        sub4.to_edge(DOWN)
        sub4.shift(UP)

        note = CText('注：')
        note.scale(0.25)
        sub5 = TexMobject('\\binom{N}{i}=C_{N}^i')
        sub5.scale(0.5)
        sub5.to_corner(DR)
        note.next_to(sub5, LEFT)

        self.play(Write(sub1))
        self.wait(3)
        self.play(Write(sub2))
        self.wait(5)
        self.play(Write(sub3))
        self.wait()
        self.play(Write(sub4))
        self.wait()
        self.play(Write(note),
            Write(sub5))
        self.wait(15)

class Answer(Scene):
    def construct(self):
        sub1 = TexMobject(r'P\{T>n-1\}=P\{T=n\}+P\{T>n\}')
        sub2 = TexMobject(r'P\{T=n\}=P\{T>n-1\}-P\{T>n\}')
        sub3 = CText('化简，得最终答案：')
        sub3.scale(0.5)
        sub4 = TexMobject(r'P\{T=n\}=\sum_{i=1}^{N-1}\
            \frac{i(-1)^{i+1}}{N}\binom{N}{i}\
            \left(\frac{N-i}{N}\right)^{n-1}')
        sub4.scale(1.3)
        
        sub1.to_corner(UL)
        sub2.next_to(sub1, DOWN, buff=LARGE_BUFF)
        sub3.next_to(sub2, DOWN, buff=LARGE_BUFF)
        sub3.align_to(sub2, LEFT)
        sub4.to_edge(DOWN)
        sub4.shift(UP)

        self.play(Write(sub1))
        self.wait(3)
        self.play(Write(sub2))
        self.wait(3)
        self.play(Write(sub3))
        self.wait()
        self.play(Write(sub4))
        self.wait(20)

class Extent(Scene):
    def construct(self):
        sub1 = CText('附加问题：')
        sub2 = CText('抽了n次后，抽到D种类型物品的概率是多少？')
        subs = VGroup(sub1, sub2)
        subs.arrange(DOWN)
        subs.scale(0.5)
        self.play(Write(subs))
        self.wait(10)
        self.play(FadeOut(subs))
