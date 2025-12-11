def je_tah_mozny(figurka, cilova_pozice, obsazene_pozice):
    """
    Ověří, zda se figurka může přesunout na danou pozici.

    :param figurka: Slovník s informacemi o figurce (typ, pozice).
    :param cilova_pozice: Cílová pozice na šachovnici jako n-tice (řádek, sloupec).
    :param obsazene_pozice: Množina obsazených pozic na šachovnici.
    
    :return: True, pokud je tah možný, jinak False.
    """
    typ = figurka["typ"]
    r, c = figurka["pozice"]
    r_cil, c_cil = cilova_pozice

    # 1. kontrola, zda je cílová pozice na šachovnici
    if not (1 <= r_cil <= 8 and 1 <= c_cil <= 8):
        return False

    # 2. kontrola, zda je cílová pozice volná
    if cilova_pozice in obsazene_pozice:
        return False

    delta_r = r_cil - r
    delta_c = c_cil - c
    abs_r = abs(delta_r)
    abs_c = abs(delta_c)

    # 3. pravidla pohybu jednotlivých figur
    if typ == "pěšec":
        # výchozí pozice pro bílé: řádek 2
        if delta_c != 0:
            return False
        if r == 2 and delta_r == 2:
            return (r+1, c) not in obsazene_pozice and (r+2, c) not in obsazene_pozice
        elif delta_r == 1:
            return (r+1, c) not in obsazene_pozice
        else:
            return False

    elif typ == "jezdec":
        return (abs_r, abs_c) in [(2, 1), (1, 2)]

    elif typ == "věž":
        if r != r_cil and c != c_cil:
            return False
        # kontrola cesty
        if r == r_cil:
            krok = 1 if c_cil > c else -1
            for cc in range(c + krok, c_cil, krok):
                if (r, cc) in obsazene_pozice:
                    return False
        else:
            krok = 1 if r_cil > r else -1
            for rr in range(r + krok, r_cil, krok):
                if (rr, c) in obsazene_pozice:
                    return False
        return True

    elif typ == "střelec":
        if abs_r != abs_c:
            return False
        krok_r = 1 if r_cil > r else -1
        krok_c = 1 if c_cil > c else -1
        for i in range(1, abs_r):
            if (r + i * krok_r, c + i * krok_c) in obsazene_pozice:
                return False
        return True

    elif typ == "dáma":
        # kombinace věže a střelce
        if r == r_cil or c == c_cil:
            return je_tah_mozny({"typ": "věž", "pozice": (r, c)}, cilova_pozice, obsazene_pozice)
        elif abs_r == abs_c:
            return je_tah_mozny({"typ": "střelec", "pozice": (r, c)}, cilova_pozice, obsazene_pozice)
        else:
            return False

    elif typ == "král":
        return max(abs_r, abs_c) == 1

    return False


if __name__ == "__main__":
    pesec = {"typ": "pěšec", "pozice": (2, 2)}
    jezdec = {"typ": "jezdec", "pozice": (3, 3)}
    vez = {"typ": "věž", "pozice": (8, 8)}
    strelec = {"typ": "střelec", "pozice": (6, 3)}
    dama = {"typ": "dáma", "pozice": (8, 3)}
    kral = {"typ": "král", "pozice": (1, 4)}
    obsazene_pozice = {(2, 2), (8, 2), (3, 3), (5, 4), (8, 3), (8, 8), (6, 3), (1, 4)}

    print(je_tah_mozny(pesec, (3, 2), obsazene_pozice))  # True
    print(je_tah_mozny(pesec, (4, 2), obsazene_pozice))  # False
    print(je_tah_mozny(pesec, (1, 2), obsazene_pozice))  # False

    print(je_tah_mozny(jezdec, (4, 4), obsazene_pozice))  # False
    print(je_tah_mozny(jezdec, (5, 4), obsazene_pozice))  # False
    print(je_tah_mozny(jezdec, (1, 2), obsazene_pozice))  # True
    print(je_tah_mozny(jezdec, (9, 3), obsazene_pozice))  # False

    print(je_tah_mozny(dama, (8, 1), obsazene_pozice))  # False
    print(je_tah_mozny(dama, (1, 3), obsazene_pozice))  # False
    print(je_tah_mozny(dama, (3, 8), obsazene_pozice))  # True