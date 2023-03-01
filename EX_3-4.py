from manim import *

class GrowCircle(Scene):
    def construct(self):
        cir = Circle()
        self.play(GrowFromCenter(cir))
        self.wait(1)

class CreateSquare(Scene):
    def construct(self):
        squ = Square()
        self.play(Create(squ))
        self.wait(1)