from manim import *
import math

class CoorPolygon(Scene):
    def construct(self):
        """ # 좌표설정을 위함
        for x in range(-8, 8):
            for y in range(-4, 5):
                self.add(Dot(np.array([x, y, 0]), color=DARK_GREY))
        self.add(Dot([0,0,0], color="#FFFFFF"))
        """
        #도입부 
        self.add_sound("4_pythagoras.mp3")
        self.wait(1)
        title = Tex("피타고라스 정리").shift(3*UP+RIGHT)
        pythagoras = MathTex(r"a^2+b^2=c^2").shift(DOWN+RIGHT)
        triangle = Polygon([0,0,0], [0,2.4,0],[1.8,0,0], color="#FF7B54", fill_opacity=1, stroke_width=0)
        text_a = MathTex(r"a").shift([0.9,-0.3,0])
        text_b = MathTex(r"b").shift([-0.2,1.2,0])
        text_c = MathTex(r"c").shift([0.9+0.2,1.2+0.2,0])
        text_abc = VGroup(text_a, text_b, text_c,)
        self.play(
            Write(title),
            FadeIn(pythagoras, shift=DOWN), 
            FadeIn(triangle, shift=DOWN), 
            FadeIn(text_abc, scale=1.5),
            run_time=3, 
        )
        trans_title = Tex("피타고라스 정리의 시각화 증명 IV").scale(0.7)
        trans_title.to_corner(UP + LEFT)
        self.play(
            Transform(title, trans_title),
            LaggedStart(*[FadeOut(obj, shift=DOWN) for obj in pythagoras]),  
            text_abc.animate.move_to([-5.5,0.6,0]),
            triangle.animate.move_to([-5,1.2,0]), run_time=3,
        )
        self.wait(2)
        
        #증명시작
        theta = math.atan(-4/3)
        mtri = triangle.copy().set(color="#227C70")
        self.play(Rotate(mtri, PI-theta), run_time=2,)
        self.play(mtri.animate.move_to([1.5,0.72,0]), run_time=2)
        
        square_a = Polygon([0,0,0], [1.08,1.44,0],[-0.36,2.52,0], [-1.44,1.08,0], color="#A555EC", fill_opacity=1, stroke_width=0)
        square_b = Polygon([3,0,0], [4.44,1.92,0],[2.52,3.36,0], [1.08,1.44,0], color="#A555EC", fill_opacity=1, stroke_width=0)
        square_c = Polygon([0,0,0], [3,0,0],[3,-3,0], [0,-3,0], color="#A555EC", fill_opacity=1, stroke_width=0)
        self.play(GrowFromCenter(square_a), GrowFromCenter(square_b), GrowFromCenter(square_c), run_time=2)
        
        text_a2 = MathTex(r"a^2").shift([square_a.get_center()])
        text_b2 = MathTex(r"b^2").shift([square_b.get_center()])
        text_c2 = MathTex(r"c^2").shift([square_c.get_center()])
        self.play(FadeIn(text_a2),FadeIn(text_b2),FadeIn(text_c2))
        self.play(text_a2.animate.move_to([-6,-1,0]),text_b2.animate.move_to([-5,-1,0]),text_c2.animate.move_to([-4,-1,0]), runt_time=4)
        
        poly_a = Polygon([0,0,0], [1.08,1.44,0],[-0.36,2.52,0], [-1.44,1.08,0], color="#FF6E31", fill_opacity=1, stroke_width=0)
        self.play(FadeIn(poly_a))
        
        hline=Line([1.08,1.44,0],[4.44,1.92,0])
        vline=Line([3,0,0],[2.52,3.36,0])
        self.play(Create(hline))
        self.play(Create(vline))
        
        d=Dot([2.76,1.68,0])
        self.play(Create(d))
        self.play(FadeOut(hline), FadeOut(vline))
        
        line0=Line([1.26,1.68,0],[4.26,1.68,0])
        line1=Line([2.76,3.18,0],[2.76,0.18,0])
        self.play(Create(line0))
        self.play(Create(line1))
        
        poly_c = Polygon([0,0,0], [3,0,0],[3,-3,0], [0,-3,0], color="#FFEBB7", fill_opacity=1, stroke_width=0)
        poly_b0 = Polygon([2.76,1.68,0], [1.26,1.68,0],[1.08,1.44,0], [2.76,0.18,0], color="#243763", fill_opacity=1, stroke_width=0)
        poly_b1 = Polygon([2.76,1.68,0], [2.76,0.18,0],[3,0,0], [4.26,1.68,0], color="#FFB100", fill_opacity=1, stroke_width=0)
        poly_b2 = Polygon([2.76,1.68,0], [4.26,1.68,0],[4.44,1.92,0], [2.76,3.18,0], color="#243763", fill_opacity=1, stroke_width=0)
        poly_b3 = Polygon([2.76,1.68,0], [2.76,3.18,0],[2.52,3.36,0], [1.26,1.68,0], color="#FFB100", fill_opacity=1, stroke_width=0)
        poly_a1 = Polygon([0,0,0], [1.08,1.44,0],[-0.36,2.52,0], [-1.44,1.08,0], color="#FF6E31", fill_opacity=1, stroke_width=0)
        
        self.play(FadeIn(poly_c, poly_b0, poly_b1, poly_b2, poly_b3), run_time=3)
        self.play(FadeOut(line0), FadeOut(line1), FadeOut(d))
        
        self.play(poly_b0.animate.shift([3,0,0]-poly_b0.get_vertices()[0]))
        self.play(poly_b1.animate.shift([0,0,0]-poly_b1.get_vertices()[0]))
        self.play(poly_b2.animate.shift([0,-3,0]-poly_b2.get_vertices()[0]))
        self.play(poly_b3.animate.shift([3,-3,0]-poly_b3.get_vertices()[0]))
        self.play(FadeOut(poly_a),poly_a1.animate.shift(poly_c.get_center()-poly_a.get_center()))
        
        text_plus=MathTex(r"\mathbb{+}").shift([-5.5,-1,0])
        text_equal=MathTex(r"\mathbb{=}").shift([-4.5,-1,0])
        self.play(FadeIn(text_plus, text_equal), run_time=2)
        
        self.wait()
        
        #배경음악 :  Bliss by Luke Bergs | https://soundcloud.com/bergscloud/   
        # Creative Commons - Attribution-ShareAlike 3.0 Unported
        # https://creativecommons.org/licenses/by-sa/3.0/
        # Music promoted by https://www.chosic.com/free-music/all/
        # 참고문헌
        # Roger B. Nelsen, <<Proofs Without Words Exercises in Visual Thinking>>, Lewis and Clark College
        # 아이디어: H. E. Dudeney(1917)