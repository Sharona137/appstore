# Het nummerraadspel en galgje importeren
from nummerraadspel import raadspel
from galgje import spel_beginnen

# Kleurtjes om mijn appstore aantrekkelijker te maken
pink = "\033[95m"
blue = "\033[34m"
red = "\33[91m"
yellow = "\033[93m"
pinkt_background = "\033[45m"
green = "\033[92m"
reset = "\033[0m"


def menu():
    print(f"\nWelkom bij {blue}VS-Store{reset}")
    gebruiker = input(f"Wat is je naam?: ")
    while True:
        print(f"\nHoi,{pink}",gebruiker)
        print(f"{reset}In deze appstore kan je kiezen welke spelletjes je wilt spelen."
              "\nDe keuzes zijn:"
              f"\n{pink}1: Nummerraadspel"
              "\n2: Galgje"
              f"\n3: Afsluiten{reset}")

        keuze = input('Kies je keuze (1, 2 of 3): ')
        if keuze == '1':
            raadspel() # Het nummerraadspel bestand wordt geopend
            continue

        elif keuze == '2':
            spel_beginnen() # Galgje bestand wordt geopend
            continue

        elif keuze == '3':
            print(f"\n{reset}Tot de volgende keer {pink}{gebruiker}{reset}, fijne dag verder :)")
            break

        else: # Een keuze anders dan 1, 2 of 3
            print('Dit is een ongeldige optie, kies alsjeblieft keuze 1, 2 of 3')
            continue

menu()