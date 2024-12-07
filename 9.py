lista_zakupow = {
    "Chleb": 4.50,
    "Mleko": 3.20,
    "Masło": 7.80,
    "Ser": 12.40,
    "Jabłka": 5.30,
    "Czekolada": 8.90
}

print("Lista zakupów:")
for artykul, kwota in lista_zakupow.items():
    print(f"{artykul}: {kwota:.2f} PLN")

suma_wydatkow = sum(lista_zakupow.values())
print(f"\nŁączna suma wydatków: {suma_wydatkow:.2f} PLN")
