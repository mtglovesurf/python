empty_dict = {}
print(empty_dict)

bierce = {
    "day": "A period of twenty-four hours, mostly misspent",
    "positive": "Mistaken at the top of one's voice",
    "misfortune": "The kind of fortune that never misses",
}
print(bierce)

acme_customer = {'first': 'Wile', 'middle': 'E', 'last': 'Coyote'}
print(acme_customer)

acme_customer = dict(first="Wile", middle="E", last="Coyote")
print(acme_customer)

lol = [['a', 'b'], ['c', 'd'], ['e', 'f']]
print(lol)
print(dict(lol))

lot = [('a', 'b'), ('c', 'd'), ('e', 'f')]
print(lol)
print(dict(lol))

los = ['ab', 'cd', 'ef']
print(los)
print(dict(los))

tos = ('ab', 'cd', 'ef')
print(tos)
print(dict(tos))

pythons = {
   'Chapman': 'Graham',
   'Cleese': 'John',
   'Idle': 'Eric',
   'Jones': 'Terry',
   'Palin': 'Michael',
}
print(pythons)
pythons['Gilliam'] = 'Gerry'
print(pythons)
pythons['Gilliam'] = 'Terry'
print(pythons)

some_pythons = {
    'Graham': 'Chapman',
    'John': 'Cleese',
    'Eric': 'Idle',
    'Terry': 'Gilliam',
    'Michael': 'Palin',
    'Terry': 'Jones',
}

print(some_pythons)

print(some_pythons['John'])

# 存在しないキーを指定するとエラーとなる
# 条件文（if 'Groucho' in some_pythons:）を付けて回避する
# print(some_pythons['Groucho'])

print(some_pythons.get('John'))

print(some_pythons.get('Groucho', 'Not a Python'))

print(some_pythons.get('Groucho'))

signals = {'green': 'go', 'yellow': 'go faster', 'red': 'smile for the camera'}
print(signals.keys())
print(list(signals.keys()))
print(signals.values())
print(list(signals.values()))
print(len(signals))

first = {'a': 'agony', 'b': 'bliss'}
second = {'b': 'bagels', 'c': 'candy'}
third = {'d': 'donuts'}
print({**first, **second, **third})

pythons = {
    'Chapman': 'Graham',
    'Cleese': 'John',
    'Gilliam': 'Terry',
    'Idle': 'Eric',
    'Jones': 'Terry',
    'Palin': 'Michael',
}
print(pythons)

others = {'Marx': 'Groucho', 'Howard': 'Moe'}
print(others)

pythons.update(others)
print(pythons)

first = {'a': 1, 'b': 2}
second = {'b': 'platypus'}
first.update(second)
print(first)

del pythons['Marx']
print(pythons)
del pythons['Howard']
print(pythons)

print(pythons.pop('Palin'))
print(pythons)
print(pythons.pop('First','Hugo'))
print(len(pythons))

pythons.clear()
print(pythons)

pythons = {'Chapman': 'Graham', 'Cleese': 'John',
'Jones': 'Terry', 'Palin': 'Michael', 'Idle': 'Eric'}
print('Chapman' in pythons)
print('Palin' in pythons)
print('Gilliam' in pythons)

# =による代入
signals = {'green': 'go',
'yellow': 'go faster',
'red': 'smile for the camera'}
save_signals = signals
signals['blue'] = 'confuse everyone'
print(save_signals)

signals = {'green': 'go',
'yellow': 'go faster',
'red': 'smile for the camera'}
original_signals = signals.copy()
signals['blue'] = 'confuse everyone'
print(signals)
print(original_signals)

#shallow_copy
signals = {'green': 'go',
'yellow': 'go faster',
'red': ['stop', 'smile']}
signals_copy = signals.copy()
signals['red'][1] = 'sweat'
print(signals)
print(signals_copy)

#deep_copy
import copy
signals = {'green': 'go',
'yellow': 'go faster',
'red': ['stop', 'smile']}
signals_copy = copy.deepcopy(signals)
signals['red'][1] = 'sweat'
print(signals)
print(signals_copy)

#辞書の比較（==と!=のみ）
a = {1: 1, 2: 2, 3: 3}
b = {3: 3, 1: 1, 2: 2}
print(a == b)

a = {1: [1, 2], 2: [1], 3: [1]}
b = {1: [1, 1], 2: [1], 3: [1]}
print(a != b)

#forとinによる反復処理
accusation = {'room': 'ballroom', 'weapon': 'lead pipe','person': 'Col. Mustard'}
#キーのみ
for card in accusation.keys():
    print(card)
#値のみ
for value in accusation.values():
    print(value)
