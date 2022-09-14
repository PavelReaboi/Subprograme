def creare_lista():
    n=int(input('nr de elemente=' ))
    lista_locala=[]
    for i in range(n):
         elem=int(input('elementul'+str(i)+'este='))
         lista_locala.append(elem)
    return lista_locala
     
lista1=creare_lista()     
print(lista1)