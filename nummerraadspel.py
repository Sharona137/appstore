import random

blue = "\033[34m"
reset = "\033[0m"
red = "\33[91m"
pink = "\033[95m"
green = "\033[92m"

def raadspel():

    # Het getal dat geraden moet worden moet tussen de 1 en 15 zijn
    rand_num = random.randint(1, 20)

    # De gebruiker heeft 5 pogingen om het getal te raden
    max_poging = 5

    print(f"\nWelkom bij het {blue}nummerraadspel{reset}, je mag een getal tussen de 1 en 20 raden.")
    print(f"Je hebt {blue}{max_poging} pogingen{reset} om het nummer te raden, succes!")

    for poging in range(max_poging):
        try:
            # Probeer de invoer om te zetten naar een integer
            gok = int(input(f"Raad het nummer {blue}(poging {poging + 1}){reset}: "))

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
            print(f"{gok} is {red}te hoog!{reset} Probeer het opnieuw.")
        elif gok < rand_num:
            print(f"{gok} is {red}te laag!{reset} Probeer het opnieuw.")
        else:
            # Het getal is correct geraden
            print(f"{green}Toppie! Je hebt het getal {rand_num} geraden!{reset}")
            break
    else:
        # Als de speler al zijn pogingen heeft gebruikt zonder het juiste getal te raden
        print(f"Helaas, je hebt al je pogingen gebruikt en het juiste getal niet kunnen raden.")
        print(f"Het juiste getal was {rand_num}.")

    input(f"\nBedankt voor het spelen :)\nDruk op {pink}'Enter'{reset} om terug naar het menu te gaan.")

    return None
