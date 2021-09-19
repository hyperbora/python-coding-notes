# 파이썬 기본

## @classmethod 사용법

\_\_init__ 메서드를 사용하는 것 외에 대체 생성자(alternative constructor)를 생성할 수 있는 유연성을 제공한다.

팩토리 패턴을 생성하는 가장 쉬운 방법을 제공한다.

```py
class User:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @classmethod
    def using_string(cls, names_str):
        first, second = map(str, names_str.split(" "))
        student = cls(first, second)
        return student

    @classmethod
    def using_json(cls, obj_json):
        # Parsing json object…
        return student

    @classmethod
    def using_file_obj(cls, file_obj):
       # Parsing file object…
       return student


data = User.using_string("Larry Page")
data = User.using_json(json_obj)
data = User.using_file_obj(file_obj)
```

## @staticmethod 사용법

- 클래스 메서드와 같은 클래스의 객체가 아니라 클래스에 바인딩된다.
- 클래스 상태에 대한 종석성 없이 자체적으로 작동할 수 있다.
- self나 cls를 사용하지 않는다.
- 클래스가 사용하기 위한 유틸리티 메서드로서 이 정적 메서드를 사용할 수 있다.
- 클래스 내부에 유지하면 해당 함수를 클래스와 쉽게 연관시킬 수 있다.

## @property 사용법

값을 가져오고 설정하는 데 유용한 파이썬 기능 중 하나

사용하는 이유

1. (getter) 객체의 속성을 숨기고 필요하면 연산한 결과를 리턴하기 위해 사용
2. (setter) set 속성의 유효성 검사를 메소드 내부에서 하기 위해 사용

```py
class Temprature:
    def __init__(self, temprature=0):
        self._temprature = temprature

    @property
    def fahrenheit(self):
        return self._temprature

    @fahrenheit.setter
    def fahrenheit(self, temp):
        if not isinstance(temp, int):
            raise("Wrong input type")

        self._temprature = (self._temprature * 1.8) + 32

if __name__ == "__main__":
    t = Temprature(temprature=30)
    print(t.fahrenheit) # print 30
    t.fahrenheit = 50
    print(t.fahrenheit) # print 86.0

```

## 모듈 사용방법

### \_\_init__ 파일

파이썬 3.3 이후로 \_\_init__.py는 디렉터리가 파이썬 패키지임을 나타내기 위해 필요하지 않다.

하지만 \_\_init__.py 파일은 코드를 쉽게 만들고 특정 방식으로 패키지화하기 위해 여러 시나리오에서 유용할 수 있다.

```py
purchase/
    cart.py
    payment.py

__init__.py 파일에서 다음과 같이 사용
from .cart import Cart
from .payment import Payment

다른 파일에서 다음과 같이 사용
import purchase
cart = purchase.Cart()
payment = purchase.Payment()
```

### \_\_all__ 속성

사용자가 모든 클래스를 임포트 하려고 할 때 특정 클래스만 허용하도록 제어할 수 있다.

```py
class A:
    pass

class B:
    pass

class C:
    pass

__all__ = ["B", "C"]
```

### \_\_new__ 속성

- 인스턴스를 생성할 때 마법 메서드 \_\_new__가 호출될 것이다.
- 해당 메서드를 사용하면 인스턴스 생성을 쉽게 사용자 정의할 수 있다.
- 클래스의 인스턴스를 초기화하는 동안 \_\_init__를 호출하기 전에 호출된다.
- super를 사용해 슈퍼클래스의 \_\_new__ 메서드를 호출함으로써 클래스의 새 인스턴스를 생성할 수도 있다.
- \_\_new__를 사용해서 메타클래스를 사용해 서브클래스가 추상 클래스나 슈퍼클래스를 상속하기 전에 유효성을 검증할 수 있다.

```py
from abc import abstractmethod, ABCMeta


class UserAbstract(metaclass=ABCMeta):
    """__new__() 이니셜라이저를 사용해 팩토리 패턴을 구현하는 추상 기본 클래스 템플릿."""

    def __new__(cls, *args, **kwargs):
        """객체 인스턴스를 생성하고 기본 속성을 설정한다."""
        obj = object.__new__(cls)
        given_data = args[0]
        # 여기서 데이터 유효성을 검사한다
        if not isinstance(given_data, str):
            raise ValueError(f"Please provide string: {given_data}")
        return obj


class User(UserAbstract):
    """UserAbstract 클래스를 구현하고 그 자신의 변수를 추가한다."""

    def __init__(self, name):
        self.name = name


user = User(10)
# ValueError: Please provide string: 10

```

### \_\_call__ 속성

- 싱글톤 생성, 값 기억, 데코레이터 사용하는데 활용

```py
"""
객체를 직접 생성하는 것을 방지
"""
class NoClassInstance(type):
    """Create the user object."""
    def __call__(self, *args, **kwargs):
        raise TypeError("Can't instantiate directly""")


class User(metaclass=NoClassInstance):

    @staticmethod
    def print_name(name):
        """print name of the provided value."""
        print(f"Name: {name}")


user = User()
# TypeError: Can't instantiate directly
User.print_name("Larry Page")
# Name: Larry Page

```

