import random

blue = "\033[34m"


def raadspel():

    # Het getal dat geraden moet worden moet tussen de 1 en 15 zijn
    rand_num = random.randint(1, 20)

    # De gebruiker heeft 5 pogingen om het getal te raden
    max_poging = 5

    print(f"{blue}Hoi, welkom bij het nummerraadspel! Je mag een getal tussen de 1 en 20 raden.")
    print(f"Je hebt {max_poging} pogingen om het nummer te raden, succes!")

    for poging in range(max_poging):
        try:
            # Probeer de invoer om te zetten naar een integer
            gok = int(input(f"Raad het nummer (poging {poging + 1}): "))

            # Controleer of de invoer binnen het juiste bereik valt
            if gok < 1 or gok > 20:
                print("Voer alsjeblieft een getal tussen de 1 en 20 in.")
                continue  # Ga verder met de volgende poging als de invoer ongeldig is

        except ValueError:
            # Als de invoer geen integer is, geef een foutmelding
            print(f"Ongeldige poging, geef alsjeblieft een nummer in.")
            continue  # Ga verder met de volgende poging

        # Check of de gok te hoog of te laag is
        if gok > rand_num:
            print(f"{gok} is te hoog! Probeer het opnieuw.")
        elif gok < rand_num:
            print(f"{gok} is te laag! Probeer het opnieuw.")
        else:
            # Het getal is correct geraden
            print(f"Toppie! Je hebt het getal {rand_num} geraden!")
            break
    else:
        # Als de speler al zijn pogingen heeft gebruikt zonder het juiste getal te raden
        print(f"Helaas, je hebt al je pogingen gebruikt en het juiste getal niet kunnen raden.")
        print(f"Het juiste getal was {rand_num}.")

    input("Bedankt voor het spelen :)\nDruk op 'Enter' om terug naar het menu te gaan.")

    return None
