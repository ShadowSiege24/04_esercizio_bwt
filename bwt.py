def bwt(testo: str) -> str:
    if not testo:
        return ""

    testo += "$"

    
    rotazione = [testo[i:] + testo[:i] for i in range(len(testo))]

    rotazione_ordinata = sorted(rotazione)

    bwt_result =  "".join(row[-1] for row in rotazione_ordinata)