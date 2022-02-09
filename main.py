import my_functions as f

lista_szamokkal = [4, 7, 11]

# sorozatszámítás
# -> pl. lista elemeinek összege
# IN: számokat tartalmazó lista
# OUT: egy szám

osszeg = f.osszegzes(lista_szamokkal)
print(f'a {lista_szamokkal} elemeinek összege: {osszeg}')

# megszámlálás
# -> pl.: páros elemek számát meghatározó fg.
# IN: számokat tartalmazó lista
# OUT: egy szám

paros_elemek_szama = f.megszamlalas_paros(lista_szamokkal)
print(f'a {lista_szamokkal}ban a páros elemek száma: {paros_elemek_szama}')


# [ezeket meg otthon/házinak]
# minimum/maximum
# eldöntés
# kiválasztás
# lineáris keresés
