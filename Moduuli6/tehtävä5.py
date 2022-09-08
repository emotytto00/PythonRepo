def luvut(numb):
    lista = []
    for t in numb:
        if t % 2 == 0:
            lista.append(t)
    return lista

lista2 = [1,2,3,4,5,6,7,8,9,10]
print(lista2)
print(luvut(lista2))