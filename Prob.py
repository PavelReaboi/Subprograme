x=int(input('Introduceti un nr '))
y=int(input('Introduceti un nr '))

import math
def sum():
    return x+y
    
print('Suma este', sum())
    
def prod():
    return x*y
    
print('Produsul este', prod())
    
def med_arit():
    return (x+y)/2
    
print('Media aritmetica este', med_arit())
    
def div():
    return math.gcd(x,y)
    
print('Cel mai mare difuzor comun este', div())
    
def mini():
      return min(x,y)
    
print('Minimul este', mini())
    
def maxi():
    return max(x,y)
    
print('Maximul este', maxi())
   
def toti_div():
    list=[]
    for i in range(1,min(x,y)+1):
        if x%i==0 and y%i==0:
            list.append(i)
            
    return list
    
print('Toti difuzorii comuni sunt', toti_div())
    
def cinm():
    listm=[]
    for i in range(1,6):
        listm.append(x*y*i)
    return listm
    
print('Cinci multipli sunt', cinm())
    
def cifc():
     com=[]
     temp=[]
     for i in str(max(x,y)):
         temp.append(i)
     for l in str(min(x,y)):
          if l in temp and l not in com:
               com.append(l)
          return com
          
print('Cifre comune sunt', cifc())
          
def cifp():
    dist=[]
    temp=[]
    for i in str(y):
        temp.append(i)
    for l in str(x):
        if l not in temp and l not in dist:
            dist.append(l)
    return dist
    
print('Cifre distincte in primul nr sunt', cifp())
    
def priet():
    list1=[]
    list2=[]
    priet=''
    for i in range(1,x+1):
        if y%i==0:
            list1.append(i)
    for l in range(1,y+1):
        if y%l==0:
            list2.append(l)
    if len(list1)==len(list2):
        priet='prieteni'
    else:
        priet='nu prieteni'
    return priet
    
print('Prieteni', priet())