f = open("input.txt")

buf = f.readlines()
first = buf[0]
last = buf[1]
length = int(buf[2])
ldict = buf[3:]

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

way = []
for i in range(0,len(ldict)) :
    if len(way) == 0 :
        if first == ldict[i] :
            way.append(i)
    else :
        if ldist(first)
print ldist('abacaba','abracadabra')
