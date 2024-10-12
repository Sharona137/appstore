import random

# Kleurtjes om mijn code aantrekkelijker te maken
blue = "\033[34m"
reset = "\033[0m"
red = "\33[91m"
pink = "\033[95m"
green = "\033[92m"

def raadspel():
    rand_num = random.randint(1, 20)  # Er wordt een random nummer tussen de 1 en 20 gekozen
    max_poging = 5
    print(f"\nWelkom bij het {blue}nummerraadspel{reset}, je mag een getal tussen de 1 en 20 raden.")
    print(f"Je hebt {blue}{max_poging} pogingen{reset} om het nummer te raden, succes!")

    poging = 0  # Houdt het aantal gebruikte pogingen bij

    while poging < max_poging:
        gok = input(f"Raad het nummer {blue}(poging {poging + 1}){reset}: ")

        if not gok.isdigit():  # Controleer of de invoer een cijfer is
            print(f"Voer alsjeblieft een {pink}cijfer{reset} in, geen {red}letter{reset}")  # Foutmelding voor geen cijfer
            continue

        gok = int(gok)  # Invoer moet een cijfer zijn

        if gok < 1 or gok > 20:
            print("Voer alsjeblieft een getal tussen de 1 en 20 in.")
            continue

        poging += 1  # Er komt een poging bij totdat de maximale pogingen zijn bereikt

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
        # Alle pogingen zijn gebruikt
        print(f"{red}Helaas, je hebt al je pogingen gebruikt en het juiste getal niet kunnen raden.{reset}")
        print(f"Het juiste getal was {blue}{rand_num}{reset}.")

    input(f"\nBedankt voor het spelen :)\nDruk op {pink}'Enter'{reset} om terug naar het menu te gaan.")

