j = [i for i in input()]
s = [i for i in input()]
c = 0
for i in s:
    if i in j:
        c += 1
print(c)