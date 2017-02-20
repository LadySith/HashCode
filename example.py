
f = open('big.in', 'r')
x = []
x.append(list(map(int, f.readline().split())))
r = x[0][0]
c = x[0][1]
m = x[0][2]
n = x[0][3]

tcount = 0
mcount = 0

for line in f:
    x.append(list(line))
for i in range(0,r):
    x[i + 1].remove("\n")
    tcount = tcount + x[i + 1].count("T")
    mcount = mcount + x[i + 1].count("M")
print(x)
print('Tomatos: ' + str(tcount))
print('Mushrooms: ' + str(mcount))
print(m)
print(n)

mode = ''
perslice = 0

if (tcount < mcount):
    mode = "T"
    perslice = tcount/m
else:
    mode = "M"
    perslice = mcount/m


input('Waiting for input...')
