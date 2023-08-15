def do_nothing():
    pass

do_nothing()

def make_a_sound():
    print('quack')

make_a_sound()

def agree():
   return True

if agree():
    print('Splendid!')
else:
    print('That was unexpected.')

def echo(anything):
   return anything + ' ' + anything

print(echo('Rumplestiltskin'))

def commentary(color):
    if color == 'red':
        return "It's a tomato."
    elif color == "green":
        return "It's a green pepper."
    elif color == 'bee purple':
        return "I don't know what it is, but only bees can see it."
    else:
        return "I've never heard of the color "  + color +  "."

comment = commentary('blue')
print(comment)

print(do_nothing())

thing = None

if thing:
    print("It's some thing")
else:
    print("It's no thing")

def whatis(thing):
    if thing is None:
        print(thing, "is None")
    elif thing:
        print(thing, "is True")
    else:
        print(thing, "is False")

whatis(None)
whatis(True)
whatis(False)
whatis(0)
whatis(0.0)
whatis('')
whatis("")
whatis("""""")
whatis(())
whatis({})
whatis(set())
whatis(0.00001)
whatis([0])
whatis([''])
whatis(' ')

def menu(wine, entree, dessert):
    return {'wine': wine, 'entree': entree, 'dessert': dessert}

print(menu('chardonnay', 'chicken', 'cake'))
print(menu(entree='chicken', dessert='cake', wine='chardonnay'))
print(menu('chardonnay',entree='chicken', dessert='cake'))

def menu(wine, entree, dessert='pudding'):
    return {'wine': wine, 'entree': entree, 'dessert': dessert}

print(menu('chardonnay', 'chicken'))
print(menu('chardonnay', 'chicken', 'cake'))

def buggy(arg, result=[]):
    result.append(arg)
    print(result)

buggy('a')
buggy('b')

def works(arg):
    result = []
    result.append(arg)
    return result

print(works('a'))
print(works('b'))

def print_args(*args):
    print('Positional tuple:', args)

print_args()
print_args(3, 2, 1, 'wait!', 'uh...')
print_args(2, 5, 7, 'x')
args = (2, 5, 7, 'x')
print_args(args)
print_args(*args)

def print_more(required1, required2, *args):
    print('Need this one:', required1)
    print('Need this one too:', required2)
    print('All the rest:', args)

print_more('cap', 'gloves', 'scarf', 'monocle', 'mustache wax')

def print_kwargs(**kwargs):
    print('Keyword arguments:', kwargs)

print_kwargs()
print_kwargs(wine='merlot', entree='mutton', dessert='macaroon')

def print_data(data, *, start=0, end=100):
    for value in (data[start:end]):
        print(value)

data = ['a', 'b', 'c', 'd', 'e', 'f']
print_data(data)
print_data(data, start=4)
print_data(data, end=2)

outside = ['one', 'fine', 'day']
def mangle(arg):
   arg[1] = 'terrible!'

mangle(outside)
print(outside)

def echo(anything):
    """echoは、与えられた入力引数を返す。"""
    return anything

print(echo(1.0))
help(echo)
print(echo.__doc__)

def print_if_true(thing, check):
    """
    第2引数が真なら、第1引数を表示する
    処理内容:
        1. 第2引数が真かどうかをチェックする。
        2. 真なら第1引数を表示する。
    """
    if check:
        print(thing)

print(print_if_true(True,"Hoge"))
help(print_if_true)
print(print_if_true.__doc__)

def answer():
    print(42)

answer()

def run_something(func):
    func()

run_something(answer)

def add_args(arg1, arg2):
    print(arg1 + arg2)

def run_something_with_args(func, arg1, arg2):
    func(arg1, arg2)

run_something_with_args(add_args, 5, 9)

def sum_args(*args):
   return sum(args)

def run_with_positional_args(func, *args):
   return func(*args)

print(run_with_positional_args(sum_args, 1, 2, 3, 4))

def outer(a, b):
    def inner(c, d):
        return c + d
    return inner(a, b)

print(outer(4, 7))

def knights(saying):
    def inner(quote):
        return f"We are the knights who say: '{quote}'"
    return inner(saying)

print(knights('Ni!'))

def knights2(saying):
    def inner2():
        return f"We are the knights who say: '{saying}'"
    return inner2

a = knights2('Duck')
b = knights2('Hasenpfeffer')
print(type(a))
print(type(b))
print(a)
print(b)
print(a())
print(b())

def edit_story(words, func):
    for word in words:
        print(func(word))

def enliven(word):
    return word.capitalize() + '!'

stairs = ['thud', 'meow', 'thud', 'hiss']
edit_story(stairs, enliven)

print(sum(range(1, 101)))

def my_range(first=0, last=10, step=1):
    number = first
    while number < last:
        yield number
        number += step

range = my_range(1,5)

for x in range:
    print(x)

for try_again in range:
    print(try_again)

genobj = (pair for pair in zip(['a', 'b'], ['1', '2']))
print(genobj)

for thing in genobj:
    print(thing)

def document_it(func):
    def new_function(*args, **kwargs):
        print('Running function:', func.__name__)
        print('Positional arguments:', args)
        print('Keyword arguments:', kwargs)
        result = func(*args, **kwargs)
        print('Result:', result)
        return result
    return new_function

def add_ints(a, b):
   return a + b

print(add_ints(3, 5))
cooler_add_ints = document_it(add_ints)
print(cooler_add_ints(3, 5))

@document_it
def add_ints(a, b):
    return a + b

add_ints(3, 5)

def square_it(func):
    def new_function(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * result
    return new_function

@document_it
@square_it
def add_ints(a, b):
    return a + b

print(add_ints(3, 5))

@square_it
@document_it
def add_ints(a, b):
    return a + b

print(add_ints(3, 5))

animal = 'fruitbat'
def print_global():
    print('inside print_global:', animal)
print('at the top level:', animal)
print_global()

animal = 'fruitbat'
def change_and_print_global():
    global animal
    animal = 'wombat'
    print('inside change_and_print_global:', animal)

change_and_print_global()

animal = 'fruitbat'
def change_local():
    animal = 'wombat'
    print('locals:', locals())

print(animal)
change_local()
print('globals:', globals())
print(animal)

def amazing():
    """これはすばらしい関数だ。
    もう一度見る?"""
    print('この関数の名前:', amazing.__name__)
    print('関数のdocstring:', amazing.__doc__)

amazing()

def dive():
    return dive()

#dive()

def flatten(lol):
    for item in lol:
        if isinstance(item, list):
            for subitem in flatten(item):
                yield subitem
        else:
            yield item

lol = [1, 2, [3,4,5], [6,[7,8,9], []]]
flatten(lol)
print(list(flatten(lol)))

def flatten(lol):
    for item in lol:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item

lol = [1, 2, [3,4,5], [6,[7,8,9], []]]
print(list(flatten(lol)))

short_list = [1, 2, 3]
position = 5
try:
    hort_list[position]
except:
    print('Need a position between 0 and', len(short_list) - 1, ' but got', position)

short_list = [1, 2, 3]
while True:
    value = input('Position [q to quit]? ')
    if value == 'q':
        break
    try:
        position = int(value)
        print(short_list[position])
    except IndexError as err:
        print('Bad index:', position)
    except Exception as other:
        print('Something else broke:', other)

class UppercaseException(Exception):
    pass

words = ['eenie', 'meenie', 'miny', 'MO']
for word in words:
    if word.isupper():
        try:
            raise UppercaseException(word)
        except Exception as other:
            print(other)