a = [[1,2,3,4],
     [4,5,6,10],
     [7,8,9,15],
     [12,8,95,3],
     [4,6,12,9]]

b = [[1,2,3,45,7],
     [4,5,6,12,76],
     [7,8,9,56,1],
     [12,5,7,87,34]]

def mul(m1, m2) : #matrix NxK * KxM = NxM
    if len(a[0]) == len(b) :
        res = []
        n = len(a)
        k = len(a[0])
        m = len(b[0])
        for i in range(0,n) :
            row = []
            for j in range(0,m) :
                t = 0
                for p in range(0,k) :
                    t += m1[i][p]*m2[p][j]
                row.append(t)
            res.append(row)
        return res
    else:
        print "Cannot multiply!"
        return res

def out(matrix) :
    n = len(matrix)
    if n > 0 :
        m = len(matrix[0])
        mx = []
        for i in range(0,m) :
            mx.append(0)
            for j in range(0,n) :
                mx[i]=max(abs(matrix[j][i]),mx[i])
    
        for i in range(0,m) :
            t = mx[i]
            mx[i] = 1
            while t > 9 :
                t /= 10
                mx[i] += 1

        for i in range(0,n) :
            for j in range(0,m) :
                print repr(matrix[i][j]).rjust(mx[j]),
            print

pm = mul(a,b)
out(pm)
