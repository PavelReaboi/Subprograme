
def fact(x):
    f=1
    for c in range(1,x+1):
        f=f*c
    return f

def com1():
    n=int(input('introdu un nr'))
    m=int(input('introdu un nr'))
    if n>m:
        c=fact(n)/(fact(m)*fact(n-m))
    return c
   
print(com1())