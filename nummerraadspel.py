import random

#Het getal dat geraden moet worden moet tussen de 1 en 15 zijn
rand_num = random.randint(1, 15)

#De gebruiker heeft 5 pogingen om het getal te raden
max_poging = 5

print(f"Hoi, welkom bij het nummerraad spel! Je mag een getal tussen de 1 en 15 raden.")
print(f"Je hebt {max_poging} pogingen om het nummer te raden, succes!")

#Deze code geeft aan dat bij elke poging, 1 poging erbij word geteld totdat er 6 pogingen zijn gedaan
for poging in range(max_poging):
    gok = eval(input(f"Poging {poging + 1}: "))
    if gok < 0 or gok > 15:
        print("Voer alsjeblieft een getal tussen de 1 en de 15 in.")
        #continue geeft aan dat de code verder gaat nadat er een ongeldige getal is ingevuld
        continue

    if gok > rand_num:
        print(str(gok) + " is te hoog! Probeer het opnieuw.")
    elif gok < rand_num:
        print(str(gok) + " is te laag! Probeer het opnieuw.")
    else:
        #Hier staat de code van of het getal is geraden
        print(f"Toppie! Je hebt het getal {rand_num} geraden!")
        #break geeft aan dat de gehele code hier stopt, omdat het getal is geraden
        break
else:
    #Hier geeft de code aan dat het getal niet is geraden en wat het getal was dat geraden moest geworden
    print(f"Helaas, je hebt al je pogingen gebruikt en je hebt het getal niet kunnen raden.")
    print(f"Het juiste getal was {rand_num}.")

print(f"Bedankt voor het spelen, fijne dag verder :)")
sluit = input(f"Toets 'Enter' in om het spel af te sluiten")
