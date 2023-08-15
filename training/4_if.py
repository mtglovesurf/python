"""
# 60 sec/min * 60 min/hr * 24 hr/day
seconds_per_day = 86400

seconds_per_day = 86400 # 60 sec/min * 60 min/hr * 24 hr/day

# I can say anything here, even if Python doesn't lile it,
# because I'm prtected by the awesome
# octothorpe.

print('No comment:quotes make the " harmless.')

total = 0
total += 1
total += 2
total += 3
total += 4
print(total)

total = 1+\
2+\
3+\
4
print(total)

total = (
1+
2+
3+
4
)
print(total)

disaster = True
if disaster:
    print("Woe!")
else:
    print("Whee!")

furry = True
large = True
if furry:
    if large:
        print("It's a yeti")
    else:
        print("It's a cat!")
else:
    if large:
        print("It's a whale!")
    else:
        print("It's a human. Or a hairless cat.")

color = "mauve"
if color == "red":
    print("It's a tomato")
elif color == "green":
    print("It's a green pepper")
elif color == "bee purple":
    print("I don't know what it is, but only bees can see it")
else:
    print("I've never heard of the color", color)

x=7
print(x == 5)
print(x == 7)
print(5<x)
print(x<10)
print(5<x or x<10)
print(5<x and x>10)
print(5<x and not x>10)
print(5<x<10)
print(5<x<10<999)

some_list=[]
if some_list:
    print("There's something in here")
else:
    print("Hey, It's empty!")

letter = "o"
if letter=='a' or letter=='e' or letter=='i'\
or letter=='o' or letter=='u':
    print(letter, 'is a vowel')
else:
    print(letter, 'is not a vowel')

vowels = 'aeiou'
letter = 'o'
print(letter in vowels)

vowel_set={'a','e','i','o','u'}
print(letter in vowel_set)
vowel_list=['a','e','i','o','u']
print(letter in vowel_list)
vowel_tupple=('a','e','i','o','u')
print(letter in vowel_tupple)
vowel_dict={'a':'apple','e':'elephant','i':'impala','o':'ocelot','u':'unicorn'}
print(letter in vowel_dict)
vowel_string="aeiou"
print(letter in vowel_string)
"""

tweet_limit=280
tweet_string="Blah"*50
#diff=tweet_limit-len(tweet_string)
#if diff>=0:
if (diff:=tweet_limit-len(tweet_string)>=0):
    print("A fitting tweet")
else:
    print("Went over by", abs(diff))


