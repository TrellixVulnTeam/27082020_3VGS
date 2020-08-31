'''Functions'''


def fn(*arg):
    print(type(arg))
    print(arg)


fn()
fn(1, 'a', None, False)


def greet(name, *arg):
    lst = list((name,) + arg)
    hi = 'Hello, ' + ' and '.join(lst) + '!'
    return hi


print(greet('Tom', 'Ann'))
print(greet('Bob'))

print('|-------------------------------------------------------------------|\n')

def bar(length, char1='-', char2='*'):
    return (char1 + char2) * length + char1

print(bar(5, '-', '*'))
print(bar(5))
print(bar(3, '.'))
print(bar(3, ':', '|'))
print(bar(3, char2='#'))
print(bar(char2='$', length=3))

def f(*args, x=None, y=None):
    print('args =', args, ', x =', x, ', y =', y)

f(*(1, 2), x='a', *[3, 4], y='b', *(5, 6))
#args = (1, 2, 3, 4, 5, 6), x = a, y = b

def f1(x, y):
    print(x, y)
f1(x=1, y=2)
f1(1, 2)
f1(1, y=2)
#f1(y=2, 1) error point
#f1(x=1, 2) error point


print('|-------------------------------------------------------------------|\n')

def rgb(red=0, green=0, blue=0):
    return 'rgb({}, {}, {})'.format(red, green, blue)


# BEGIN (write your solution here)
def get_colors(*args):
    colors = {'red': rgb(red=255), 'green': rgb(green=255), 'blue': rgb(blue=255)}
    return colors

    # return {
    #     'red': rgb(red=255),
    #     'green': rgb(green=255),
    #     'blue': rgb(blue=255),
    # }


colors = get_colors()
set(colors.keys()) == {'red', 'green', 'blue'}
print(colors['red'])
print(colors['blue'])
print(colors['green'])

for (i, v) in colors.items():
    print(f'i: {i} - v: {type(v)}')