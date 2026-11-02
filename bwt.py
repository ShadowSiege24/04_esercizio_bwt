def bwt(testo: str) -> str:
    if not testo:
        return ""

    testo += "$"

    
    rotazione = [testo[i:] + testo[:i] for i in range(len(testo))]

    rotazione_ordinata = sorted(rotazione)

    bwt_result =  "".join(row[-1] for row in rotazione_ordinata)
    return bwt_result

if __name__ == "__main__":
    stringa_test = input("Inserisci la stringa da convertire: ")
    risultato = bwt(stringa_test)
    print(f"Stringa originale: {stringa_test}")
    print(f"Stringa trasformata: {risultato}")