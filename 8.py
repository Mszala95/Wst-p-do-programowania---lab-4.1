stopnie = (
    "Szeregowy",
    "Kapral",
    "Sierżancie",
    "Porucznik",
    "Kapitan",
    "Major",
    "Pułkownik",
)

ilosc_stopni = len(stopnie)

major_index = stopnie.index("Major")

pulkownik_wystepowanie = "Pułkownik" in stopnie

print("Liczba stopni wojskowych:", ilosc_stopni)
print("Indeks stopnia 'Major':", major_index)
print("Czy 'Pułkownik' występuje w krotce:", pulkownik_wystepowanie)
