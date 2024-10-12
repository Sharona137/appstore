import random

# Kleurtjes om mijn code aantrekkelijker te maken
yellow = "\033[93m"
pink = "\033[95m"
reset = "\033[0m"
red = "\33[91m"
green = "\033[92m"
grey = "\033[37m"
blue = "\033[34m"

def woordenbestand(file): # Het woorden bestand wordt uitgelezen
    with open(file, 'r') as infile:
        woorden = infile.readlines()
    woorden_lijst = {'easy': [], 'medium': [], 'hard': []}

    for line in woorden:
        moeilijkheid, woord = line.strip().split(":")
        woorden_lijst[moeilijkheid].append(woord)
    return woorden_lijst

def kies_woord(woordenlijst, moeilijkheid): # Er wordt een random woord uitgekozen op basis van de moeilijkheidsgraad
    return random.choice(woordenlijst[moeilijkheid])

def spel_spelen(woord, max_pogingen):
    geraden_letters = []
    pogingen_over = max_pogingen
    woord_compleet = "_" * len(woord) # Het aantal streepjes geeft aan uit hoeveel letters het woord bestaat
    print(f"Het woord dat geraden moet worden is -> {pink}" + woord_compleet, f"{reset}")

    while pogingen_over > 0:
        poging = input("Raad een letter: ").lower()

        if poging.isdigit():  # Controleer of de invoer een cijfer is
            print(f"Voer alsjeblieft een {blue}letter{reset} in, geen {red}cijfer{reset}.")
            continue

        if poging in geraden_letters:
            print(f"Je hebt deze letter {blue}al{reset} geraden.")
        elif len(poging) != 1: # Als er meerdere letters worden ingevoerd
            print(f"Voer slechts {blue}1 letter in.")
        elif poging in woord:
            geraden_letters.append(poging) # De letter wordt aan de lijst toegevoegd van de letters die zijn ingevoerd door gebruiker
            woord_compleet = "".join([letter if letter in geraden_letters else "_" for letter in woord]) # De letter wordt op de plaats van het streepje gezet
            print(f"{blue}Correct{reset}, de letter {blue}{poging}{reset} zit in het woord -> {pink} {woord_compleet} {reset}")
        else:
            geraden_letters.append(poging) # De letter wordt aan de lijst toegevoegd van de letters die zijn ingevoerd door gebruiker
            pogingen_over -= 1 # Van de maximale pogingen, wordt er 1 poging van af geteld
            print(f"De letter {red} {poging} is fout {reset}, je hebt nog {red}{pogingen_over} pogingen over{reset}")
        if woord_compleet == woord:
            print(f"Yes, je hebt het woord {pink}'{woord}'{reset} geraden")
            return True

    print(f"Helaas, je hebt geen pogingen meer. Het woord was: {woord}")
    return False

def spel_beginnen():  # Hier begint het spel
    print(f"\n{reset}Welkom bij {pink}galgje{reset}")
    woorden_lijst = woordenbestand("woorden.txt")

    # Vraag de gebruiker om een moeilijkheidsgraad met nummers
    moeilijkheid = input(f"Type hier de moeilijkheidsgraad die je wilt ({pink}1{reset} voor easy, {pink}2{reset} voor medium, {pink}3{reset} voor hard): ").lower()

    # Vertaal de keuze van de gebruiker naar de moeilijkheidsgraad
    while moeilijkheid not in ['1', '2', '3']:
        moeilijkheid = input(f"Ongeldige keuze. Kies {pink}1{reset} voor easy, {pink}2{reset} voor medium of {pink}3{reset} voor hard: ").lower()

    if moeilijkheid == '1':
        moeilijkheid = 'easy'
    elif moeilijkheid == '2':
        moeilijkheid = 'medium'
    elif moeilijkheid == '3':
        moeilijkheid = 'hard'

    woord = kies_woord(woorden_lijst, moeilijkheid)  # Een random woord wordt gekozen op basis van de ingevoerde moeilijkheidsgraad
    max_pogingen = len(woord) + 3  # Aantal pogingen hangt af van de lengte van het woord
    spel_spelen(woord, max_pogingen)

    input(f"\nBedankt voor het spelen :)\nDruk op {blue}'Enter'{reset} om terug naar het menu te gaan.")

