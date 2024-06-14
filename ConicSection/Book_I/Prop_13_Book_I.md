# I 권

## 명제 13

꼭짓점이 $\rm A$이고 밑변이 원 $\rm BC$인 원뿔이 있다. 원뿔의 축을 포함하는 평면에 의해서 원뿔을 잘라 원뿔곡선인 축 삼각형 $\rm ABC$를 만든다. 그리고 한편으로는 축삼각형의 두 변을 만나고 다른 한편으로는 원뿔의 밑면과 평행하지도 않고 반대방향으로는 확장하지 않은 다른 평면에 의해 원뿔을 잘라 원뿔곡선 $\rm DE$인 단면을 만들자. 원뿔을 자르는 평면과 원뿔 밑면의 공통 직선을 직선 $\rm BC$에 수직인 직선 $\rm FG$라 하고, 원뿔 곡선의 지름을 $\rm ED$라 하자([I권 명제 7, 정의 4]). 점 $\rm E$에서 직선 $\rm ED$에 수직이 직선 $\rm EH$와 점 $\rm A$에서 직선 $\rm ED$에 평행한 직선 $\rm AK$를 그리돼

$$
{\rm AK}^2 : \rm BC \cdot KC=DE : EH
$$

을 만족하도록 하자. 그리고 원뿔곡선 위의 어떤 $\rm L$을 잡자. 점 $\rm L$에서 직선 $\rm FG$에 평행한 직선 $\rm LM$을 그리자.

그러면 $\rm LM^2=EM \cdot XM$이고 직사각형 $\rm EOXM$은 두 변 $\rm EH$, $\rm DE$를 두 변으로 하는 직사각형과 닮음이다.(단, $\rm XM$은 변 $\rm LM$의 일부 길이와 같다.)

## 애플릿

<iframe
src="./GGB_Html/Prop_13_Book_I_Apollonius.html"
width="800"
height="600"
frameborder="0"
framespacing="0"
marginheight="0"
marginwidth="0"
scrolling="no"
vspace="0"></iframe>

## 증명

직선 $\rm DH$를 그리고, 선분 $\rm HE$에 평행하고 한 점 $\rm H$를 지나는 선분 $\rm MXN$을 그리자. 또한 선분 $\rm EM$에 평행하고 점 $\rm H$, 점 $\rm X$에 각각 평행한 두 선분 $\rm HN$, $\rm XO$을 그리자. 직선 $\rm BC$에 평행하고 점 $\rm M$을 지나는 직선 $\rm PMR$을 그리자.

선분 $\rm PR$이 선분 $\rm BC$와 평행하고, 선분 $\rm LM$이 선분 $\rm FG$에 평행하므로, 두 선분 $\rm LM, $ $\rm PR$을 포함하는 평혐은 두 선분 $\rm FG$, $\rm BC$를 포함하는 평면 즉 원뿔의 밑면ㅌ에 평행하다[유클리드 원론 XI권 명제 15]. 만약 두 선분 $\rm LM$, $\rm PR$을 포함하는 평면을 확장한 평면이 원뿔을 자르고 그 단면은 지름이 $\rm PR$인 원이 된다[I권 명제 4].

선분 $\rm LM$은 $\rm PR$과도 수직이다. 그러므로

$$
\rm PM \cdot \rm MR = \rm LM^2.
$$

그리고 가정에 의해서

$$
\rm AK^2 : BK\cdot KC = ED:EH
$$

[유클리드 원론 VI권 명제 23]이며, 그런데

$$
\rm AK:KB=EG:GB=EM:MP
$$

[유클리드 원론 VI권 명제 4]와

$$
\rm AK:KC=DG:GC=DM:MR
$$

[유클리드 원론 VI권 명제 4]이므로

$$
\rm DE: EH=EM\cdot DM:MP\cdot MR
$$

[유클리드 원론 VI권 명제 23].

그러므로

$$
\rm EM\cdot MD:PM\cdot MR=DE:EH=DM:MX
$$

[유클리드 원론 VI권 명제 4].

그리고 선분 $\rm ME$를 공통 높이로 생각하면

$$
\rm DM:MX=DM\cdot ME:XM\cdot ME
$$

[유클리드 원론 VI권 명제 1].

그러므로 역시

$$
\rm DM\cdot ME:PM\cdot MR=DM\cdot ME:XM\cdot ME
$$

[유클리드 원론 V권 명제 11].

그러므로

$$
\rm PM\cdot MR=XM\cdot ME
$$

[유클리드 원론 V권 명제 9].

그런데 식 (1)

$$
\rm PM \cdot \rm MR = \rm LM^2
$$

에 의해서

$$
\rm LM^2=XM \cdot ME.
$$

따라서 선분 $\rm LM$을 한 변으로하는 정사각형 넓이와 선분 $\rm HE$의 일부가 한 변인 평행사변형 $\rm MXOE$의 넓이와 같으며, 평행사변형 $\rm MXOE$은 두 변이 $\rm DE$ , $\rm EH$인 직사각형과 닮음이고 한 변이 선분 $\rm EM$이며 직사각형 $\rm OXNH$를 제고한 직사각형이다(유클리드 원론 VI권 명제 24).

그리고 이러한 단면(원뿔곡선)을 타원(ellipse)이라하고 선분 $\rm EH$는 선분 $\rm DE$에 수직이며 좌표축 처럼 볼수 있다. 선분 $\rm EH$를 세로축 변(upright side)이라고 하고, 선분 $\rm ED$를 가로축 변(transverse side)이라 한다.

<div style="text-align: right"><h5><b>Q.E.D.</b></h5></div>

---
