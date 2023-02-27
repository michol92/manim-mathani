# 파이썬 `import`하는 방법

파이썬(Python)에서는 모듈(`module`)을 `import`를 사용하여 불러올수 있다.  
세 가지 방법이 있다. 더 정확히는 두 가지 방법이다.  
첫 번째 방법:

## 1) import [모듈 이름]

> 형식:
>
> ```python
> import [module 이름]
> ```
>
> 이 방법은 모듈 전체를 가져올 경우 사용한다. 이렇게 불러오면 `모듈.변수`의 형식으로 써주어야 한다.

예:

```python
import math
math.pi
```

실행결과:

```python
3.141592653589793
```

## 2) import [module 이름] as [변수 이름]

> 형식:
>
> ```python
> import [module 이름] as [변수 이름]
> ```
>
> 모듈의 가져와서 변수이름으로 지정한다.

예:

```python
import math as m
m.sqrt(2)
```

실행결과:

```python
1.4142135623730951
```

## 3) from [module 이름] import [변수 이름]

> 형식:
>
> ```python
> from [module 이름] import [변수 이름]
> ```
>
> 모듈에서 지정한 변수만 가져온다.

예:

```python
from math import pi
pi
```

실행결과:

```python
3.141592653589793
```
