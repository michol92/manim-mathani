from manim import *
import math

class Pythagoras(Scene):
    def construct(self):
        self.add_sound("1_Pythagoras.mp3")
        title = Tex("피타고라스 정리").scale(0.7)
        pythagoras = MathTex(r"a^2+b^2=c^2")
        VGroup(title, pythagoras).arrange(DOWN)
        self.play(
            Write(title),
            FadeIn(pythagoras, shift=DOWN), run_time=3, 
        )
        
        transform_title = Tex("피타고라스 정리의 시각화 증명 1").scale(0.7)
        transform_title.to_corner(UP + LEFT)
        self.play(
            Transform(title, transform_title),
            LaggedStart(*[FadeOut(obj, shift=DOWN) for obj in pythagoras]), run_time=2, 
        )
        #self.wait()

        triangle = Polygon(ORIGIN, LEFT, LEFT + 2*UP, color="#FFE15D", fill_opacity=1, stroke_width=0)
        triangle.to_corner(3*UP+3*LEFT)
        self.play(GrowFromCenter(triangle))
        
        text_a = MathTex(r"a")
        text_b = MathTex(r"b")
        text_c = MathTex(r"c")
        text_a.scale(0.7).shift(4*LEFT+1.5*UP)
        text_b.scale(0.7).shift(3.5*LEFT+0.2*UP)
        text_c.scale(0.7).shift(3.1*LEFT+1.5*UP)
        self.play(GrowFromCenter(text_a))
        self.play(GrowFromCenter(text_b))
        self.play(GrowFromCenter(text_c))
        
        square = Square(side_length=3, color="#FFFFFF", fill_opacity=1, stroke_width=0).shift(UP)
        self.play(Create(square), run_time=2)
        
        mtri_1 = triangle.copy().set(color="#F49D1A")
        self.play(FadeIn(mtri_1))
        #self.play(mtri_1.animate.rotate(3/2*PI))
        self.play(Rotate(mtri_1, angle=3/2*PI, rate_func=linear))
        self.play(mtri_1.animate.shift(square.get_vertices()[1]-mtri_1.get_vertices()[1]))
        
        mtri_2 = triangle.copy().set(color="#DC3535")
        self.play(FadeIn(mtri_2))
        #self.play(mtri_1.animate.rotate(0*PI))
        self.play(mtri_2.animate.shift(square.get_vertices()[2]-mtri_2.get_vertices()[1]))
        
        mtri_3 = triangle.copy().set(color="#F49D1A")
        self.play(FadeIn(mtri_3))
        #self.play(mtri_3.animate.rotate(1/2*PI))
        self.play(Rotate(mtri_3, angle=1/2*PI, rate_func=linear))
        self.play(mtri_3.animate.shift(square.get_vertices()[3]-mtri_3.get_vertices()[1]))
        
        mtri_4 = triangle.copy().set(color="#DC3535")
        self.play(FadeIn(mtri_4))
        #self.play(mtri_4.animate.rotate(3.14))
        self.play(Rotate(mtri_4, angle=PI, rate_func=linear))
        self.play(mtri_4.animate.shift(square.get_vertices()[0]-mtri_4.get_vertices()[1]))
        
        dir0=(2*square.get_vertices()[0]+square.get_vertices()[1])/3
        dir1=(2*square.get_vertices()[1]+square.get_vertices()[2])/3
        dir2=(2*square.get_vertices()[2]+square.get_vertices()[3])/3
        dir3=(2*square.get_vertices()[3]+square.get_vertices()[0])/3
        
        square2 = Polygon(dir0, dir1, dir2, dir3, color="#B01E68", fill_opacity=1, stroke_width=0)
        self.play(GrowFromCenter(square2))

        text_c0=text_c.copy().scale(0.7).shift(2.6*RIGHT+0.4*UP)
        text_c1=text_c.copy().scale(0.7).shift(2.2*RIGHT+0.9*DOWN)
        text_c2=text_c.copy().scale(0.7).shift(3.9*RIGHT+0.1*UP)
        text_c3=text_c.copy().scale(0.7).shift(3.5*RIGHT+1.4*DOWN)
        text_cg=Group(text_c0, text_c1, text_c2, text_c3)
        self.play(FadeIn(text_cg))
        
        text_cs=MathTex(r"c^2").scale(0.7).shift(UP)
        self.play(GrowFromCenter(text_cs))
        self.play(FadeOut(text_cg))
        self.play(square2.animate.scale(0.5).move_to(1.5*DOWN+1.5*RIGHT), text_cs.animate.move_to(1.5*DOWN+1.5*RIGHT),run_time=2)
        
        self.play(mtri_2.animate.shift(dir0-dir1))
        self.play(mtri_1.animate.shift(square.get_vertices()[2]-dir1),mtri_3.animate.shift(square.get_vertices()[2]-dir2))       
        
        square3=Square(side_length=4, color="#3C79F5", fill_opacity=1, stroke_width=0).scale(0.5).shift(square.get_vertices()[1]+RIGHT+DOWN)
        square4=Square(side_length=4, color="#3C79F5", fill_opacity=1, stroke_width=0).scale(0.25).shift(square.get_vertices()[3]+0.5*LEFT+0.5*UP)
        self.play(GrowFromCenter(square3), GrowFromCenter(square4), run_time=2)
        
        text_a1=MathTex(r"a").scale(0.5).shift(square3.get_center()+0.8*UP)
        text_a2=MathTex(r"a").scale(0.5).shift(square3.get_center()+0.8*LEFT)
        text_a3=MathTex(r"a").scale(0.5).shift(square3.get_center()+0.8*DOWN)
        text_a4=MathTex(r"a").scale(0.5).shift(square3.get_center()+0.8*RIGHT)
        text_ag=Group(text_a1, text_a2, text_a3, text_a4)        
        text_b1=MathTex(r"b").scale(0.5).shift(square4.get_center()+0.4*UP)
        text_b2=MathTex(r"b").scale(0.5).shift(square4.get_center()+0.4*LEFT)
        text_b3=MathTex(r"b").scale(0.5).shift(square4.get_center()+0.4*DOWN)
        text_b4=MathTex(r"b").scale(0.5).shift(square4.get_center()+0.4*RIGHT)
        text_bg=Group(text_b1, text_b2, text_b3, text_b4)
        self.play(FadeIn(text_ag), FadeIn(text_bg))
        
        text_as=MathTex(r"a^2").scale(0.7).shift(square3.get_center())
        text_bs=MathTex(r"b^2").scale(0.7).shift(square4.get_center())
        self.play(GrowFromCenter(text_as),GrowFromCenter(text_bs))
        self.play(FadeOut(text_ag), FadeOut(text_bg))
        self.play(square3.animate.scale(0.5).move_to(1.5*DOWN+2*LEFT), text_as.animate.move_to(1.5*DOWN+2*LEFT), square4.animate.scale(0.5).move_to(1.5*DOWN+0.3*LEFT), text_bs.animate.move_to(1.5*DOWN+0.3*LEFT), run_time=2)
        text_plus=MathTex(r"\mathbb{+}").scale(0.7).shift(1.5*DOWN+LEFT)
        text_eq=MathTex(r"\mathbb{=}").scale(0.7).shift(1.5*DOWN+0.5*RIGHT)
        self.play(GrowFromCenter(text_plus), GrowFromCenter(text_eq))
        self.play(text_as.animate.move_to(4*LEFT+0.5*DOWN), text_plus.copy().animate.move_to(3.5*LEFT+0.5*DOWN), text_bs.animate.move_to(3*LEFT+0.5*DOWN), text_eq.copy().animate.move_to(2.5*LEFT+0.5*DOWN), text_cs.animate.move_to(2*LEFT+0.5*DOWN), run_time=2)
        self.wait()

# 배경음악
# Feel Good by MusicbyAden | https://soundcloud.com/musicbyaden
# Music promoted by https://www.chosic.com/free-music/all/
# Creative Commons CC BY-SA 3.0
# https://creativecommons.org/licenses/by-sa/3.0/
# 참고자료
# Roger B. Nelsen, <<Proofs Without Words Exercises in Visual Thinking>>, Lewis and Clark College
