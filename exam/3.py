import operator

fname = raw_input()
inp = open(fname)
buf = inp.readlines()

for line in buf :
    if line != "\n" :
        line = line.rstrip()
        ra = dict()
        for ch in line :
            if ch != " " :
                if ra.has_key(ch) :
                    ra[ch] += 1
                else :            
                    ra[ch] = 1
        ra_s = sorted(ra.iteritems(), key=operator.itemgetter(1))
        ra_s.reverse()
        for p in ra_s :
            os = p[0]+str(p[1])
            print os,
        print
