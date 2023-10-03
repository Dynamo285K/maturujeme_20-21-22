import string
from collections import Counter

letters = string.ascii_lowercase

res = ''
with open('tabulka_pocetnosti.txt','r') as fp:
    for line in fp:
        lower = line.lower()
        res += lower
        res = res.replace('\n','')
    print(res)

c = Counter(res)
print(c)

for i in c.keys():
    if i in letters:
        print(i.upper(),'-',c[i])



