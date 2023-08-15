""""
empty_tuple = ()
print(empty_tuple)

one_marx='Groucho',
print(one_marx)

one_marx=('Groucho',)
print(one_marx)

one_marx=('Groucho')
print(one_marx)
print(type(one_marx))

marx_tuple='Groucho','Chico','Harpo'
print(marx_tuple)

marx_tuple=('Groucho','Chico','Harpo')
print(marx_tuple)

one_marx='Groucho',
print(type(one_marx))
print(type('Groucho',))
print(type(('Groucho',)))

marx_tuple=('Groucho','Chico','Harpo')
a,b,c=marx_tuple
print(a)
print(b)
print(c)

password='swordfish'
icecream='tuttifrutti'
password,icecream = icecream, password
print(password)
print(icecream)

marx_list = ['Groucho','Chico','Harpo']
print(tuple(marx_list))

print(('Groucho',) + ('Chico','Harpo'))

print(('yada',)*3)

a = (7,2)
b = (7,2,9)
print(a==b)
print(a<b)

words = ("fresh","out","of","ideas")
for word in words:
    print(word)

t1 = ('Fee','Fie','Foe')
t2 = ('Flop',)
print(t1+t2)

t1 = ('Fee','Fie','Foe')
print(id(t1))
t2 = ('Flop',)
t1 += t2
print(t1)
print(id(t1))

empty_list=[]
print(empty_list)
weekdays=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturaday','Sunday']
print(weekdays)
big_birds=['emu','ostrich','cassowary']
print(big_birds)
first_names=['Graham','John','Terry','Terry','Michael','Eric']
print(first_names)
leap_years=[2000,2004,2008]
print(leap_years)
randomness=['Punxsatawney',{"groundhog":"Phil"},"Feb.2"]
print(randomness)

another_empty_list=list()
print(another_empty_list)

print(list("cat"))

a_tuple = ('ready','fire','aim')
print(list(a_tuple))

talk_like_a_pirate_day='9/19/2019'
print(talk_like_a_pirate_day.split('/'))

splitme='a/b//c/d///e'
print(splitme.split('/'))
print(splitme.split('//'))

marxes=['Groucho','Chico','Harpo']
print(marxes[0])
print(marxes[1])
print(marxes[2])
print(marxes[-3])
print(marxes[-2])
print(marxes[-1])

marxes=['Grousho','Chico','Harpo']
print(marxes[0:2])
print(marxes[::2])
print(marxes[::-2])
print(marxes[::-1])

marxes=['Grousho','Chico','Harpo']
marxes.reverse()
print(marxes)

marxes=['Grousho','Chico','Harpo']
print(marxes[4:])
print(marxes[-6:])
print(marxes[-6:-2])
print(marxes[-6:-4])

marxes=['Grousho','Chico','Harpo']
marxes.append('Zeppo')
print(marxes)

marxes=['Grousho','Chico','Harpo']
marxes.insert(2,'Gummo')
print(marxes)
marxes.insert(10,'Zeppo')
print(marxes)

print(["blah"]*3)

marxes=['Grousho','Chico','Harpo']
others=['Gummo','Karl']
marxes.extend(others)
print(marxes)

marxes=['Grousho','Chico','Harpo']
others=['Gummo','Karl']
marxes+=others
print(marxes)

marxes=['Grousho','Chico','Harpo']
others=['Gummo','Karl']
marxes.append(others)
print(marxes)

marxes=['Grousho','Chico','Harpo']
others=['Gummo','Karl']
marxes.insert(2,others)
print(marxes)

marxes=['Grousho','Chico','Harpo']
marxes[2]='Wanda'
print(marxes)

numbers=[1,2,3,4]
numbers[1:3]=[8,9]
print(numbers)

numbers=[1,2,3,4]
numbers[1:3]=[7,8,9]
print(numbers)

numbers=[1,2,3,4]
numbers[1:3]=[]
print(numbers)

numbers=[1,2,3,4]
numbers[1:3]=(98,99,100)
print(numbers)

numbers=[1,2,3,4]
numbers[1:3]="wat?"
print(numbers)

marxes=['Grousho','Chico','Harpo','Gummo','Karl']
print(marxes[-1])
del marxes[-1]
print(marxes)

marxes=['Grousho','Chico','Harpo','Gummo']
print(marxes)
del marxes[1]
print(marxes)

marxes=['Groucho','Chico','Harpo']
marxes.remove('Groucho')
print(marxes)

marxes=['Groucho','Chico','Harpo','Zeppo']
print(marxes.pop())
print(marxes)
print(marxes.pop(1))
print(marxes)

work_quotes = ['Working hard?', 'Quick question!', 'Number one priorities!']
print(work_quotes)
work_quotes.clear()
print(work_quotes)

marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
print(marxes.index('Chico'))

simpsons = ['Lisa', 'Bart', 'Marge', 'Homer', 'Bart']
print(simpsons.index('Bart'))

marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
print('Groucho' in marxes)
print('Bob' in marxes)
False

words = ['a', 'deer', 'a', 'female', 'deer']
print('deer' in words)

marxes = ['Groucho', 'Chico', 'Harpo']
print(marxes.count('Harpo'))
print(marxes.count('Bob'))

snl_skit = ['cheeseburger', 'cheeseburger', 'cheeseburger']
print(snl_skit.count('cheeseburger'))

marxes = ['Groucho', 'Chico', 'Harpo']
print(', '.join(marxes))

friends = ['Harry', 'Hermione', 'Ron']
separator = ' * '
joined = separator.join(friends)
print(joined)
separated = joined.split(separator)
print(separated)
print(separated == friends)

marxes = ['Groucho', 'Chico', 'Harpo']
sorted_marxes = sorted(marxes)
print(sorted_marxes)
marxes.sort()
print(marxes)

numbers = [2, 1, 4.0, 3]
numbers.sort()
print(numbers)

numbers = [2, 1, 4.0, 3]
numbers.sort(reverse=True)
print(numbers)

marxes = ['Groucho', 'Chico', 'Harpo']
print(len(marxes))

a = [1, 2, 3]
print(a)
b = a
print(b)
a[0] = 'surprise'
print(a)
print(b)

b[0] = 'I hate surprises'
print(b)
print(a)

a = [1, 2, 3]
b = a.copy()
c = list(a)
d = a[:]
a[0] = 'integer lists are boring'
print(a)
print(b)
print(c)
print(d)

a = [1, 2, [8, 9]]
b = a.copy()
c = list(a)
d = a[:]
a[2][1] = 10
print(a)
print(b)
print(c)
print(d)

import copy
a = [1, 2, [8, 9]]
b = copy.deepcopy(a)
a[2][1] = 10
print(a)
print(b)

a = [7, 2]
b = [7, 2, 9]
print(a == b)
print(a <= b)
print(a < b)

cheeses = ['brie', 'gjetost', 'havarti']
for cheese in cheeses:
     print(cheese)

cheeses = ['brie', 'gjetost', 'havarti']
for cheese in cheeses:
     if cheese.startswith('g'):
         print("I won't eat anything that starts with 'g'")
         break
     else:
         print(cheese)

cheeses = ['brie', 'gjetost', 'havarti']
for cheese in cheeses:
     if cheese.startswith('x'):
         print("I won't eat anything that starts with 'x'")
         break
     else:
         print(cheese)
else:
     print("Didn't find anything that started with 'x'")

cheeses = []
for cheese in cheeses:
    print('This shop has some lovely', cheese)
    break
else:  # breakされなければチーズはない
    print('This is not much of a cheese shop, is it?')

days = ['Monday', 'Tuesday', 'Wednesday']
fruits = ['banana', 'orange', 'peach']
drinks = ['coffee', 'tea', 'beer']
desserts = ['tiramisu', 'ice cream', 'pie', 'pudding']
for day, fruit, drink, dessert in zip(days, fruits, drinks, desserts):
    print(day, ": drink", drink, "- eat", fruit, "- enjoy", dessert)

english = 'Monday', 'Tuesday', 'Wednesday'
french = 'lundi', 'mardi', 'mercredi'
print(list(zip(english, french)))
print(dict(zip(english, french)))

number_list = []
number_list.append(1)
number_list.append(2)
number_list.append(3)
number_list.append(4)
number_list.append(5)
print(number_list)

number_list = []
for number in range(1, 6):
    number_list.append(number)
else:
    print(number_list)

number_list = list(range(1, 6))
print(number_list)

number_list = [number for number in range(1,6)]
print(number_list)

number_list = [number-1 for number in range(1,6)]
print(number_list)

a_list = [number for number in range(1, 6) if number % 2 == 1]
print(a_list)

a_list = []
for number in range(1, 6):
    if number % 2 == 1:
        a_list.append(number)
print(a_list)

rows = range(1, 4)
cols = range(1, 3)
for row in rows:
    for col in cols:
        print(row, col)

rows = range(1, 4)
cols = range(1, 3)
cells = [(row, col) for row in rows for col in cols]
for cell in cells:
    print(cell)

for row, col in cells:
    print(row, col)

small_birds = ['hummingbird', 'finch']
extinct_birds = ['dodo', 'passenger pigeon', 'Norwegian Blue']
carol_birds = [3, 'French hens', 2, 'turtledoves']
all_birds = [small_birds, extinct_birds, 'macaw', carol_birds]
print(all_birds)
print(all_birds[0])
print(all_birds[1])
print(all_birds[1][0])
"""
number_thing = (number for number in range(1, 6))
print(number_thing)