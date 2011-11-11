from operator import itemgetter

f = open("input.txt")

buf = f.readlines()
first = buf[0].rstrip()
last = buf[1].rstrip()
length = int(buf[2])
ldi = buf[3:]
ldict = []

for word in ldi :
    ldict.append(word.rstrip())

def ldist(s1, s2) :
    l1 = len(s1)
    l2 = len(s2)

    matrix = [range(l1 + 1)] * (l2 + 1)
    for zz in range(l2 + 1) :
        matrix[zz] = range(zz,zz + l1 + 1)
    for zz in range(0,l2) :
        for sz in range(0,l1) :
            if s1[sz] == s2[zz] :
                matrix[zz+1][sz+1] = min(matrix[zz+1][sz] + 1, matrix[zz][sz+1] + 1, matrix[zz][sz])
            else :
                matrix[zz+1][sz+1] = min(matrix[zz+1][sz] + 1, matrix[zz][sz+1] + 1, matrix[zz][sz] + 1)
    return matrix[l2][l1]

way = dict()

w = []

ndict = ldict
ndict.insert(0,first)
ndict.append(last)

table = []
for i in range (length + 2) :
    lin = []
    for j in range (length + 2) :
        lin.append(ldist(ndict[i],ndict[j]))
    table.append(lin)
    print lin

def go(curr) :
    print
    print curr, ":",
    if curr == length + 1 :
        return True
    s = 0
    for i in range (length + 2) :
        p = []
        if (table[curr][i] == 1) and (i > curr):
            p.append(i)
            s += 1
        if way.has_key(curr) :
            way[curr].append(p)
        else :
            way[curr] = p
    if s == 0 :
        return False
    else :
        for i in range (len(way[curr])) :
            go(way[curr][i])


if not go(0) :
    print "Impossible"
else :
    print way
print ldist('abacaba','abracadabra')
