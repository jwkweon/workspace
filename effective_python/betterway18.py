################                 BetterWay 18                 ################
# 가변 위치 인수로 깔끔하게 보이게 하자
def log(message, values):
    if not values:
        print(message)
    else:
        value_str = ', '.join(str(x) for x in values)
        print('%s: %s' % (message, value_str))

log('My nums are', [1, 2])
log('Hi there', [])

def log(message, *values):
    if not values:
        print(message)
    else:
        value_str = ', '.join(str(x) for x in values)
        print('%s: %s' % (message, value_str))

log('My nums are', [1, 2])
log('Hi there')

favorites = [7, 33, 99]
log('Favorite colors', *favorites)

def my_generator():
    for i in range(10):
        yield i

def my_func(*args):
    print(args)

it = my_generator()
my_func(*it)

def log(sequence, message, *values):
    if not values:
        print('%s: %s' % (sequence, message))
    else:
        value_str = ', '.join(str(x) for x in values)
        print('%s: %s: %s' % (sequence, message, value_str))

log(1, 'Favorites', 7, 33)
log('Favorites', 7, 33)
