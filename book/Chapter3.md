# 3장 Manim으로 Scene 제작하기 기초

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
manim -p EX_3-1.py
```

그러면 아래와 같이 실행이 된다. 플래그(flag) `-p`는 렌더링후 실행시키라는 옵션이다.
