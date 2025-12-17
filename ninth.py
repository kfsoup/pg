def dec_to_bin(cislo):
    """
    Funkce prevede cislo na binarni reprezentaci (cislo muze byt str i int!!!)
    7 -> "111"
    5 -> "101"
    """
    # 1. Převedeme vstup na integer (řeší vstup "100" i 100)
    hodnota = int(cislo)
    
    # 2. Ošetření nuly (speciální případ, algoritmus níže by vrátil prázdný string)
    if hodnota == 0:
        return "0"
    
    binarni_retezec = ""
    
    # 3. Algoritmus opakovaného dělení dvěma
    while hodnota > 0:
        zbytek = hodnota % 2      # Zjistíme zbytek (0 nebo 1)
        binarni_retezec = str(zbytek) + binarni_retezec  # Přidáme zbytek na ZAČÁTEK řetězce
        hodnota = hodnota // 2    # Celochíselně vydělíme dvěma
        
    return binarni_retezec


# Přejmenoval jsem testovací funkci na 'test_dec_to_bin', aby odpovídala logice
def test_dec_to_bin():
    assert dec_to_bin("0") == "0"
    assert dec_to_bin(1) == "1"
    assert dec_to_bin("100") == "1100100"
    assert dec_to_bin(101) == "1100101"
    assert dec_to_bin(127) == "1111111"
    assert dec_to_bin("128") == "10000000"
    
    # Doplňkový test pro vaše konkrétní číslo (matematicky správně)
    assert dec_to_bin(167) == "10100111"
    assert dec_to_bin(157) == "10011101"

if __name__ == "__main__":
    # Pokud spustíte soubor přímo, vypíše ukázku
    print(dec_to_bin(167))