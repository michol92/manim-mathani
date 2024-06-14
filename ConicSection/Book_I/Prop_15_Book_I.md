# I 권

## 명제 15

주어지 타원의 지름이 $\rm AB$이고 지름 $\rm AB$의 중점을 $\rm C$라 하고, 점 $\rm C$를 지나고 지름에 수직인 선분 $\rm DCE$를 그리자. 점 $\rm D$에서 선분 $\rm DE$에 수직이면서

$$
\rm DE:AB=AB:DF
$$

을 만족한다. 타원 위의 어떤 점 $\rm G$를 지나고 지름 $\rm AB$에 평행한 선분 $\rm GHW$를 그리고, 선분 $\rm EF$를 그리자. 점 $\rm H$를 지나고 선분 $\rm DF$에 평행한 선분 $\rm HL$을 그리자. 두 점 $\rm F$, $\rm L$을 각각 지나고 선분 $\rm HD$에 팽행한 선분을 각각 $\rm FK$, $\rm LM$이라 하자.

그러면 선분 $\rm GH^2$는 두 선분 $\rm DF$, $\rm DH$를 두 변으로 하는 직사각형에서 두 변이 $\rm ED$, $\rm DF$인 직사각형과 닮음은 직사각형 $\rm LMFK$를 뺀 직사각형 $\rm DHLM$의 넓이와 같다. 즉, [^1]

$$
\rm GH^2 = \it area\rm [DHKF]-\it area\rm[LKFM]=DH\cdot HL
$$

## 애플릿

<iframe
src="./GGB_Html/Prop_15_Book_I_Apollonius.html"
width="800"
height="600"
frameborder="0"
framespacing="0"
marginheight="0"
marginwidth="0"
scrolling="no"
vspace="0"></iframe>

## 증명

선분 $\rm AN$을 평행한 선분 $\rm AB$의 매개변수라하자. 선분 $\rm BN$을 그리고, 점 $\rm G$를 지나며 선분 $\rm DE$에 평행한 선분 $\rm GX$를 그리자. 또한 점 $\rm X$, $\rm C$를 각각 지나며 선분 $\rm AN$에 평행한 선분 $\rm XO$, $\rm CP$를 그리자. 그리고 점 $\rm N$, $\rm O$, $\rm P$를 각각 지나며 선분 $\rm AB$에 평행한 선분 $\rm NU$, $\rm OS$, $\rm TP$를 그리자.

그러면

$$
\rm DC^2 = \it area\rm[ATPC]
$$

$$
\rm GX^2 = \it area \rm[AA^\prime OX]
$$

[I. 명제 13].

그러면

$$
\rm BA:AN=BC:CP=PT:TN
$$

[유클리드 원론 VI권 명제 4]이고,

$$
\rm BC=CA=TP
$$

이며,

$$
\rm CP=TA
$$

이므로

$$
area\rm[ATPC]=\it area\rm[TNRP]
$$

이고

$$
area\rm[XB^\prime TA]=\it area\rm[TNUB^\prime].
$$

또한

$$
area\rm[OA^\prime TB^\prime]=\it area\rm[OURS]
$$

[유클리드 원론 I권 명제 43] 이고 선분 $\rm NO$가 공통이므로

$$
area\rm[TNUB^\prime]=\it area\rm[NRSA^\prime].
$$

그러나

$$
area\rm[TNUB^\prime]=\it area\rm[TB^\prime XA]
$$

이고 선분 $\rm TX$가 공통이다. 그러므로

$$
area\rm[NRPT]=\it area\rm [PCAT]=\it area\rm[AA^\prime OX] + \it area\rm[PB^\prime OS]
$$

이며 또한

$$
area\rm[PCAT]-\it area\rm[AA^\prime OX]=\it area\rm[PB^\prime OS].
$$

역시

$$
area\rm[ATPC]=CD^2 \,,\it area\rm[AA^\prime OB^\prime]=XG^2
$$

이고

$$
area\rm[OSPB^\prime]=OS \cdot SP.
$$

그러므로

$$
\rm CD^2 - GX^2 = OS\cdot SP.
$$

역시 선분 $\rm DE$는 점 $\rm C$에 의해서 길이가 같은 두 선분으로 나누어지며, 선분 $\rm DE$ 위의 한 점을 $\rm H$라 하면

