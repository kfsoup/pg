def bin_to_dec(binarni_cislo):
    """
    Funkce spocita hodnotu predavaneho binarniho cisla (binarni_cislo muze byt str i int!!!)
    111 -> 7
    "101" -> 5
    """
    # Převedeme vstup na řetězec, abychom mohli pracovat s int i str vstupy stejně
    cislo_str = str(binarni_cislo)
    
    decimalni_hodnota = 0
    
    # Procházíme číslo a v každém kroku posouváme hodnotu (násobíme 2) a přičítáme bit
    for cislice in cislo_str:
        decimalni_hodnota = decimalni_hodnota * 2 + int(cislice)
        
    return decimalni_hodnota


def test_bin_to_dec():
    assert bin_to_dec("0") == 0
    assert bin_to_dec(1) == 1
    assert bin_to_dec("100") == 4
    assert bin_to_dec(101) == 5
    assert bin_to_dec("010101") == 21
    assert bin_to_dec(10000000) == 128
    
    # Test pro číslo 167 (správný binární zápis je 10100111)
    assert bin_to_dec("10100111") == 167 
    
    print("Všechny testy proběhly v pořádku.")


if __name__ == "__main__":
    test_bin_to_dec()
    
    # Ukázka rozdílu (vysvětlení chyby v zadání)
    chybne_zadani = "10011101"
    spravne_zadani = "10100111"
    
    print(f"Binární {chybne_zadani} = {bin_to_dec(chybne_zadani)} (Matematicky správně)")
    print(f"Binární {spravne_zadani} = {bin_to_dec(spravne_zadani)} (To je číslo 167)")