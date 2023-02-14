from manim import *
import math

class CoorPolygon(Scene):
    def construct(self):
        # 좌표설정을 위함
        '''
        for x in range(-8, 8):
            for y in range(-4, 5):
                self.add(Dot(np.array([x, y, 0]), color=DARK_GREY))
        self.add(Dot([0,0,0], color="#FFFFFF"))
        '''
        self.add_sound("5_pythagoras.mp3")
        self.wait(1)
        title = Tex("피타고라스 정리").shift(0.5*UP)
        Text_pythagoras = MathTex(r"a^2+b^2=c^2").shift(0.5*DOWN)
        self.play(Write(title), FadeIn(Text_pythagoras, shift=DOWN), run_time=2)
        trans_title = Tex("피타고라스 정리의 시각화 증명 V").scale(0.7)
        trans_title.to_corner(UP + RIGHT)
        self.play(Transform(title, trans_title),FadeOut(Text_pythagoras, shift=DOWN), run_time=2)
        
        #main triagnle
        main_rtriangle = Polygon([-6,0,0], [-1,0,0],[-4.2,2.4,0], color="#FF7B54", fill_opacity=1, stroke_width=4, stroke_color="#FFFFFF")
        lineBC = Line([-6,0,0],[-1,0,0]).shift(DOWN)
        brace_c = Brace(lineBC)
        theta=math.tan(math.atan2(4,3))
        text_c = brace_c.get_tex(r"c")
        lineCA = Line([-1,0,0],[-4.2,2.4,0]).shift(0.5*RIGHT+0.5*theta*UP)
        brace_b = Brace(lineCA, direction=lineCA.copy().rotate(-PI/2).get_unit_vector())
        text_b = brace_b.get_tex(r"b")
        lineAB = Line([-4.2,2.4,0],[-6,0,0])
        brace_a = Brace(lineAB, direction=lineAB.copy().rotate(-PI/2).get_unit_vector())
        text_a = brace_a.get_tex(r"a")
        tri_group = VGroup(main_rtriangle, brace_a, text_a, brace_b, text_b, brace_c, text_c, DashedLine([-4.2,2.4,0],[-4.2+0.5,2.4+0.5*theta,0]), DashedLine([-1,0,0],[-1+0.5,0.5*theta,0]), DashedLine([-6,0,0],[-6,-1,0]), DashedLine([-1,0,0],[-1,-1,0]))
        self.play(GrowFromCenter(tri_group), run_time=2)
        
        lineDE=Line([-3.13,1.6,0],[-4.33,0,0])
        lineDF=Line([-3.13,1.6,0],[-3.13,0,0])
        self.play(Create(lineDE), Create(lineDF), run_time=2)
                
        # 2nd triangle
        lineCE=Line([-4.33,0,0],[-1,0,0])
        braceCE= Brace(lineCE)
        text_cp= braceCE.get_tex(r"c^\prime")
        #lineDE=Line([-3.13,1.6,0],[-4.33,0,0])
        braceDE= Brace(lineDE, direction=lineDE.copy().rotate(-PI/2).get_unit_vector())
        text_ap= braceDE.get_tex(r"a^\prime")
        lineCD=Line([-1,0,0],[-3.13,1.6,0])
        braceCD= Brace(lineCD, direction=lineCD.copy().rotate(-PI/2).get_unit_vector())
        text_bp= braceCD.get_tex(r"b^\prime")
        tri2_group=VGroup(braceCE, text_cp, braceDE, text_ap, braceCD, text_bp)
        self.play(GrowFromCenter(tri2_group), run_time=2)
        
        braceEF= BraceBetweenPoints([-3.13,0,0], [-4.33,0,0])
        text_ef= braceEF.get_tex(r"x")
        braceFC= BraceBetweenPoints([-1,0,0], [-3.13,0,0])
        text_fc= braceFC.get_tex(r"y")
        triCFD=Polygon([-1,0,0],[-3.13,0,0],[-3.13,1.6,0], color="#8BF5FA", fill_opacity=1, stroke_width=4, stroke_color="#FFFFFF")
        triEFD=Polygon([-4.33,0,0],[-3.13,1.6,0],[-3.13,0,0], color="#EA8FEA", fill_opacity=1, stroke_width=4, stroke_color="#FFFFFF")
        tri3_group = VGroup(triCFD, triEFD, braceEF, text_ef, braceFC, text_fc)
        self.play(FadeIn(tri3_group))
        
        mtri1=main_rtriangle.copy()
        mtri2=triCFD.copy()
        mtri3=triEFD.copy()
        self.play(mtri1.animate.shift([1,0.5,0]-main_rtriangle.get_vertices()[0]))
        
        matrix = [[-1, 0], [0, 1]]
        self.play(ApplyMatrix(matrix, mtri2))
        self.play(Rotate(mtri2, PI/2+math.atan2(4,3)))
        self.play(mtri2.animate.shift([1,-1,0]-mtri2.get_vertices()[2]))
        self.play(ApplyMatrix(matrix, mtri3))
        self.play(Rotate(mtri3, 3*PI/2-math.atan2(3,4)))
        self.play(mtri3.animate.shift([1,-2.5,0]-mtri3.get_vertices()[0]))
        
        self.play(mtri2.animate.shift([0,1.5,0]), mtri3.animate.shift([0,3,0]), run_time=2)
        self.play(mtri2.animate.shift([0,-1.5,0]), mtri3.animate.shift([0,-3,0]), run_time=2)
        
        text_ma=MathTex(r"a").shift([1.7,2,0])
        text_mb=MathTex(r"b").shift([4.5,2,0])
        text_mc=MathTex(r"c").shift([3.5,0.2,0])
        text_mx=MathTex(r"y").shift([3,-0.2,0])
        text_mbp=MathTex(r"b^\prime").shift([2.2,-1.4,0])
        text_my=MathTex(r"x").shift([1.1,-2,0])
        text_map=MathTex(r"a^\prime").shift([2,-2.8,0])
        self.play(FadeIn(text_ma), FadeIn(text_mb), FadeIn(text_mc), FadeIn(text_mx), FadeIn(text_mbp), FadeIn(text_my), FadeIn(text_map))
        
        self.play(FadeOut(tri_group), FadeOut(lineDE), FadeOut(lineDF), FadeOut(tri2_group), FadeOut(tri3_group))
        
        line11=Line(mtri1.get_vertices()[2], mtri1.get_vertices()[1]).set_color(RED)
        line12=Line(mtri1.get_vertices()[1], mtri1.get_vertices()[0]).set_color(RED)
        line21=Line(mtri2.get_vertices()[1], mtri2.get_vertices()[0]).set_color(RED)
        line22=Line(mtri2.get_vertices()[0], mtri2.get_vertices()[2]).set_color(RED)
        self.play(Create(line11), Create(line21))
        self.play(Create(line12), Create(line22))
        
        text1=MathTex(r"b:c=y:b^\prime").shift([-3,1,0])
        self.play(Write(text1))

        self.play(FadeOut(line11), FadeOut(line21), FadeOut(line12), FadeOut(line22))

        line13=Line(mtri1.get_vertices()[2], mtri1.get_vertices()[0]).set_color(RED)
        line14=Line(mtri1.get_vertices()[0], mtri1.get_vertices()[1]).set_color(RED)
        line31=Line(mtri3.get_vertices()[2], mtri3.get_vertices()[0]).set_color(RED)
        line32=Line(mtri3.get_vertices()[0], mtri3.get_vertices()[1]).set_color(RED)      
        self.play(Create(line13), Create(line31))
        self.play(Create(line14), Create(line32))
        
        self.play(FadeOut(line13), FadeOut(line14), FadeOut(line31), FadeOut(line32))
        
        text2=MathTex(r"a:c=x:a^\prime").shift([-3,2,0])
        self.play(Write(text2))
        
        self.play(FadeOut(mtri1), FadeOut(mtri2), FadeOut(mtri3), FadeOut(text_ma), FadeOut(text_mb), FadeOut(text_mc), FadeOut(text_mx), FadeOut(text_my), FadeOut(text_map), FadeOut(text_mbp))
        
        self.play(text1.animate.move_to([3,1,0]), text2.animate.move_to([3,2,0]), FadeIn(tri_group), FadeIn(tri2_group), FadeIn(tri3_group))
        
        text3=MathTex(r"bb^\prime =cy").shift([3,1,0])
        text4=MathTex(r"aa^\prime =cx").shift([3,2,0])
        self.play(Transform(text1,text3), Transform(text2,text4), run_time=2)
        
        text5=MathTex(r"aa^\prime + bb^\prime =").shift([2,0,0])
        text6=MathTex(r"cx+cy").shift([4,0,0])
        self.play(Write(text5))
        self.play(Write(text6))
        
        text7=MathTex(r"c(x+y)").shift([4.5,0,0])
        text8=MathTex(r"cc^\prime").shift([4,0,0])
        self.play(Transform(text6,text7), run_time=2)
        self.play(Transform(text6,text8), run_time=2)
        
        self.play(FadeOut(text1), FadeOut(text2), FadeOut(text3),FadeOut(text4),FadeOut(text5), FadeOut(text6), FadeOut(text8))
        text9=MathTex(r"aa^\prime + bb^\prime = cc^\prime").shift([3,0,0])
        self.play(FadeIn(lineDE), Write(text9))
        text10=MathTex(r"a^2+b^2=c^2").shift([3,0,0])
        
        self.play(FadeOut(tri2_group), FadeOut(tri3_group), FadeIn(lineDE))
        
        
        dot1=Dot([-3.13,1.6,0])
        dot2=Dot([-4.33,0,0])
        mline=Line(dot1.get_center(),dot2.get_center())
        mline.add_updater(lambda z: z.become(Line(dot1.get_center(),dot2.get_center())))
        
        '''
        mlineCD=Line(dot1.get_center(),[-1,0,0])
        mlineCE=Line(dot2.get_center(),[-1,0,0])
        mbraceCD= Brace(mlineCD, direction=mlineCD.copy().rotate(-PI/2).get_unit_vector())
        mtext_ap= mbraceCD.get_tex(r"b^\prime")
        mbraceCE= Brace(mlineCE)
        mtext_bp= mbraceCE.get_tex(r"c^\prime")
        
        tri2_group=VGroup(braceCE, text_cp, braceDE, text_ap, braceCD, text_bp)
        mline=Line(dot1.get_center(),dot2.get_center())
        mbraceDE= Brace(mline, direction=mline.copy().rotate(PI/2).get_unit_vector())
        mtext_ap= mbraceDE.get_tex(r"a^\prime")
        mline.add_updater(lambda z: z.become(Line(dot1.get_center(),dot2.get_center())))
        #mbraceCD.add_updater(lambda z: z.become(Line(dot1.get_center(),[-1,0,0])))
        '''
        dot3=Dot([-4.2,2.4,0])
        dot4=Dot([-6,0,0])
        self.add(dot1, dot2, mline)
        self.play(dot1.animate.shift(dot3.get_center()-dot1.get_center()), dot2.animate.shift(dot4.get_center()-dot2.get_center()), Transform(text9, text10),run_time=2)
        Wait()
        
        #배경음악  Real Estate by LesFM | https://lesfm.net/corporate-background-music/
        # Music promoted by https://www.chosic.com/free-music/all/
        # Creative Commons CC BY 3.0
        # https://creativecommons.org/licenses/by/3.0/

        