zdanie = input("Podaj zdanie: ")

# a
litery = sorted([litera for litera in zdanie.lower() if litera.isalpha()])
print("Litery w zdaniu w kolejności alfabetycznej:", "".join(litery))

# b
alfabet = set("abcdefghijklmnopqrstuvwxyz")
litery_zdania = set(litera for litera in zdanie.lower() if litera.isalpha())
brakujace_litery = alfabet - litery_zdania
print("Brakujące litery alfabetu:", "".join(sorted(brakujace_litery)))
