def osszegzes(lista):
    '''ez a fg. összeadja a paraméterben kapott lista elemeit'''
    sum = 0
    for e in lista:
        sum += e
    return sum


def megszamlalas_paros(lista):
    '''ez az fg. meghatározza a paraméterben kapott lista páros elemeinek számát'''
    count = 0
    for e in lista:
        if e % 2 == 0:
            count += 1
    return count