# Maak een selectie om na te gaan of iemand oud genoeg is voor een rijbewijs.
def check_rijbewijsleeftijd(leeftijd):
    rijbewijsleeftijd = 18

    # Schrijf hier jouw selectie!
    if 18 <= rijbewijsleeftijd:

        print (0)
    else:
        print(1)

# Vraag de leeftijd aan de gebruiker
input_leeftijd = int(input("Hoe oud ben je? "))

# Roep de functie aan om de leeftijd te controleren
check_rijbewijsleeftijd(input_leeftijd)
