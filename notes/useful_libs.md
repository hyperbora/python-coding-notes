# 유용한 파이썬 내장 라이브러리

## collections

### namedtuple

```py
"""
튜플은 명명된 것인지 여부에 관계없이 불변이다.
튜플은 튜플의 데이터에 컨텍스트나 이름을 제공하지 않으며 dict는 불변성이 없으므로, 첫 번째 할당 후에 데이터를 변경하지 않으려는 경우 제약을 받는다.
namedtuple은 인덱스 대신 이름을 사용해 액세스를 좀 더 편리하게 만든다.
namedtuple은 필드 이름이 문자열이어야 한다는 엄격한 제한이 있다.
"""
from collections import namedtuple

Point = namedtuple("Point", ["x", "y", "z"])
point = Point(x=3, y=4, z=5)
print(point.x, point.y, point.z)
```

```py
def get_user_info(user_obj):
    user = get_data_from_db(user_obj)
    UserInfo = namedtuple("UserInfo", ["first_name", "last_name", "age"])
    
    user_info = UserInfo(first_name=user["first_name"],
                         last_name=user["last_name"],
                         age=user["age"])
    
    return user_info

def get_full_name(user_info):
    return user_info.first_name + user_info.last_name

user_info = get_user_info(user_obj)
full_name = get_full_name(user_info)

```

### Counter

- 유사한 데이터를 집계할 수 있는 편리한 방법 제공
- most_common(num) : num 개수 만큼 가장 많은 키와 값을 반환한다.
- elements() : 요소가 개수만큼 반복되는 이터레이터를 반환한다.

### dict

```py
"""
두 개의 딕셔너리를 병합하는 방법, 파이썬 3.5 이상
"""
salary_first = {"Lisa": 238900, "Ganesh": 8765000, "John": 3450000}
salary_second = {"Albert": 3456000, "Arya": 987600}
{**salary_first, **salary_first}
```

```py
"""
두 개의 딕셔너리를 병합하는 방법, 파이썬 3.5 미만
"""
salary_first = {"Lisa": 238900, "Ganesh": 8765000, "John": 3450000}
salary_second = {"Albert": 3456000, "Arya": 987600}
salary = salary_first.copy()
salary.update(salary_second)
```


```py
"""
딕셔너리 가독성 좋게 출력
"""
import pprint

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(colors)
```


```py
"""
딕셔너리 가독성 좋게 출력, 중첩된 딕셔너리의 경우
"""
import json

data = {'a':12, 'b':{'x':87, 'y':{'t1': 21, 't2':34}}}
json.dumps(data, sort_keys=True, indent=4)
```

## abc

추상클래스 관련 라이브러리

abc 모듈을 사용해 모든 예상되는 메서드를 구현하고, 유지 보수 가능한 코르를 제공한다.

```py
from abc import ABCMeta, abstractmethod

class Fruit(metaclass=ABCMeta):

    @abstractmethod
    def taste(self):
        pass

    @abstractmethod
    def originated(self):
        pass


class Apple:
    def originated(self):
        return "Central Asia"


fruit = Fruit()
"""
TypeError:
"Can't instantiate abstract class Fruit with abstract methods originated, taste"
"""
```