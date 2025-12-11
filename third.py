def je_prvocislo(cislo):
    """
    Funkce overi, zda zadane cislo je nebo neni prvocislo a vrati True nebo False

    Prvocislo je takove cislo vetsi nez 1, ktere neni delitelne zadnym jinym cislem
    nez 1 a samo sebou.
    """
    # prvočíslo musí být větší než 1
    if cislo <= 1:
        return False

    # stačí testovat dělitele do odmocniny čísla
    for i in range(2, int(cislo ** 0.5) + 1):
        if cislo % i == 0:
            return False
    return True


def vrat_prvocisla(maximum):
    """
    Funkce spocita vsechna prvocisla v rozsahu 1 az maximum a vrati je jako seznam.
    """
    # převod na celé číslo (vstup z inputu bývá řetězec)
    maximum = int(maximum)

    prvocisla = []
    for cislo in range(2, maximum + 1):
        if je_prvocislo(cislo):
            prvocisla.append(cislo)
    return prvocisla


if __name__ == "__main__":
    cislo = input("Zadej maximum: ")
    prvocisla = vrat_prvocisla(cislo)
    print(prvocisla)