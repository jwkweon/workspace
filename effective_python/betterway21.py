################                 BetterWay 21                 ################
# 키워드 전용 인수로 명료성을 강요하자
def safe_division(number, divisor, ignore_overflow,
                  ignore_zero_division):
    try:
        return number / divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        else:
            raise

result = safe_division(1, 10**500, True, False)
print(result)
result = safe_division(1, 0, False, True)
print(result)

def safe_division_b(number, divisor,
                  ignore_overflow=False,
                  ignore_zero_division=False):
    try:
        return number / divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        else:
            raise

result = safe_division_b(1, 10**500, ignore_overflow=True)
print(result)
result = safe_division_b(1, 0, ignore_zero_division=True)
print(result)

def safe_division_c(number, divisor, *,
                  ignore_overflow=False,
                  ignore_zero_division=False):
    try:
        return number / divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        else:
            raise

print(safe_division_c(1, 10**500, True, False))

safe_division_c(1, 0, ignore_zero_division=True)

try:
    safe_division_c(1, 0)
except ZeroDivisionError:
    pass

def print_args(*args, **kwargs):
    print('Positional :', args)
    print('Keyword    :', kwargs)

print_args(1, 2, foo='bar', stuff='meep')
