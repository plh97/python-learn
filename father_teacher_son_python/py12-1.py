# 可变循环


letters = ['a','b','c','d','e']


print(letters[:]==letters)

letters.append(['123123'])
letters.extend(['123123'])

letters.insert(2,'zzzzzzzzz')
letters.remove('b')

print(letters[1:])
print('c' in letters)
news = letters[:]
print(news==letters)