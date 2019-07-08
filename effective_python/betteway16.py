################                 BetterWay 16                 ################
# 리스트를 반환하는 대신 제너레이터를 고려하자
import os
from itertools import islice

def index_words(text):
    result = []
    if text:
        result.append(0)
    for index, letter in enumerate(text):
        if letter == ' ':
            result.append(index + 1)
    return result

def index_words_iter(text):
    if text:
        yield 0
    for index, letter in enumerate(text):
        if letter == ' ':
            yield index + 1

def index_file(handle):
    offset = 0
    for line in handle:
        if line:
            yield offset
        for letter in line:
            offset += 1
            if letter == ' ':
                yield offset

text1 = 'a aa aaa aaaa'
print(index_words(text=text1))
print(index_words_iter(text='aaa aaa aaaa aaaa'))
result = list(index_words_iter(text='aaa aaa aaaa aaaa'))
print(result)

print(os.getcwd())
f_path = os.path.abspath('address.txt')
print(f_path)
os.chdir('C:\zzu0203.github.io\workspace\effective_python\\')

with open(f_path, 'r') as f:
    it = index_file(f)
    results = islice(it, 0, 3)
    print(list(results))
