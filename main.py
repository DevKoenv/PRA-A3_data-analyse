import os
import pandas as pd

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
        print(f'Het gemiddelde salaris voor functie {functie} is: {data[functieFilter]["Salaris_bruto"].mean()}')

        input('\nDruk op enter om door te gaan...')

    elif choice == '3':
        os.system('cls')

        input('\nDruk op enter om door te gaan...')

    elif choice == '4':
        os.system('cls')

        input('\nDruk op enter om door te gaan...')

    elif choice == '5':
        os.system('cls')

        input('\nDruk op enter om door te gaan...')

    elif choice == '6':
        os.system('cls')

        input('\nDruk op enter om door te gaan...')

    elif choice.lower() == 'w':
        os.system('cls')

        input('\nDruk op enter om door te gaan...')

    elif choice.lower() == 'x':
        os.system('cls')
        isRunning = False
        print('Het programma wordt afgesloten')
