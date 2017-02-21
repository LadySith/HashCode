import numpy as np

f = open('small.in', 'r')
z = []
z.append(list(map(int, f.readline().split())))
r = z[0][0]
c = z[0][1]
m = z[0][2]
n = z[0][3]

tcount = 0
mcount = 0

x = []

for line in f:
    x.append(list(line))
for i in range(0,r):
    x[i].remove("\n")
    tcount = tcount + x[i].count("T")
    mcount = mcount + x[i].count("M")
print(z)

x = np.array(x)
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



slices = []

for i in range(0,r):
    for j in range(0,c-m):
        a = x[i, j:(j+m)]
        if isSlice(a):
            slices.append[i, j, i, j+m]
        a[1][0] = a[1][2] = 0
        sum_arr.append(np.sum(a))



def isSlice(array):
    if (np.count_nonzero(array == least) >= l && np.count_nonzero(array == least) <= m-l):
        return true




input('Waiting for input...')
