def cislo_text(cislo):
    cisla = [
        "nula", "jedna", "dva", "tři", "čtyři", "pět", "šest", "sedm", "osm", "devět",
        "deset", "jedenáct", "dvanáct", "třináct", "čtrnáct", "patnáct", "šestnáct",
        "sedmnáct", "osmnáct", "devatenáct"
    ]
    desitky = [
        "", "", "dvacet", "třicet", "čtyřicet", "padesát",
        "šedesát", "sedmdesát", "osmdesát", "devadesát"
    ]

    try:
        cislo = int(cislo)
    except ValueError:
        return "Neplatný vstup"

    if cislo < 0 or cislo > 100:
        return "Číslo mimo rozsah"
    if cislo == 100:
        return "sto"
    if cislo < 20:
        return cisla[cislo]
    if cislo % 10 == 0:
        return desitky[cislo // 10]
    return f"{desitky[cislo // 10]} {cisla[cislo % 10]}"


if __name__ == "__main__":
    cislo = input("Zadej číslo: ")
    text = cislo_text(cislo)
    print(text)