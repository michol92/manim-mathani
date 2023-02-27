from manim import *

class CreateCircle(Scene):
    def construct(self):
        cir = Circle() 
        self.play(GrowFromCenter(cir))