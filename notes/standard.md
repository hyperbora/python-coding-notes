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