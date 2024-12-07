Moja_lista = [1, 17, 3, 5, 3, 4, 86, 90, 2, 21]

# 1. Odwołania do pierwszego i ostatniego elementu
print("Pierwszy element:", Moja_lista[0])
print("Ostatni element:", Moja_lista[-1])

# 2. Długość listy
print("Długość listy:", len(Moja_lista))

# 3. Największa i najmniejsza wartość
print("Największa wartość:", max(Moja_lista))
print("Najmniejsza wartość:", min(Moja_lista))

# 4. Suma elementów listy
print("Suma elementów:", sum(Moja_lista))

# 5. Sortowanie listy
print("Posortowana lista:", sorted(Moja_lista))

# 6. Dodanie elementu na końcu listy
Moja_lista.append(6)
print("Po dodaniu elementu na końcu:", Moja_lista)

# 7. Wstawienie elementu w określonym indeksie
Moja_lista.insert(3, 5)
print("Po wstawieniu elementu na indeksie 3:", Moja_lista)

# 8. Usunięcie ostatniego elementu
ostatni_element = Moja_lista.pop()
print("Po usunięciu ostatniego elementu:", Moja_lista)
print("Usunięty element:", ostatni_element)

# 9. Odwrócenie kolejności elementów
Moja_lista.reverse()
print("Odwrócona lista:", Moja_lista)

# 10. Połączenie dwóch list
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
listaL = lista1 + lista2
print("Połączenie dwóch list:", listaL)

# 11. Pięciokrotne powtórzenie wartości listy1
listaM = lista1 * 5
print("Pięciokrotne powtórzenie listy1:", listaM)

# 12. Wycinki listy
print("Wycinek od początku do 3 elementu:", listaL[:3])
print("Wycinek od elementu 2 do końca:", listaL[2:])
print("Wycinek z zakresem i krokiem (1:5:2):", listaL[1:5:2])
print("Odwrócony wycinek:", listaL[::-1])
