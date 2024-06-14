from manim import *


class Point_Draw(Scene):
    def construct(self):
        ptA = Dot([0, -0, 0])
        ptB = Dot([3, 2, 0])
        line_AB = Line(ptA, ptB)
        self.add(line_AB)
