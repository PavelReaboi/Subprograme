def sum():
    s=1
    for x in range (2,9):
        if x%2==0:
            s+=0.5**x
    return s
     
print(sum())