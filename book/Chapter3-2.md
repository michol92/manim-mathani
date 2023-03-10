# 클래스(class)와 상속

파이썬에서 class란 무엇이고 상속은 왜 하여야 하는가?
보통 상속은 기존 클래스를 변경하지 않고 기능을 추가하거나 기존 기능 을 변경하려고 할 때 사용한다. "클래스에 기능을 추가하고 싶으면 기존 클래스를 수정하면 되는데 왜 굳이 상속을 받아서 처리해야 하지?" 라는 의문이 들 수 도 있다. 하지만 기존 클래스가 라이브러리 형태로 제공되거나 수정이 허용되지 않는 상황이라면 상속을 사용해야 한다.

## 클래스

클래스란 객체(instance)를 만들어내기 위한 툴이다. 동일한 무엇가를 계속해서 만들어낼 수 있는 형태이며 만들어낸 객체들은 모두 고유한 겅격을 가진다. 단 객체별로 갖는 기능은 모두 동일하다.  
클래스는 객체(object)의 구조와 행동을 정의한다. 객체 클래스는 초기화를 통해 제어한다. 클래스는 복잡한 문제를 다루기 쉽도록 만든다. 즉, 여러번 같은 작업을 할 수 있다.

## 상속

클래스에서 상속이란, 물려주는 클래스(Parent Class, Super class)의 내용(속성과 메소드)을 물려받는 클래스(Child class, sub class)가 가지게 된다.

## 인스턴스(instance)

클래스로 만들어진 객체를 인스턴스라고 한다. 인스턴스와 객체는 동일하다. 단 차이점은 인스턴스는 클래스오 객체 사이의 관계를 설명할 때 그 객체를 인스턴스라고 한다. 단순하게 말할때는 객체라고 한다.

## 클래스와 메서드 만들기

클래스 만들기:

```python
class [클래스명]
    [코드]
```

메서드 만들기:

```python
class [클래스명]
    def [메서드 명(self, ...)]
        [메서드 코드]
```
