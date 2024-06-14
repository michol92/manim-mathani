# I권

## 명제 5

꼭짓점이 $\rm A$ 이고 밑면이 원 $\rm BC$ 인 비스듬한 원뿔면을 원 $\rm BC$ 에 수직이고 축을 포함하는 평면으로 잘랐다. 이 때 비스듬한 원뿔과 평면과 교선의 도형은 삼각형 $\rm ABC$ 이다. [I권 명제 3] 그리고 삼각형 $\rm ABC$ 에 수직인 다른 평면으로 꼭짓점 $\rm A$ 의 한 쪽 원뿔 면을 잘랐을 때, 삼각형 $\rm ABC$ 와 평면과의 교점을 $\rm G$, $\rm K$ 라 할 때, 삼각형 $\rm AGK$ 는 삼각형 $\rm ABC$ 와 닯음이고 두 삼각형이 반대쪽에 놓여 있다. 즉, $\rm\angle AKG=\angle ABC$ 를 만족한다. 이때, 선분 $\rm GK$ 를 포함하고 삼각형 $\rm AGK$에 수직인 평면과 비스듬한 원뿔과 교선을 $\rm GHK$ 라 하자. 그러면 교선 $\rm GHK$ 는 원이다. 이 원을 소반대(subcontrary) 원이라 한다.

## 애플릿

<iframe
src="./GGB_Html/Prop_5_Book_I_Apollonius.html"
width="800"
height="600"
frameborder="0"
framespacing="0"
marginheight="0"
marginwidth="0"
scrolling="no"
vspace="0"></iframe>

### 증명

교선 $\rm GHK$ 와 원 $\rm BC$ 위의 어떤 점을 각각 $\rm H$, $\rm K$ 이라 하자. 두 점 $\rm H$, $\rm K$ 에서 삼각형 $\rm ABC$ 에 수직으로 내린 수선을 발을 각각 $\rm F$, $\rm M$ 이라 하자. 두 수선의 발 $\rm F$ 은 삼각형 $\rm ABC$ 와 $\rm GK$ 를 포함하고 삼각형 $\rm ABC$ 에 수직인 평면과이 교선 위에 있고, 점 $\rm M$ 은 삼각형 $\rm ABC$ 와 원 $\rm BC$ 의 교선 위에 있다. [원론 XI권 정의 6] 두 선분 $\rm FH$, $\rm LM$ 을 그리자. 그러면 두 선분 $\rm FH$, $\rm LM$ 은 평행하자. [원론 XI 명제 6]

점 $\rm F$ 를 지나는 직선 $\rm DFE$ 는 직선 $\rm BC$ 와 평행하다. 직선 $\rm FH$ 와 직선 $\rm LM$ 은 평행하므로 두 직선 $\rm FH$ 와 $\rm DE$ 를 포함하는 평면은 원뿔의 밑면 원 $\rm BC$ 와 평행하다. [I권 명제 4]

그러므로

$$
{\rm DF}\cdot{\rm FE}={{\rm FH}}^2
$$

이다. [원론 III권 명제 31, VI권 명제 8, I권 명제 1 부정명제]

선분 $\rm ED$ 는 선분 $\rm BC$ 와 평행하기 때문에 $\rm\angle ADE=\angle ABC$ 이다. 그리고 $\rm\angle AKG=\angle ADE$ 라 가정하다. 따라서 $\rm\angle AKG=\angle ADE$ 이다. 그리고 점 $\rm F$ 에서 맞꼭짓각은 같다. 그러므로 삼각형 $\rm DFG$ 와 삼각형 $\rm KFE$ 는 닮음 삼각형이다. 그러므로

$$
{\rm EF}:{\rm FK}={\rm GF}:{\rm FD}
$$

이 성립한다. [원론 VI권 명제 4] 그러므로

$$
{\rm EF}\cdot{\rm FD}={\rm KF}\cdot{\rm FG}
$$

이다. [원론 VI권 명제 16] 그리고 식 (1)에서 ${{\rm FH}}^2={\rm EF}\cdot{\rm FD}$ 을 보였다. 그러므로

$$
{\rm KF}\cdot{\rm FG}={{\rm FH}}^2 \tag{4}
$$

이다.

식 (4)의 의미는 선 $\rm GHK$ 에서 선분 $\rm GK$ 가 빗변이고 임의의 점 $\rm H$ 에 대하여 $\rm\angle GHK=\frac{\pi}{2}$ 이다. 즉, 선 $\rm GHK$ 가 원이라는 의미이고, 선분 $\rm GK$ 는 지름이 된다.

Q.E.D.

---
