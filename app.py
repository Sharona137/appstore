from nummerraadspel import raadspel
from galgje import spel_beginnen

def menu():
    while True:
        print('\nWelkom bij VS-Store.'
              '\nIn deze appstore kan je kiezen welke spelletjes je wilt spelen.'
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
            print('Tot de volgende keer')
            break


        else:
            print('Dit is een ongeldige optie')

menu()