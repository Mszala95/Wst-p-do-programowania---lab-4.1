imiona = ["Anna", "Marek", "Kasia", "Tomasz"]

# a.
imiona.sort()
print("Posortowana lista:", imiona)

# b.
imiona.append("Joanna")
imiona.append("Paweł")
ostatnia_osoba = imiona.pop()
print("Lista po dodaniu dwóch osób i usunięciu ostatniej:", imiona)
print("Usunięta osoba:", ostatnia_osoba)

# c.
imiona.insert(2, "Karolina")
print("Lista po dodaniu osoby na pozycji 3:", imiona)

# d.
imiona.reverse()
zdublowana_lista = imiona * 2
print("Lista po odwróceniu i zdublowaniu:", zdublowana_lista)
