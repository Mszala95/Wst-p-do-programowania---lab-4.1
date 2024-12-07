# a
imie = input("Podaj swoje imię: ")
print("Witaj", imie)

# b
wiek = input("Podaj swój wiek: ")
print("Twój wiek to:", wiek)

# c
imie = input("Podaj swoje imię: ")
nazwisko = input("Podaj swoje nazwisko: ")
inicjaly = imie[0].upper() + "." + nazwisko[0].upper() + "."
print("Twoje inicjały to:", inicjaly)

# d.
lancuch = input("Podaj dowolny łańcuch znaków: ")
print("Łańcuch powtórzony pięć razy:", lancuch * 5)

# e
lancuch1 = input("Podaj pierwszy łańcuch znaków: ")
lancuch2 = input("Podaj drugi łańcuch znaków: ")
polaczony_lancuch = lancuch1 + lancuch2
print("Połączone łańcuchy:", polaczony_lancuch)

# f
lancuch1 = input("Podaj pierwszy łańcuch znaków: ")
lancuch2 = input("Podaj drugi łańcuch znaków: ")
pierwsza_polowa = lancuch1[:len(lancuch1)//2]
druga_polowa = lancuch2[len(lancuch2)//2:]
polaczony_fragment = pierwsza_polowa + druga_polowa
print("Połączenie pierwszej połowy pierwszego i drugiej połowy drugiego łańcucha:", polaczony_fragment)
