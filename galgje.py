import random

yellow = "\033[93m"
pink = "\033[95m"
reset = "\033[0m"
red = "\33[91m"
green = "\033[92m"
grey = "\033[37m"

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
    print(f"Het woord dat geraden moet worden is -> {yellow}" + woord_compleet, f"{reset}")

    while pogingen_over > 0:
        poging = input("Raad een letter: ").lower()

        if poging in geraden_letters:
            print("Je hebt deze letter al geraden.")
        elif len(poging) != 1:
            print("Voer slechts 1 letter in.")
        elif poging in woord:
            geraden_letters.append(poging)
            woord_compleet = "".join([letter if letter in geraden_letters else "_" for letter in woord])
            print(f"{green}Correct{reset}, de letter {green}{poging}{reset} zit in het woord -> {yellow} {woord_compleet} {reset}")
        else:
            geraden_letters.append(poging)
            pogingen_over -= 1
            print(f"De letter {red} {poging} is fout {reset}, je hebt nog {red}{pogingen_over} pogingen over{reset}")
        if woord_compleet == woord:
            print(f"Yes, je hebt het woord {yellow}'{woord}'{reset} geraden")
            return True, max_pogingen - pogingen_over

    print(f"Helaas, je hebt geen pogingen meer. Het woord was: {woord}")
    return False, max_pogingen


def spel_beginnen():
    print(f"\n{reset}Welkom bij {yellow}galgje{reset}")
    woorden_lijst = woordenbestand("woorden.txt")
    moeilijkheid = input(f"Type hier de moeilijkheidsgraad die je wilt{grey}(easy, medium, hard): {reset}").lower()

    while moeilijkheid not in woorden_lijst:
        moeilijkheid = input("Ongeldige keuze. Kies easy, medium of hard: ").lower()

    woord = kies_woord(woorden_lijst, moeilijkheid)
    max_pogingen = len(woord) + 3
    spel_spelen(woord, max_pogingen)

    input(f"\nBedankt voor het spelen :)\nDruk op {pink}'Enter'{reset} om terug naar het menu te gaan.")

