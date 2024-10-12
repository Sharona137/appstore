import random

yellow = "\033[93m"

def woordenbestand(file):
    with open(file, 'r') as infile:
        woorden = infile.readlines()
    woorden_lijst = {'easy': [], 'medium': [], 'hard': []}

    for line in woorden:
        moeilijkheid, woord = line.strip().split(":")
        woorden_lijst[moeilijkheid].append(woord)
    return woorden_lijst

def kies_woord(woordenlijst, moeilijkheid):
    return random.choice(woordenlijst[moeilijkheid])

def spel_spelen(woord, max_pogingen):
    geraden_letters = []
    pogingen_over = max_pogingen
    woord_compleet = "_" * len(woord)
    print("Het woord dat geraden moet worden is " + woord_compleet)

    while pogingen_over > 0:
        poging = input("Raad een letter: ").lower()

        if poging in geraden_letters:
            print("Je hebt deze letter al geraden.")
        elif len(poging) != 1:
            print("Voer slechts 1 letter in.")
        elif poging in woord:
            geraden_letters.append(poging)
            woord_compleet = "".join([letter if letter in geraden_letters else "_" for letter in woord])
            print(f"De letter {poging} zit in het woord -> {woord_compleet}")
        else:
            geraden_letters.append(poging)
            pogingen_over -= 1
            print(f"De letter {poging} is fout, je hebt nog {pogingen_over} pogingen over")
        if woord_compleet == woord:
            print(f"Yes, je hebt het woord '{woord}' geraden")
            input(f"Bedankt voor het spelen :)"
                  f"\nDruk op 'Enter' om terug naar het menu te gaan")
            return True, max_pogingen - pogingen_over

    print(f"Helaas, je hebt geen pogingen meer. Het woord was: {woord}")
    return False, max_pogingen


def spel_beginnen():
    print(f"{yellow}Welkom bij galgje")
    woorden_lijst = woordenbestand("woorden.txt")
    moeilijkheid = input("Kies een moeilijkheidsgraad (1: easy, 2: medium, 3: hard): ").lower()

    while moeilijkheid not in woorden_lijst:
        moeilijkheid = input("Ongeldige keuze. Kies easy, medium of hard: ").lower()

    woord = kies_woord(woorden_lijst, moeilijkheid)
    max_pogingen = len(woord) + 2
    spel_spelen(woord, max_pogingen)

    input("Bedankt voor het spelen :)\nDruk op 'Enter' om terug naar het menu te gaan.")

