# I 권

## 명제 12

꼭짓점이 $\rm A$이고 밑변이 원 $\rm BC$인 원뿔이 있다. 원뿔의 축을 포함하는 평면에 의해서 원뿔을 잘라 원뿔곡선인 축 삼각형 $\rm ABC$를 만든다[I권 명제 3]. 다른 평면으로 원뿔 밑면을 잘라 만들어진 선분을 $\rm DE$라 하고 축 삼각형 밑변 $\rm BC$와 수직이되게하자. 같은 평면으로 원뿔의 옆면을 잘려진 곡선을 $\rm DFE$라 하고 이 곡선의 지름을 $\rm FG$라 하자[I권 명제 7, 정의 4]. 또한 반직선 $\rm FG$와 축 삼각형 $\rm ABC$의 반직선 $\rm CA$와 원뿔의 꼭짓점 $\rm A$를 넘어서의 교점을 $\rm H$라 하자. 점 $\rm A$를 지나며 지름 $\rm FG$와 평행한 직선을 $\rm AK$이라 하자(단, 점 $\rm K$는 선분 $\rm BC$ 위의 점이다). 선분 $\rm FL$은 점 $\rm F$에서 선분 $\rm FG$와 수직이며

$$
{\rm KA}^2 : \rm BK \cdot KC = FH:FL
$$

을 만족한다. 점 $\rm M$은 원뿔곡선 $\rm DFE$ 위의 어떤 점이라 하자. 점 $\rm M$을 지나며 선분 $\rm DE$에 평행한 선분 $\rm MN$을 그리자. 그리고 점 $\rm N$을 지나며 선분 $\rm FL$에 평행한 선분 $\rm NOX$를 그리자. 선분 $\rm HL$을 그려 확장시키면 점 $\rm X$가 그 직선 위에 있다. 두 선분 $\rm LO$, $\rm XP$를 각각 점 $\rm L$, $\rm X$를 지나고 선분 $\rm XP$​에 평행하게 그리자.

그러면 $\rm MN^2$은 두 변이 $\rm FL$, $\rm FN$인 직사각형 $\rm FLON$과 두 변이 $\rm FH$, $\rm FL$인 직사각형 $\rm FHYL$과 대각선 쪽 너머에 있는 닮음인 직사각형 $\rm LPXO$를 합친 평행사변형 $\rm FPXN$의 넓이의 제곱과 같다.

## 애플릿

<iframe
src="/Book_I/GGB_Html/Prop_12_Book_I_Apollonius.html"
width="800"
height="600"
frameborder="0"
framespacing="0"
marginheight="0"
marginwidth="0"
scrolling="no"
vspace="0"></iframe>

## 증명

점 $\rm N$을 지나고 선분 $\rm BC$에 평행한 선분 $\rm RNS$를 그리자. 선분 $\rm NM$ 역시 $\rm DE$에 평행하다. 그러므로 두 선분 $\rm MN$, $\rm RS$는 두 선분 $\rm BC$, $\rm DE$를 포함하는 평면 즉, 원뿔의 밑면에 평행하다[유클리드 XI권 명제 15]. 그러므로 두 선분 $\rm MN$, $\rm RS$를 포함하는 평면과 원뿔과의 교선은 선분 $\rm RNS$를 지름으로 하는 원이다[I권 명제 4]. 그리고 선분 $\rm MN$은 지름 $\rm RNS$에 수직이다.

그러므로

$$
\rm RN \cdot NS = MN^2
$$

그리고

$$
\rm AK^2 : BK \cdot KC=FH:FL
$$

이고

$$
\rm AK^2 : BK\cdot KC = AK\cdot AK :KC\cdot KB
$$

[유클리드 원론 VI권 명제 23]이기 때문에 그러므로 역시

$$
\rm FH:FL=AK\cdot AK:KC\cdot KB
$$

그러나

$$
\rm AK:KC=HG:GC=HN:NS
$$

[유클리드 원론 VI권 명제 4]이고

$$
\rm AK:KB=FG:GB=FN:NR
$$

그러므로

$$
\rm HF:FL=HN\cdot FN:NS\cdot NR
$$

그리고

$$
\rm HN\cdot NF:SN\cdot NR=HN \cdot FN: NS\cdot NR
$$

[유클리드 원론 VI권 명제 23].

그러므로 게다가

$$
\rm HN\cdot NF:SN\cdot NR=HF:FL=HN:NX
$$

[유클리드 원론 VI권 명제 4].

그러나 선분 $\rm FN$은 공통 높이 처럼 생각할 수 있기 때문에

$$
\rm HN:NX = HN\cdot NF:FN\cdot NX
$$

[유클리드 원론 VI권 명제 1].

그러므로

$$
\rm HN\cdot NF:SN\cdot NR=HN\cdot NF:XN\cdot NF
$$

[유클리드 원론 V권 명제 11].

따라서

$$
\rm SN\cdot NR=XN\cdot NF
$$

[유클리드 원론 V권 명제 9].

그런데

$$
\rm MN^2=SN\cdot NR
$$

이므로

$$
\rm MN^2 = XN\cdot NF
$$

따라서 $[\rm FPXN]=XN\cdot NF$이므로 두 변 $\rm XN$, $\rm NF$인 평행사변형 $\rm FPXN$의 넓이와 같다. 그러므로 직사각형 $\rm FPXN$의 넓이와 같은 정사각형의 한 변의 길이가 $\rm MN$이다. 평행사변형 $\rm FPXN$은 두 변이 $\rm FL$, $\rm FN$인 직사각형 $\rm FLON$과 두 변이 $\rm FH$, $\rm FL$인 직사각형 $\rm FHYL$과 대각선 쪽 너머에 있는 닮음인 직사각형 $\rm LPXO$를 합친것이다[유클리드 원론 VI권 명제 24].

이러한 원뿔곡선 $\rm DFE$를 **쌍곡선**이라 한다. 선분$\rm LF$은 선분 $\rm FG$에 수직이며 좌표축처럼 볼수 있다. 이때 선분 $\rm LF$를 **세로축 변(upright side)**이라 하고, 선분 $\rm FH$를 **가로축 변(transverse side)**이라 한다.

<div style="text-align: right"><h5><b>Q.E.D.</b></h5></div>

---
