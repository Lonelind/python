inp = open("input.txt")
out = open("output.txt", 'w')

buf = inp.readlines()

ea = int(buf[0])
eb = int(buf[1])
n = int(buf[2])
mine = "A"
maxe = "B"
a = ea
b = eb


if a > b :
    mine = "B"
    maxe = "A"
    a = eb
    b = ea

res = False
done = False
a_val = 0
b_val = 0

if n == b or n == a :
    done = True
    res = True
elif b % a == 0 and n % a != 0:
    done = True

while not done :
    if b_val == b :
        b_val = 0
    elif a_val == 0 :
        a_val = a
    else :
        if b_val < b :
            if b - b_val < a_val :
                a_val -= b - b_val
                b_val = b
            else :
                b_val += a_val
                a_val = 0
    if a_val == n or b_val == n :
        done = True
        res = True
        break
    elif a_val == 0 and b_val == 0:
        done = True
        res = False
        break


if res :
    if n == b :
        print ">%s" % maxe
    elif n == a :
        print ">%s" % mine
    else :
        res = False
        done = False
        a_val = 0
        b_val = 0

        while not done :
            if b_val == b :
                b_val = 0
                print "%s>" % maxe
            elif a_val == 0 :
                a_val = a
                print ">%s" % mine                
            else :
                if b_val < b :
                    print "%s>%s" % (mine, maxe)                    
                    if b - b_val < a_val :
                        a_val -= b - b_val
                        b_val = b
                    else :
                        b_val += a_val
                        a_val = 0
            if a_val == n or b_val == n :
                done = True
                res = True
                break
            elif a_val == 0 and b_val == 0:
                done = True
                res = False
                break
else :
    print "Impossible"
