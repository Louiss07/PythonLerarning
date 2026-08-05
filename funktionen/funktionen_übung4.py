

def netto_zu_brutto(netto):
    return netto * 1.19 

print(netto_zu_brutto(100))



def warenkorb_summe(preise):
    summe = 0
    for preis in preise:
        summe += netto_zu_brutto(preis)
    return summe



print(f"{warenkorb_summe([10.0, 25.0, 8.5]):.2f}")

   