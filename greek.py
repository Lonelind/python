print "Greek alphabet:"

t = 0
for i in range(int("391", 16),int("3AA",16)) :
    if i != int("3A2", 16) :
        if t == 4 :
            t = 0
            print
        print unichr(i)+unichr(i+32),
        t += 1
