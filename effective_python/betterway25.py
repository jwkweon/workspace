################                 BetterWay 25                 ################
# super로 부모 클래스를 초기화하자

#기존 자식 클래스에서 부모 클래스의 __init__ 메서드를 직접 호출하는 방법으로 부모 클래스를 초기화
class MyBaseClass(object):
    def __init__(self, value):
        self.value = value

class MyChildClass(MyBaseClass):
    def __init__(self):
        MyBaseClass.__init__(self, 5)

'''
    이러한 방법은 간단한 계층 구조에서는 잘 동작
    많은 경우에서는 제대로 동작하지 못함
    다중 상속의 영향을 받는다면 슈퍼클래스의 __init__ 메서드를 직접 호출하는
    행위는 예기치 못한 동작을 일으킬 수 있다.

    문제 1 : __init__의 호출 순서가 모든 서브클래스에 걸쳐 명시되어 있지 않다.
'''

class TimesTwo(object):
    def __init__(self):
        self.value *= 2

class PlusFive(object):
    def __init__(self):
        self.value += 5

class OneWay(MyBaseClass, TimesTwo, PlusFive):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        TimesTwo.__init__(self)
        PlusFive.__init__(self)

foo = OneWay(5)
print('First ordering is (5 * 2) + 5 =', foo.value)

class OtherWay(MyBaseClass, TimesTwo, PlusFive):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        TimesTwo.__init__(self)
        PlusFive.__init__(self)

foo = OtherWay(5)
print('Second ordering still is', foo.value)

'''
    다른 문제 : 다이아몬드 상속
    다이아몬드 상속은 서브클래스가 계층 구조에서 같은 슈퍼클래스를 둔 서로 다른
    두 클래스에서 상속받을 때 발생
    다이아몬드 상속은 공통 슈퍼클래스의 __init__ 메서드를 여러 번 실행하게 해서
    예기치 못한 동작을 일으킨다.
'''

class TimesFive(MyBaseClass):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        self.value *= 5

class PlusTwo(MyBaseClass):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        self.value += 2

class ThisWay(TimesFive, PlusTwo):
    def __init__(self, value):
        TimesFive.__init__(self, value)
        PlusTwo.__init__(self, value)

foo = ThisWay(5)
print('Should be (5 * 5) + 2 = 27 but', foo.value)
