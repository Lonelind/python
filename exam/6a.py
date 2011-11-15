import copy

f = open("input.txt")

buf = f.readlines()
first = buf[0].rstrip()
last = buf[1].rstrip()
length = int(buf[2])
ldi = buf[3:]
ldict = []
f.close()

for i in range(length) :
    ldict.append(ldi[i].rstrip())

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

ldict.insert(0,first)
ldict.append(last)
length +=2
lmatrix = []

for i in range(length) :
    row = []
    for j in range(length) :
        row.append(ldist(ldict[i],ldict[j]))
    lmatrix.append(row)

words = []
words.append([first])

check = True
done = False

while check :
    t = copy.deepcopy(words)
    for p in range(len(words)) :
        check = False
        for i in range (len(ldict)) :
            if ldict[i] == words[p][len(words[p]) - 1] :
                for j in range (i + 1,len(ldict)) :
                    if lmatrix[i][j] == 1 : 
                        if ldict[i] == last :  
                            done = True
                        temp = []
                        temp = copy.deepcopy(words[p])
                        temp.append(ldict[j])
                        lmatrix[i][j]=0
                        t.append(temp)
                        check = True
    if len(t) > 0 :
        words = copy.deepcopy(t)
minlength = -1
minindex = 0
for i in range(len(words)):
    if words[i][0] == first and words[i][len(words[i])-1] == last :
        if minlength == -1:
            minlength = len(words[i])
            minindex = i
        if minlength > len(words[i]):
            minlength = len(words[i])
            minindex = i

if minlength == -1:
    print "Impossible"
else:
    for i in range(minlength - 1):
        print words[minindex][i]
    print last
