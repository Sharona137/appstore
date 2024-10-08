from nummerraadspel import raadspel
from galgje import spel_beginnen

pink = "\033[95m"
blue = "\033[34m"
red = "\33[91m"
yellow = "\033[93m"
pinkt_background = "\033[45m"


def menu():
    print(f"{red}\nWelkom bij VS-Store")
    gebruiker = input(f"Wat is je naam?: ")
    while True:
        print(f"{pink}\nHoi", gebruiker)
        print('In deze appstore kan je kiezen welke spelletjes je wilt spelen.'
              '\nDe keuzes zijn:'
              '\n1: Nummerraadspel'
              '\n2: Galgje'
              '\n3: Afsluiten')

        keuze = input('Kies je keuze (1, 2 of 3): ')
        if keuze == '1':
            raadspel()
            continue

        elif keuze == '2':
            spel_beginnen()
            continue

        elif keuze == '3':
            print('Tot de volgende keer', gebruiker)
            break

        else:
            print('Dit is een ongeldige optie, kies alsjeblieft keuze 1, 2 of 3')
            continue

menu()