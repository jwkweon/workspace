'''
데코레이터는 대상 함수를 wrapping하고 wrapping된 함수의 앞뒤에
꾸며질 구문들을 정의해서 손쉽게 재사용 가능하게 해주는 것.
'''
@decorator_
def function():
    print("what is decorator")

'''
메인 구문이 있고, 부가적인 구문을 추가하고 싶을때
부가적인 구문을 반복해서 사용하고 싶을때 decorator로
선언해서 자유롭게 사용 가능
'''
def main_func():
    print("Main Function Start")

'''
추가적인 작업 : 해당 문장 출력 전후에 날짜 시간 출력
'''
import datetime

def main_func():
    print(datetime.datetime.now())
    print("Main Function Start")
    print(datetime.datetime.now())

def main_func1():
    print(datetime.datetime.now())
    print("Main Function1 Start")
    print(datetime.datetime.now())

def main_func2():
    print(datetime.datetime.now())
    print("Main Function2 Start")
    print(datetime.datetime.now())

def main_func3():
    print(datetime.datetime.now())
    print("Main Function3 Start")
    print(datetime.datetime.now())

#############################
#       decorator 적용       #
#############################
import datetime

def datetime_decorator(func):
    def decorated():
        print(datetime.datetime.now())
        func()
        print(datetime.datetime.now())
    return decorated

@datetime_decorator
def main_func1():
    print("Main Function1 Start")

@datetime_decorator
def main_func2():
    print("Main Function2 Start")

@datetime_decorator
def main_func3():
    print("Main Function3 Start")

main_func3()
