# I 권

## 명제 11

꼭짓점이 $\rm A$이고 밑변이 원 $\rm BC$인 원뿔이 있다. 원뿔의 축을 포함하는 평면에 의해서 잘려진 원뿔곡선인 축 삼각형 $\rm ABC$이 만들어진다[I권 명제 3]. 다른 평면으로 밑변을 잘라 교선을 선분 $\rm DE$이라 하고 선분 $\rm DE$가 직선 $\rm BC$에 수직이 되도록 하자. 이 평면으로 원뿔을 잘라 만들어진 원뿔곡선을 $\rm DFE$라 하자. 그리고 원뿔 곡선 $\rm DFE$의 지름을 $\rm FG$가[I권 명제 7, 정의 4] 축 삼각형 $\rm ABC$의 한 변인 $\rm AC$에 평행하다고 하자. 그리고 선분 $\rm FH$를 점 $\rm F$에서 선분 $\rm FG$에 수직이며

$$
{{\rm BC}}^2:{\rm BA}\cdot{\rm AC}={\rm FH}:{\rm FA}
$$

가 성립하도록 그리자. 그리고 원뿔곡선 위의 임의점 $\rm K$를 잡고 직선 $\rm DE$에 평행하고 점 $\rm K$를 지나는 직선 $\rm KL$을 그리자.

그러면 ${{\rm KL}}^2={\rm HF}\cdot  {\rm FL}$이다.

## 애플릿

<iframe
src="/Book_I/GGB_Html/Prop_11_Book_I_Apollonius.html"
width="800"
height="600"
frameborder="0"
framespacing="0"
marginheight="0"
marginwidth="0"
scrolling="no"
vspace="0"></iframe>

## 증명

점 $\rm L$을 지나며 선분 $\rm BC$에 평행한 직선 $\rm MN$을 그리자. 그리고 선분 $\rm DE$는 역시 선분 $\rm KL$에 평행하다. 그러므로 두 선분 $\rm KL$, $\rm MN$을 포함하는 평면은 두 선분 $\rm BC$, $\rm DE$를 포함하는 평면, 즉 밑면과 평행하다[유클리드 XI권 명제 15]. 그러므로 두 선분 $\rm KL$, $\rm MN$을 포함하는 평면은 지름이 $\rm MN$인 원이다[I권 명제 4]. 그리고 선분 $\rm KL$과 선분 $\rm MN$은 수직이다. 왜냐하면 역시 선분 $\rm DE$가 선분 $\rm BC$에 수직이기 때문이다[유클리드 원론 XI권 명제 10]. 그러므로

$$
{\rm ML} \cdot {\rm LN} ={{\rm KL}}^2
$$

[유클리드 원론 III권 명제 31, VI권 명제 대우명제, VI권 명제 17]

그리고

$$
{{\rm BC}}^2:{\rm BA}\cdot{\rm AC}={\rm HF}:{\rm FA}
$$

이고

$$
\rm BC^2 :\rm BA\cdot AC = \rm BC \cdot \rm BC :\rm BA \cdot \rm CA
$$

이기 때문에[유클리드 원론 VI권 명제 23] 그러므로

$$
\rm HF:\rm FA= \rm BC\cdot \rm BC : \rm BA\cdot\rm CA
$$

그런데

$$
\rm BC: CA=MN:NA=ML:LF \tag{1}
$$

이고[유클리드 원론 VI권 명제 4]

$$
\rm BC:BA=MN:MA=LM:MF=NL:FA \tag{2}
$$

[유클리드 원론 VI권 명제 4, 명제 2]

그러므로 위 두 식 $(1)$, $(2)$ 에 의해서

$$
\rm HF:FA=ML\cdot NL:LF\cdot FA
$$

[유클리드 원론 VI권 명제 23].

그런데 선분 $\rm FL$을 공통 높이처럼 보면,

$$
\rm HF : FA=HF\cdot FL:LF\cdot FA
$$

[유클리드 원론 VI권 명제 1] [^1] 그러므로

$$
\rm ML \cdot LN : LF\cdot FA=HF\cdot FL:LF\cdot FA
$$

[유클리드 원론 V권 명제 11]

그러므로

$$
\rm ML\cdot LN = HF\cdot FL
$$

그런데

$$
\rm ML\cdot LN = KL^2
$$

이므로

$$
\rm KL^2 = HF\cdot FL
$$

이 원뿔곡선을 **_포물선_**이라 한다. 그리고 직선 $\rm HF$를 지름 $\rm FG$에 직각이며 정사각형($\rm ZH$)에 적용되는 직선이며, 이를 **_직립변(upright side)_**라 한다.

**Q.E.D.**

---

[^1]: 식 (8)에서 식 (9) 유도에서 $\rm ML\cdot NL = HF\cdot FL$임을 살펴보자. $\rm HF=(BC^2\cdot FA)/(BA \cdot AC)$(가정)이고 닮음에 의해서 $\rm FL:AC=ML:BC$이므로 $\rm FL=AC/BC\cdot ML$이다. 따라서 $\rm FH\cdot FL=(BC^2\cdot FA)/(BA\cdot AC)\cdot AC/BC \cdot ML=BC/BA \cdot FA\cdot ML$이다. 그런데 닮음에 의해서 $\rm BA:BC=MF:ML=FA:LN$이므로 $\rm BC/BA\cdot FA=LN$이다. 따라서 $\rm FH\cdot FL=BC/BA \cdot FA \cdot ML = LN \cdot ML$이다.
