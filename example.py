import numpy as np

f = open('small.in', 'r')
z = []
z.append(list(map(int, f.readline().split())))
r = z[0][0]
c = z[0][1]
n = z[0][2]
m = z[0][3]

tcount = 0
mcount = 0

x = []

for line in f:
    x.append(list(line))
for i in range(0,r):
    x[i].remove("\n")
    tcount = tcount + x[i].count('T')
    mcount = mcount + x[i].count('M')
print(z)

x = np.array(x)
print(x)
print('\nVars:')
print('Tomatos: ' + str(tcount))
print('Mushrooms: ' + str(mcount))
print('Min no of each: ' + str(n))
print('Max size of slice: ' + str(m))

mode = ""
perslice = 0

if (tcount < mcount):
    mode = 'T'
else:
    mode = 'M'

def isSlice(array):
    if (np.count_nonzero(array == mode) == n):
        return 1
    else:
        return 0

slices = []

for i in range(0,r):
    for j in range(0,c-(2*n)+1):
        a = x[i, j:(j+(2*n))]
        if (isSlice(a) == 1):
            slices.append([i, j, i, (j+(2*n)-1)])

print('No of slices: ' + str(len(slices)))
print(slices)


input('Hold...')
