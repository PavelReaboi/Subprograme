a=int(input('Introduceti un nr'))
b=int(input('Introduceti un nr'))
c=int(input('Introduceti un nr'))
d=int(input('Introduceti un nr'))

from fractions import Fraction

def fracts():
    s=Fraction(a,b)+Fraction(c,d)
    return s

def fractp():
    p=Fraction(a,b)*Fraction(c,d)
    return p
    
print('Suma fractiei este=',fracts(),',iar produsul este=',fractp())