#キーと値
for item in accusation.items():
    print(item)
for card, contents in accusation.items():
    print('Card', card, 'has the contents', contents)

#辞書内包表記
word = 'letters'
letter_counts = {letter: word.count(letter) for letter in word}
print(letter_counts)

word = 'letters'
letter_counts = {letter: word.count(letter) for letter in set(word)}
print(letter_counts)

vowels = 'aeiou'
word = 'onomatopoeia'
vowel_counts = {letter: word.count(letter) for letter in set(word) if letter in vowels}
print(vowel_counts)

##集合

#set()による生成
empty_set = set()
print(empty_set)

even_numbers = {0, 2, 4, 6, 8}
print(even_numbers)

odd_numbers = {1, 3, 5, 7, 9}
print(odd_numbers)

#set()による変換
print('letters')
print(set('letters'))
print(set(['Dasher', 'Dancer', 'Prancer', 'Mason-Dixon']))
print(set(('Ummagumma', 'Echoes', 'Atom Heart Mother')))
print(set({'apple': 'red', 'orange': 'orange', 'cherry': 'red'}))
reindeer = set(['Dasher','Dasher', 'Dancer', 'Prancer', 'Mason-Dixon'])
print(len(reindeer))

#add()による要素の追加
s = set((1, 2, 3))
print(s)
s.add(4)
print(s)

#remove()による要素の削除
s = set((1, 2, 3))
s.remove(3)
print(s)

#forとinによる反復処理
furniture = set(('sofa', 'ottoman', 'table'))
for piece in furniture:
    print(piece)

#inによる値の有無テスト
drinks = {
    'martini': {'vodka', 'vermouth'},
    'black russian': {'vodka', 'kahlua'},
    'white russian': {'cream', 'kahlua', 'vodka'},
    'manhattan': {'rye', 'vermouth', 'bitters'},
    'screwdriver': {'orange juice', 'vodka'}
}
for name, contents in drinks.items():
    if 'vodka' in contents:
        print(name)

for name, contents in drinks.items():
    if 'vodka' in contents and not ('vermouth' in contents or 'cream' in contents):
        print(name)

#組み合わせと集合演算
for name, contents in drinks.items():
    if contents & {'vermouth', 'orange juice'}:
        print(name)

for name, contents in drinks.items():
    if 'vodka' in contents and not contents & {'vermouth', 'cream'}:
        print(name)

a = {1, 2}
b = {2, 3}
print(a&b)
print(a.intersection(b))
print(a|b)
print(a.union(b))
print(a-b)
print(a.difference(b))
print(a^b)
print(a.symmetric_difference(b))
print(a<=b)
print(a.issubset(b))
print(a<=a)
print(a<a)
print(a.issubset(a))
print(a>=a)
print(a>a)
print(a.issubset(a))

bruss = drinks['black russian']
wruss = drinks['white russian']
print(bruss|wruss)
print(bruss-wruss)
print(wruss-bruss)
print(bruss^wruss)
print(bruss<=wruss)
print(bruss<wruss)
print(wruss>=bruss)
print(wruss>bruss)

#集合内包表記
a_set = {number for number in range(1, 6) if number % 3 == 1}
print(a_set)

#frozenset()によるイミュータブルな集合の作成
fs = frozenset([3, 2, 1])
print(fs)

#今までに取り上げてきたデータ構造
marx_list = ['Groucho', 'Chico', 'Harpo']
marx_tuple = ('Groucho', 'Chico', 'Harpo')
marx_dict = {'Groucho': 'banjo', 'Chico': 'piano', 'Harpo': 'harp'}
marx_set = {'Groucho', 'Chico', 'Harpo'}
marx_list[2]
marx_tuple[2]
marx_dict['Harpo']
print('Harpo' in marx_list)
print('Harpo' in marx_tuple)
print('Harpo' in marx_dict)
print('Harpo' in marx_set)

#もっと大きいデータ構造
marxes = ['Groucho', 'Chico', 'Harpo']
pythons = ['Chapman', 'Cleese', 'Gilliam', 'Jones', 'Palin', 'Eric']
stooges = ['Moe', 'Curly', 'Larry']

tuple_of_lists = marxes, pythons, stooges
print(tuple_of_lists)

list_of_lists = [marxes, pythons, stooges]
print(list_of_lists)

dict_of_lists = {'Marxes': marxes, 'Pythons': pythons, 'Stooges': stooges}
print(dict_of_lists)

houses = {
    (44.79, -93.14, 285): 'My House',
    (38.89, -77.03, 13): 'The White House'
}
print(houses[(44.79, -93.14, 285)])