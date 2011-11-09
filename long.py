import string

class longint (object) :
   def __init__(self, string) :
       self.arr = []
       self.minus = 0
       length = len(string)
       for i in reversed(xrange(0,length,1)) :
           number = ord(string[i]) - 48
           self.arr.append(number)

   def out(self):
       res = ""
       length = len(self.arr)
       if self.minus == 1 :
           res += "-"
       for i in reversed(xrange(0,length,1)) :
           res += chr(self.arr[i] + 48)
       return res

   def balance(self) :
       length = len(self.arr)
       for i in reversed(xrange(1,length,1)) :
           if self.arr[i] == 0:
               self.a.pop()
           else:
               break

   def __add__(self, other) : #operator +
       length1 = len(self.arr)
       length2 = len(other.arr)
       if length1 >= length2 :
           length1_alt = length1
           length2_alt = length2
           self_alt = self
           other_alt = other
       else :
           length1_alt = length2
           length2_alt = length1
           self_alt = other
           other_alt = self
       r = 0;
       for i in xrange(0,length1_alt,1) :
           if i < length2_alt :
               res = (self_alt.arr[i] + other_alt.arr[i] + r) % 10
               r = (self_alt.arr[i] + other_alt.arr[i]) / 10
               self_alt.arr[i] = res
           else:
               res = (self_alt.arr[i] + r) % 10
               r = (self_alt.arr[i] + r) / 10
               self_alt.arr[i] = res
       if r > 0 :
           self_alt.arr.append(r)
       return self_alt

   def __ge__(self, other) : #operator >
       length1 = len(self.arr)
       length2 = len(other.arr)
       if length1 > length2 :
           return True
       elif length1 == length2 :
           for i in reversed(xrange(0,length1,1)):
               if self.arr[i] < other.arr[i]:
                   return False
               elif self.arr[i] > other.arr[i]:
                   return True
       else :
           return False
       return True

   def __sub__(self, other) : #operator -
       length1 = len(self.arr)
       length2 = len(other.arr)
       if self >= other :
           length1_alt = length1
           length2_alt = length2
           self_alt = self
           other_alt = other
       else :
           length1_alt = length2
           length2_alt = length1
           other_alt = self
           self_alt = other
           self_alt.minus = 1
       for i in xrange(0,length1_alt,1):
           if i < length2_alt:
               res = self_alt.arr[i] - other_alt.arr[i]
           else:
               res = self_alt.arr[i]
           if res < 0:
               if (i + 1) < length1_alt:
                   res += 10
                   self_alt.arr[i + 1] -= 1
               else:
                   self_alt.minus = 1
           self_alt.arr[i] = res
       self_alt.balance()
       return self_alt

   
a = longint('11110000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001')

b = longint('222200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000002')

s = a + b
print a.out(), "+", b.out(), "=", s.out()
print
s = s + s

print s.out()
print
s -= a
print s.out()
