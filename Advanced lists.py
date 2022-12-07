t = [[3-i for i in range(3)] for j in range (3)]
s = 0
for i in range (3):
    s += t[i][i]
print(s)

p = [[[x*3 for x in range(3)] for z in range(2)] for w in range(3)]
print(p)