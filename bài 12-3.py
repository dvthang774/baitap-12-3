import random, string

n = random.randint(50,100)
print('Số list n:', n)
for i in range(n):
    tt = dict()
    d = random.randint(2,6)
    g = random.choice(string.ascii_lowercase)
    ch = g + ''.join(random.choice(string.ascii_lowercase) for _ in range(d - 1))
    tt['name'] = ch
    tuoi = random.randint(1,100)
    tt['age'] =tuoi
    list.append(tt)
print(list)
for index, value in enumerate(list, 1):
    print(f'{index}: {value}')



