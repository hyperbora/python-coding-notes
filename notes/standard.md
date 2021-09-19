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