from manim import *


class Point(Scene):
    def construct(self):
        dot_A = Dot()
        self.add(dot_A)
        self.wait(2)
        self.play(dot_A.animate().set_color(BLUE))
        self.wait(2)
