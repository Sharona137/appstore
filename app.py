def menu():
    print('Welkom bij VS-Store.'
          '\nIn deze appstore kan je kiezen welke spelletjes je wilt spelen.'
          '\nJe kan op dit moment kiezen uit een nummerraadspel of galgje')
    keuze = input('Kies je keuze (nummerraadspel of galgje): ')
    if keuze == 'nummerraadspel':
        import nummerraadspel
    elif keuze == 'galgje':
        import galgje

menu()