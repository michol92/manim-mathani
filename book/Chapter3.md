# 3장 Scene 렌더링

파이썬에 대해서 약간의 기초 지식이 필요하다. 아래 두 자료를 읽자.

- [파이썬 `import`하는 방법](./Chapter3-1.md)
- [클래스, 객체, 메소드](./Chapter3-2.md)

## 3.1. 원 나타내기

Manim을 처음 실행하여 보자.  
클래스와 메소드의 개념이 필요는 하지만 우선 실행을 하여 보도록 하자. 첫 번째 매개 변수로 클래스의 인스턴스가 넘어오게 된다. 이 첫 번째 매개 변수의 이름은 보통 관행적으로 `self`라고 하며, 인스턴스 메서드는 이 `self`를 통해 인스턴 스 속성(attribute)에 접근하거나 다른 인스턴스 메서드를 호출할 수 있다. 뿐만 아니라 `self`를 통해, 클래스 속성에 접근하거나 클래스 메서드를 호출할 수도 있다.
우선 원 하난를 그려보려고 한다.

```python
from manim import *
```

manim 모듈에서 전부(\*)를 가져왔다. 물론 `import manim`과 같다. 그러나 이렇게 하면 좀더 편리하다.  
`CreateCircle`란 이름의 클래스를 정의하고 `Scene`에 상속한다.

```python
class CreateCircle(Scene):
```

클래스 CreateCircle 안에 메소드 construct를 def 키워드를 사용하여 정의한 다. 파이썬은 클래스의 메소드를 정의할 때 self를 명시한다. 메소드를 불러올 때 self는 자동으로 전달된다. self를 사용함으로 클래스 안에 정의한 멤버에 접근할 수있게된다.또한파이썬에서는중괄호{ }을사용하여메소드를묶지않고 들여쓰기를 하여 이를 구분한다. 코드 블럭을 구성하기 위해 if, for, class, def 등등을 작성하면서 나오는 : 다음 아랫줄은 반드시 들여쓰기를 해야 한다. 들여 쓰기의 방법은 스페이스바로 네 칸 또는 한 번의 탭 방식을 사용한다. 중요한 것은 같은 블록 내에서는 들여쓰기 칸 수가 같아야 한다는 것이다. 위반시에는
"IndentationError: unexpected indent"라는 에러 메세지가 출력된다.

```python
    def construct(self):
```

이제 manim 모듈에서 불러온 Circle() 메서드를 이용하여 원을 그리자. 아래와 같이 두 탭 들여쓰기를 하여 작성하자.

```python
        self.add(Circle())
```

Circle()의 () 안에 아무것도 코딩을 하지 않으면 기본값인 중심이 원점이고 반지름 1이며 테두리 색이 빨간색인 원을 그린다. 나중에 매개변수, 메소드, 속성 등에 대하여 논의하자. 지금은 그냥 넘어가자.

전체 코딩은 다음과 같다.

```python
from manim import *

class CreateCircle(Scene):
    def construct(self):
        self.add(Circle())
```

파일명을 `EX_3-1.py`라 저장하자. 파일명은 아래도 좋다.  
터미널 창에서 아래와 같이 코딩후 엔터를 치면 렌더링이 된다.

```bash
~ manim -p EX_3-1.py
```

렌더링 방법과 옵션은 아래 링크를 참조하시오.

- [렌더링 방법](./Chapter3-4.md)
- [렌더링 옵션](./Chapter3-3.md)

그러면 아래와 같이 실행이 된다. 플래그(flag) `-p`는 렌더링후 실행시키라는 옵션이다.  
![실행](./images/EX_3-1.png)
그러면 아래와 같이 실행된다. 동영상이 아니다. 그림이다. `self.add()`는 오브젝트만을 단지 추가할 뿐이다. 실행 파일도 그림을 볼 수 있는 맥의 경우 `미리보기`가 실행된다.

코딩 중에 `self.add(Circle())`처럼 코딩을 할 수도 있으나 인스턴스를 사용하여 코딩을 한다. 그래야 여러 개의 객체를 사용할 수 있다. 아래와 같이 코딩을 하고 파일명을 EX_3-2.py로 하자.

```python
from manim import *

class CreateCircle(Scene):
    def construct(self):
        cir = Circle() // cir이 인스턴스이다.
        self.add(cir)
```

결과는 EX_3-1.py를 실행한 것과 같이 그림 프로그램이 실행되고 아래와 같다.
![실행](./images/EX_3-2.png)

## 3.2. 원을 커지면서 나타나는 애니메이션 실행하기

애니메이션을 구현하려면 오브젝트를 `self.play()`로 실행을 시켜야 한다. 오브젝트 중심으로 부터 커지면서 나타나는 애니메이션 모듈은 `GrowFromCenter([오브젝트 이름])`을 사용하여야 한다. 아래와 같이 코딩을 하고 EX_3-3.py로 저장을 하자.

```python
from manim import *

class CreateCircle(Scene):
    def construct(self):
        cir = Circle() // cir이 인스턴스이다.
        self.play(GrowFromCenter(cir))
```

Circle() 안에 attributes들을 정의 하지 않으면 기본값이 원점을 중심으로 하고 반지름이 1인 원을 출력한다.
렌더링을 실행하자. 그러면 아래와 같이 실행 된다.  
![영상 실행](./movies/EX_3-3.gif)

## 3.3 두 개의 scene 렌더링 하기

이 번에는 한 파일에 여러 Scene를 렌더링 하는 것에 대하여 알아보자.

두 개의 Scene으로 나누어서 렌더링을 하려고 한다.  
첫 번째 Scene은 원이 중심이 원점이고 반지름이 1인 원이 커지면서 나타나게 하고, 두 번째 Scene은 이 정사각형이 그려지면서 만들어지게 하려고 한다.

```python
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

```

EX_3-4.py 파일 내에 여러 개의 Scene이 있으면 다음과 같은 여러 개의 렌더링 방법으로 실행하여야 한다.

우선 첫 번째 렌더링이다.

```bash
manim -p EX_3-4.py
```

![렌더링 1](./images/EX_3-4-1.png)

그러면 두 개의 Scene의 Scene의 이름이 보인다. 1. CreateSquare 2. GrowCircle을 선택하면 선택한 Scene이 렌더링 된다.  
또한 강제로 GrowCircle Scene을 렌더링하려면 아래와 같이 실행하면 된다.

```bash
manim -p EX_3-4.py GrowCircle
```

![렌더링 3](./images/EX_3-4-3.png)

강제로 CreateSquare Scene을 렌더링하려면 아래와 같이 실행하면 된다.

```bash
manim -p EX_3-4.py CreateSquare
```

![렌더링 4](./images/EX_3-4-4.png)

그러나 모든 Scene를 렌더링 하려면 다음과 플래그 -a를 넣어 실행하면 된다.

```bash
manim -p -a EX_3-4.py
```

![렌더링 5](./images/EX_3-4-5.png)

실행은 다음과 같다.

![정사각형 만들기](./images/EX_3-4-6.gif)

![원 생성하기](./images/EX_3-4-7.gif)
