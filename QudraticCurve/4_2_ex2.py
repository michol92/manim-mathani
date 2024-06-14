from manim import *


class Point(Scene):
    def construct(self):
        dot_A = Dot([0, 0, 0], color=RED)
        dot_B = Dot([2, 2, 0], color="#FC6255")
        self.add(dot_A, dot_B)