```py
"""
__call__를 이용한 API 디자인
"""
class Calculation:
    """
    다른 계산 알고리즘을 둘러싼 래퍼는 두 숫자가 서로 다른 작업을 수행할 수 있도록 한다.
    공통 로직의 복사 없이 특정 작업을 수행하기 위해 다른 메서드나 알고리즘을 전송할 수 있다.
    여기서는 __call__ 안에 코드가 표시돼 API를 훨씬 쉽게 사용할 수 있다.
    """
    def __init__(self, operation):
        self.operation = operation

    def __call__(self, first_number, second_number):
        if isinstance(first_number, int) and isinstance(second_number, int):
            return self.operation(self, first_number, second_number)
        raise ValueError("Provide numbers")



def add(self, first, second):
    return first + second

def multiply(self, first, second):
    return first * second


add = Calculation(add)
print(add(5, 4)) # 9
multiply = Calculation(multiply)
print(multiply(5, 4)) # 20
```

### 파이썬 디스크립터

- 객체의 딕셔너리에서 속성을 가져오고, 설정하고, 삭제하는 데 도움이 된다.
- 클래스 속성에 엑세스하면 룩업 체인이 시작된다.
- \_\_get__, \_\_set__, \_\_delete__ 가 있다.
- 클래스 인스턴스에서 특정 속성 값을 지정하거나 가져오는 경우 속성 값을 설정하기 전이나 속성 값을 가져오는 동안에 추가 처리를 수행할 수 있다.
- \_\_get__(self, instance, owner) : 속성에 엑세스하면 이 메서드는 자동으로 호출된다.
- \_\_set__(self, instance, value) : 인스턴스의 속성을 설정할 때 사용된다, 이 메서드는 obj.attr = value 로 호출된다. 
- \_\_delete__(self, instance) : 특정 속성을 삭제하려는 경우 호출된다.

## 데코레이터

### 사용하는 이유

- 데코레이터를 함수에 적요하면 둘러싸는 함수 전후에 실행하는 능력이 있다.
- 함수에서 추가 코드를 실행하는 데 도움이 된다.
- 입력 인자와 반환 값을 액세스하고 수정할 수 있으며, 여러 위치에서 사용할 수 있다.
- 다중 데코레이터가 적용되면 아래에 있는 데코레이터가 먼저 실행된다.

```py
"""
래퍼 클로저(wrapper closure)는 입력 함수(input function)에 엑세스할 수 있고
함수 전후에 새 코드를 추가할 수 있다.
명시적으로 호출될 때까지 함수를 실행하지 않는다.
또한 호출될 때까지 함수를 감싸고 함수의 객체를 작성한다.
"""
def to_upper_case(func):
    def wrapper(*args, **kwargs):
        text = func(*args, **kwargs)
        if not isinstance(text, str):
            raise TypeError("Not a string type")
        return text.upper()

    return wrapper


@to_upper_case
def say():
    return "welcome"


@to_upper_case
def hello():
    return "hello"


print(say())  # WELCOME
print(hello())  # HELLO
```

### @wraps

기존 데코레이터는 \_\_name__, \_\_doc__ 정보가 손실되어서 functools.wraps를 사용한다.

```py
from functools import wraps


def logging(func):
    @wraps(func)
    def logs(*args, **kwargs):
        print(func.__name__ + " was called")
        return func(*args, **kwargs)
    return logs


@logging
def foo(x):
    """does some math"""
    return x + x * x


print(foo.__name__)  # prints 'foo'
print(foo.__doc__)   # prints 'does some math'
```

### 클래스 데코레이터

- 클래스도 데코레이터로 사용이 가능하며, 상태를 유지하기 위해 사용한다.

```py
"""
__call__ 메서드는 클래스를 데코레이트한 함수가 호출될 때마다 호출된다.
functools 라이브러리는 여기서 데코레이터 클래스를 작성하는 데 사용된다.
클래스 데코레이터를 사용해 변수의 상태를 저장한다.
"""
import functools
from typing import Any


class Count:
    def __init__(self, func) -> None:
        functools.update_wrapper(self, func)
        self.func = func
        self.num = 1

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        self.num += 1
        print(f"Number of times called: {self.num}")
        return self.func(*args, **kwargs)


@Count
def counting_hello():
    print("Hello")


counting_hello()
counting_hello()
```

- 클래스 데코레이터를 사용해 타입 검사를 수행하는 예제

```py
import functools
from typing import Any


class ValidateParameters:
    def __init__(self, func) -> None:
        functools.update_wrapper(self, func)
        self.func = func

    def __call__(self, *parameters: Any) -> Any:
        if any([isinstance(item, int) for item in parameters]):
            raise TypeError("Parameter shouldn't be int!!")
        else:
            return self.func(*parameters)


@ValidateParameters
def add_numbers(*list_string):
    return "".join(list_string)


print(add_numbers("a", "n", "b"))

print(add_numbers("a", 1, "c"))
```

## 컨텍스트 매니저

