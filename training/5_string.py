# シングルクオート
print('abc')
# ダブルクオート
print("def")
# トリプルクオート
print("""abc
def""")
# エスケープ
print('\'')
# エスケープ
print("\"")
# 改行コード
print('abc\ndef')
# 連結
print('abc'+'def')
# 繰り返し
print('abc'*3)
# 型変換
print(str(10.6)+"%")
# 抽出
letters='abcdefghi'
print(letters[0])
print(letters[-1])
print(letters[:])
print(letters[:4])
print(letters[:4:2])
print(letters[:-3])
print(letters[-3:])
print(letters[-1::-1])
# 長さ
print(len('abc'))
print(len('あ'))
# 分割
print(letters.split('h'))
# 結合
strlist = ['abc','def','ghi']
print('@'.join(strlist))
# 除去
print(' abc '.strip())
# 置換
print('abchdefghi'.replace('h','@'))
# 探索
print('abcdefghi'.startswith('abc'))
print('abcdefghi'.startswith('bcd'))
print('abcdefghi'.endswith('ghi'))
print('abcdefghi'.endswith('bcd'))
print('abcabcabcabc'.find('bc'))
print('abcabcabcabc'.index('bc'))
print('abcabcabcabc'.rfind('bc'))
print('abcabcabcabc'.rindex('bc'))
print('abcabcabcabc'.count('bc'))
print('abcabcabcabc'.isalnum())
#大文字・小文字
print('abc def ghi'.capitalize())
print('abc def ghi'.title())
print('abc DEF ghi'.upper())
print('abc DEF ghi'.lower())
print('abc DEF ghi'.swapcase())
#配置
print('abc DEF ghi'.center(30))
print('abc DEF ghi'.ljust(30))
print('abc DEF ghi'.rjust(30))
#フォーマット
print('%s' % 10.5)
print('%d' % 10.5)
print('%x' % 10)
print('%o' % 10)
print('%f' % 10)
print('%e' % 10)
print('%g' % 10)
print('%d%%' % 10)
print('%12s' % 10.5)

#フォーマット（引数指定）
actor = 'Richrd Gere'
cat = 'Chester'
weight = 28
print("My wife's favorite actor is %s" % actor)
print("Our cat %s weighs %s pounds" % (cat, weight))

thing = 'woodchuck'
print('{}'.format(thing))
place='lake'
print('{} is in the {}'.format(thing, place))
print('{1} is in the {0}'.format(place, thing))

d = {'thing':'duck', 'place':'bathtub'}
print('The {0[thing]} is in the {0[place]}'.format(d))

thing = 'wereduck'
place = 'werepond'
print(f'The {thing} is in the {place}')
print(f'The {thing.capitalize()} is in the {place.rjust(20)}')
print(f'{thing:>20},{place:.^20}')
print(f'{thing=},{place=}')
print(f'{thing[-4:]=},{place.title()=}')
print(f'{thing=:>4.4}')

