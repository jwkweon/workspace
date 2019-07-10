################                 BetterWay 19                 ################
# 키워드 인수로 선택적인 동작을 제공하자
def remainder(number, divisor):
    return number % divisor

#assert 뒤의 조건이 True가 아니면 AssertError 발생
assert remainder(20, 7) == 6
a1 = remainder(20, 7)
a2 = remainder(20, divisor=7)
a3 = remainder(number=20, divisor=7)
a4 = remainder(divisor=7, number=20)
#remainder(divisor=7, 20) 이건 안됨
#위치 인수는 키워드 인수 앞에 지정해야함

print(a1, a2, a3, a4)

def flow_rate(weight_diff, time_diff):
    return weight_diff / time_diff

weight_diff = 0.5
time_diff = 3
flow = flow_rate(weight_diff, time_diff)
print('%.3f kg per second' % flow)

def flow_rate(weight_diff, time_diff, period=1):
    return (weight_diff / time_diff) * period

flow_per_second = flow_rate(weight_diff, time_diff, 1)
print('%.3f kg per second' % flow_per_second)

flow_per_second = flow_rate(weight_diff, time_diff)
print('%.3f kg per second' % flow_per_second)

flow_per_hour = flow_rate(weight_diff, time_diff, 3600)
print('%.3f kg per hour' % flow_per_hour)

def flow_rate(weight_diff, time_diff, period=1, units_per_kg=1):
    return ((weight_diff / units_per_kg) / time_diff) * period

flow_per_hour = flow_rate(weight_diff, time_diff, period=3600, units_per_kg=2.2)
print('%.3f kg per hour' % flow_per_hour)
