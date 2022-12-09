import os
import pandas as pd
from datetime import datetime, timedelta

data = pd.read_csv('VW.csv', sep=';')

isRunning = True
while isRunning:
    os.system('cls')
    print('1. Bereken het gemiddelde salaris')
    print('2. Berekend het gemiddelde salaris voor functie X')
    print('3. Aantal werknemers binnen 2 jaar met pensioen')
    print('4. Aantal chauffeurs')
    print('5. Top 10 langst in dienst')
    print('6. Aantal medewerkers met functie X bij afdeling Y')
    print('W. Schrijf alle gegevens naar een bestand')

    print('X. Stop het programma')

    choice = input('\nMaak uw keuze: ')

    if choice == '1':
        os.system('cls')
        print('Het gemiddelde salaris is: ', data['Salaris_bruto'].mean())

        input('\nDruk op enter om door te gaan...')

    elif choice == '2':
        os.system('cls')
        functie = input('Welke functie: ')
        functie = functie[0].upper() + functie[1:]

        functieFilter = (data['Functie'] == functie)
        os.system('cls')
        print(f'Het gemiddelde salaris voor functie {functie} is: {data[functieFilter]["Salaris_bruto"].mean()}')

        input('\nDruk op enter om door te gaan...')

    elif choice == '3':
        os.system('cls')
        willRetire = 0
        for i in data['Geboortedatum']:
            birthDate = datetime.strptime(i, '%d-%m-%Y')
            today = datetime.today()
            age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
            if age >= 65:
                willRetire += 1

        print(f'Aantal werknemers binnen 2 jaar met pensioen: {willRetire}')
        input('\nDruk op enter om door te gaan...')

    elif choice == '4':
        os.system('cls')
        chauffeurCount = 0
        for i in data['Functie']:
            if i == 'Chauffeur':
                chauffeurCount += 1
        print(f'Aantal chauffeurs: {chauffeurCount}')

        input('\nDruk op enter om door te gaan...')

    elif choice == '5':
        os.system('cls')
        dateInServiceSorted = data.sort_values(by='Datum in dienst', ascending=False).head(10)
        print('Top 10 langst in dienst:')
            
        
        input('\nDruk op enter om door te gaan...')

    elif choice == '6':
        os.system('cls')
        functie = input('Welke functie: ')
        functie = functie[0].upper() + functie[1:]

        afdeling = input('Welke afdeling: ')
        afdeling = afdeling[0].upper() + afdeling[1:]

        functieFilter = (data['Functie'] == functie)
        afdelingFilter = (data['Afdeling'] == afdeling)

        print(f'Aantal medewerkers met functie {functie} bij afdeling {afdeling}: {data[functieFilter & afdelingFilter].count()}')
        os.system('cls')

        input('\nDruk op enter om door te gaan...')

    elif choice.lower() == 'w':
        os.system('cls')

        input('\nDruk op enter om door te gaan...')

    elif choice.lower() == 'x':
        os.system('cls')
        isRunning = False
        print('Het programma wordt afgesloten')
