################                 BetterWay 17                 ################
# 인수를 순회할 때는 방어적으로 하자
import os

os.path.abspath(' ')
os.getcwd()

def normalize(numbers):
    #total = 100
    total = sum(numbers)   #sum(numbers)에서 이터레이터 소진
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result

visits = [15, 35, 80]
percentages = normalize(visits)
print(percentages)

def read_visits(data_path):
    with open(data_path) as f:
        for line in f:
            yield int(line)

it = read_visits('./num.txt')
percentages = normalize(it)
print(percentages)

def normalize_copy(numbers):
    numbers = list(numbers)
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result

it = read_visits('./num.txt')
percentages = normalize_copy(it)
print(percentages)

def normalize_func(get_iter):
    total = sum(get_iter())
    result = []
    for value in get_iter():
        percent = 100 * value / total
        result.append(percent)
    return result

path = './num.txt'
percentages = normalize_func(lambda: read_visits(path))
print(percentages)

class ReadVisits(object):
    def __init__(self, data_path):
        self.data_path = data_path

    def __iter__(self):
        with open(self.data_path) as f:
            for line in f:
                yield int(line)

visits = ReadVisits('./num.txt')
percentages = normalize(visits)
print(percentages)

a = [10, 15, 30]
b = iter(visits)
if iter(b) is iter(b):
    print('zzz')

if iter(visits) is iter(visits):
    print('zzz')

def normalize_defensive(numbers):
    if iter(numbers) is iter(numbers):
        raise TypeError('Must supply a container')
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result

visits = [15, 35, 80]
normalize_defensive(visits)
visits = ReadVisits('./num.txt')
normalize_defensive(visits)

it = iter(visits)
normalize_defensive(it)
