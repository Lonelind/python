inp = open("input.txt")
out = open("output.txt", 'w')

buf = inp.readlines()

def swap(a, b) :
    t = a
    a = b
    b = t

a = int(buf[0])
b = int(buf[1])
n = int(buf[2])
mine = "A"
maxe = "B"

if a > b :
    a = int(buf[1])
    b = int(buf[0])
    mine = "B"
    maxe = "A"

res = False

a_val = 0
b_val = 0

while True :
    if b - b_val >= a :
        b_val += a
    else :
        b_val = a - (b - b_val)
    if n == b_val :
        res = True
        break

if res :
    b_val = 0
    while True:
        print ">%s" % mine
        print "%s>%s" % (mine, maxe)
        if b - b_val >= a :
            b_val += a
        else :
            b_val = a - (b - b_val)
            print "%s>" % maxe
            print "%s>%s" % (mine, maxe)
        if n == b_val :
            break
else :
    print "Impossible"