- 리소스 관리에 유용하다.
- with 구문을 생성하려면 \_\_enter__ 메서드와 \_\_exit__ 메서드를 객체에 추가하면 된다.

### 동작방식

- \_\_enter__는 컨텍스트 매니저 블록에서와 같이 변수에 할당된 객체를 반환한다. 보통 self
- \_\_exit__ 는 \_\_enter__에 의해 반환되는 것이 아니라 본래의 컨텍스트 매니저를 호출한다.
- \_\_init__ 또는 \_\_enter__ 메서드에서 예외나 오류가 있으면 \_\_exit__가 호출되지 않는다.
- 코드 블록이 컨텍스트 매니저 블록에 들어가면, 어떤 예외나 오류가 발생했는지 상관없이 \_\_enter__가 호출될 것이다.
- \_\_exit__가 참을 반환하면 어떤 예외도 억제되고, 실행은 컨텍스트 매니저 블록에서 오류 없이 종료된다.

### contextlib를 이용한 컨텍스트 매니저 생성

contextlib.contextmanager 데코레이터라는 라이브러리를 제공한다.

\_\_enter__와 \_\_exit__ 메서드로 전체 클래스를 작성할 필요가 없다.

```py
"""
write_file이 리소스를 획득하고, 이후에 호출자가 사용하는 yield 키워드에 영향을 미친다.
호출자가 with 블록을 종료하면, 리소스 정리와 같은 나머지 정리 단계가 발생할 수 있으므로
제너레이터는 계속 실행된다.

@contextmanager 데코레이터를 사용해 컨텍스트 매니저를 생성하는 경우 제너레이터가 생성하는
값은 컨텍스트 리소스다.
"""
from contextlib import contextmanager


@contextmanager
def write_file(file_name):
    try:
        fread = open(file_name, "w")
        yield fread
    finally:
        fread.close()


with write_file("accounts.txt") as f:
    f.write("Hello, how you are doing")
    f.write("Writing into file")
```

## 제너레이터와 이터레이터

### 이터레이터

- 이터레이터는 데이터 스트림에서 작동하는 객체다.
- 이터레이터 객체는 \_\_next__라는 메서드를 갖고 있으며, for 루프, 리스트 컴프리헨션, 또는 모든 데이터 포인트를 통해 객체나 다른 데이터 구조에서 데이터를 얻기 위한 무언가를 사용할 때 백그라운드에서 \_\_next__ 메서드가 호출된다.

### 이터러블

- \_\_iter__라는 메서드가 있으며, 이 메서드는 이터레이터를 반환한다.
- \_\_iter__가 모든 객체에서 호출되면, 데이터를 가져오기 위해 객체를 반복하는데 사용할 수 있는 이터레이터를 반환한다.
- 문자열, 리스트, 파일, 딕셔너리는 모두 이터러블의 예제이다.
- 한정된 수의 이터레이터를 원한다면 StopIteration을 발생시킨다.

```py
class MultiplyByTwo:
    def __init__(self, number, limit) -> None:
        self.number = number
        self.limit = limit
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.count += 1
        value = self.number * self.count

        if value > self.limit:
            raise StopIteration
        else:
            return value

for num in MultiplyByTwo(500, 5000):
    print(num)
```

### 제너레이터

- 많은 양의 데이터나 많은 수의 파일을 읽는 데 유용하다.
- 일시 중지했다가 재시작할 수 있다.
- 제너레이터는 리스트처럼 반복할 수 있는 객체를 반환한다.
- 리스트와 달리 한 번에 하나씩 항목을 생성한다.

```py
"""
__next__, __iter__를 정의할 필요가 없다.
yield는 return과 비슷하지만, 함수를 종료하는 대신 다른 값을 요청할 때까지 실행을 일시 중지한다.
"""
def multiple_generator(number, limit):
    counter = 1
    value = number * counter

    while value <= limit:
        yield value
        counter += 1
        value = number * counter

for num in multiple_generator(500, 5000):
    print(num)
```

### yield

함수 중 하나에서 yield를 정의하고, 함수가 호출되면 제너레이터 객체가 제공된다.

하지만 그것은 함수를 실행하지 않는다. 제너레이터 객체를 얻고 제너레이터(for 루프나 next() 사용)에서

객체를 추출할 때마다 파이썬은 yieid 키워드가 다가올 때까지 함수를 실행할 것이다.

파이썬이 yieid 키워드에 도달하면 객체를 전달하고 추출할 때까지 일시 중지한다.

일단 객체를 추출하면, 파이썬은 다른 yieid에 도달할 때까지 계속해서 yieid 후에 코드를 재개하고 실행한다.

제너레이터가 소진되면, for 루프가 자동으로 처리되는 StopIteration 예외와 함께 종료될 것이다.

### yieid from

파이썬 3부터 사용됐다. 다른 제너레이터에서 값을 얻는다.

```py
def flat_list(iter_values):
    """flatten a multi list or something."""
    for item in iter_values:
        if hasattr(item, '__iter__'):
            yield from flat_list(item)
        else:
            yield item

print(list(flat_list([1, [2], [3, [4]]])))
#  [1, 2, 3, 4]
```
