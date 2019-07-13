################                 BetterWay 23                 ################
# 인터페이스가 간단하면 클래스 대신 함수를 받자
from collections import defaultdict

names = ['Socrates', 'Archimedes', 'Plato', 'Aristotle']
names.sort(key=lambda x: len(x))
print(names)

name = []
name.sort(key=lambda x: len(x))
print(name)

def log_missing():
    print('Key added')
    return 0

current = {'green': 12, 'blue': 3}
increments = [
    ('red', 5),
    ('blue', 17),
    ('orange', 9),
    ]
result = defaultdict(log_missing, current)
print('Before:', dict(result))
for key, amount in increments:
    result[key] += amount
print('After: ', dict(result))

int_dict = defaultdict(int)
int_dict
int_dict['key1']
int_dict
int_dict['key2'] = 'test'
int_dict

list_dict = defaultdict(list)
list_dict
list_dict['key1']
list_dict
list_dict['key2'] = 'test'
list_dict

def increment_with_report(current, increments):
    added_count = 0

    def missing():
        nonlocal added_count
        added_count += 1
        return 0

    result = defaultdict(missing, current)
    for key, amount in increments:
        result[key] += amount

    return result, added_count