$$
\rm EH \cdot HD + CH^2 = CD^2
$$

[유클리드 원론 II권 명제 5] 또는

$$
\rm EH\cdot HD + XG^2 = CD^2.
$$

그러므로

$$
\rm CD^2 - XG^2 = EH\cdot HD
$$

그러나

$$
\rm CD^2-XG^2 = OS \cdot SP
$$

이고 그래서

$$
\rm EH\cdot HD = OS\cdot SP.
$$

그리고

$$
\rm DE:AB=AB:DF
$$

이므로

$$
\rm DE-DF=DE^2:AB^2
$$

[유클리드 원론 VI권 명제 19 보조명제] 즉,

$$
\rm DE:DF=CD^2:CB^2
$$

[유클리드 원론 V권 명제 15]. 그리고

$$
\rm PC\cdot CA = PC \cdot CB = CD^2
$$

[I권 명제 13] 이고

$$
\rm DE:DF=EH:HL
$$

[유클리드 VI권 명제 4] 또는

$$
\rm DE:DF=EH\cdot HD: DH\cdot HL
$$

[유클리드 VI권 명제 1, V권 명제 11] 이므로, 그리고

$$
\rm DE:DF=PC\cdot CB : CB^2
$$

이고

$$
\rm PC\cdot CB:CB^2 = OS\cdot SP:OS^2
$$

이기 때문에[^2]

$$
\rm EH\cdot HD: DH\cdot HL=OS\cdot SP:OS^2.
$$

그리고

$$
\rm EH\cdot HD=OS\cdot SP
$$

이어서 그러므로

$$
\rm DH\cdot HL = OS^2 = GH^2.
$$

그러므로 $\rm GH^2 = \it area\rm [DHLM]$이고 직사각형 $\rm DHLM$은 직사각형 $\rm DHKF$에서 $\rm ED$, $\rm DF$를 두 변으로 하는 직사각형과 닮은인 직사각형 $\rm FKLM$​을 뺀 도형이다[유클리드 원론 VI권 명제 24].

이제는 원뿔곡선의 다른 쪽에서 위 명제의 결론을 만족한다면, 선분 $\rm GH$[^3]는 선분 $\rm DE$를 이등분함을 보여야 한다. 선분 $\rm GH$를 길게 늘려서 타원 반대쪽과의 교점을 $\rm W$라 하고, 점 $\rm W$를 지나고 선분 $\rm GX$에 평행한 선분 $\rm WY$를 그리자. 점 $\rm Y$를 지니고 선분 $\rm AN$에 평행한 선분 $\rm YZ$를 그리자. 그러면

$$
\rm GX=WY
$$

이므로

$$
\rm GX^2 = WY^2.
$$

그런데

$$
\rm GX^2 = AX\cdot XO
$$

[I권 명제 13] 그리고

$$
\rm WY^2= AY\cdot YZ
$$

[I권 명제 13].

그러므로

$$
\rm OX:ZY=YA:AX
$$

[유클리드 원론 VI권 명제 16]. 그리고

$$
\rm OX:ZY=XB:BY
$$

[유클리드 VI권 명제 4]이다. 그러므로

$$
\rm HA:AX=XB:BY.
$$

분리 성질(separando)에 의해서

$$
\rm YX:AX=YX:BY
$$

[유클리드 원론 V권 명제 17]. 그러므로

$$
\rm AX=YB.
$$

그리고

$$
\rm AC=CB.
$$

그러므로 나머지도 같아서

$$
\rm XC=CY
$$

이고 그래서

$$
\rm GH = HW.
$$

따라서 선분 $\rm HG$의 반대편에 있는 타원의 선분함께 선분 $\rm DH$에 의해서 이등분된다.

<div style="text-align: right"><h5><b>Q.E.D.</b></h5></div>

[^1]: $area[\rm ABCD]$는 직사각형 $\rm ABCD$의 넓이를 의미한다.
[^2]: 이는 $\rm PC:CB=PS:OS$ [유클리드 원론 VI권 명제 4] 이고 $\rm PC:CB=PC\cdot CB:CB^2$이며 $\rm PS:OS=PS\cdot OS:OS^2$ [유클리드 VI권 명제 1]이기 때문이다.
[^3]: 더 정확히는 선분 $\rm GW$이다.
