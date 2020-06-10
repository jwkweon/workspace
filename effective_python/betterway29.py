# 메타클래스

Hello = type('Hello', (), {})
Hello
print(Hello)

h = Hello()
print(h)


def replace(self, old, new):
    while old in self:
        self[self.index(old)] = new


AdvancedList = type('AdvancedList', (list, ), {
                    'desc': 'Advanced list', 'replace': replace})

x = AdvancedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
x.replace(1, 100)
print(x)
print(x.desc)

print('====')


class meta(type):
    def __new__(metacls, name, bases, namespace):
        pass


class MakeCalc(type):
    def __new__(metacls, name, bases, namespace):
        namespace['desc'] = 'cal class'
        namespace['add'] = lambda self, a, b: a + b
        return type.__new__(metacls, name, bases, namespace)


Calc = MakeCalc('Calc', (), {})
c = Calc()
print(c.desc)
print(c.add(1, 2))
