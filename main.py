import os
import pandas as pd
from datetime import datetime

try:
    data = pd.read_csv('VW.csv', sep=';')
except FileNotFoundError:
    print('File not found')
    exit()


"""
Bereken het gemiddelde salaris
"""
def choice1():
    gemiddeldSalaris = data['Salaris_bruto'].mean()

    return(f'Het gemiddelde salaris is: {gemiddeldSalaris}')

"""
Bereken het gemiddelde salaris voor functie X
"""
def choice2():
    functie = input('Welke functie: ')
    functie = functie[0].upper() + functie[1:]

    functieFilter = (data['Functie'] == functie)

    gemiddeldSalaris = data[functieFilter]["Salaris_bruto"].mean()
    os.system('cls')

    return(f'Het gemiddelde salaris voor functie {functie} is: {gemiddeldSalaris}')

"""
Bereken het aantal werknemers binnen 2 jaar met pensioen

!PENSIOENLEEFTIJD IS 67 JAAR!
"""
def choice3():
    willRetire = 0
    for i in data['Geboortedatum']:
        birthDate = datetime.strptime(i, '%d-%m-%Y')
        today = datetime.today()
        age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
        if age >= 65:
            willRetire += 1


    return(f'Aantal werknemers binnen 2 jaar met pensioen: {willRetire}')

"""
Bereken het aantal chauffeurs
"""
def choice4():
    chauffeurCount = 0
    for i in data['Functie']:
        if i == 'Chauffeur':
            chauffeurCount += 1

    return(f'Aantal chauffeurs: {chauffeurCount}')

"""
Bereken het top 10 langst in dienst
"""
def choice5():
    data['Datum in dienst'] = pd.to_datetime(data['Datum in dienst'], format='%d-%m-%Y').sort_values()
    datumsSorted = data.sort_values(by='Datum in dienst')

    top10 = datumsSorted[['Voornaam', 'Achternaam', 'Datum in dienst']].head(10).to_string(index=False)

    return(f'Top 10 langst in dienst: \n{top10}')

"""
Bereken het aantal medewerkers met functie X bij afdeling Y
"""
def choice6():
    functie = input('Welke functie: ')
    functie = functie[0].upper() + functie[1:]

    afdeling = input('Welke afdeling: ')
    afdeling = afdeling[0].upper() + afdeling[1:]

    functieFilter = (data['Functie'] == functie)
    afdelingFilter = (data['Afdeling'] == afdeling)

    aantalMedewerkers = data[functieFilter & afdelingFilter].shape[0]

    os.system('cls')

    return(f'Aantal medewerkers met functie {functie} bij afdeling {afdeling}: {aantalMedewerkers}')


isRunning = True
while isRunning:
    # Windows Screen Clear
    os.system('cls')
    
    print('1. Bereken het gemiddelde salaris')
    print('2. Berekend het gemiddelde salaris voor functie X')
    print('3. Aantal werknemers binnen 2 jaar met pensioen')
    print('4. Aantal chauffeurs')
    print('5. Top 10 langst in dienst')
    print('6. Aantal medewerkers met functie X bij afdeling Y')
    print('W. Schrijf alle gegevens naar een bestand')

    print('X. Stop het programma')

    choice = input('\nMaak uw keuze: ').lower()

    if choice not in ['1', '2', '3', '4', '5', '6', 'w', 'x']:
        # Windows Screen Clear
        os.system('cls')
        
        print('Ongeldige keuze, probeer het opnieuw')

        input('\nDruk op enter om door te gaan...')

    elif choice == '1':
        # Windows Screen Clear
        os.system('cls')

        print(choice1())

        input('\nDruk op enter om door te gaan...')

    elif choice == '2':
        # Windows Screen Clear
        os.system('cls')

        print(choice2())

        input('\nDruk op enter om door te gaan...')

    elif choice == '3':
        # Windows Screen Clear
        os.system('cls')

        print(choice3())
        
        input('\nDruk op enter om door te gaan...')

    elif choice == '4':
        # Windows Screen Clear
        os.system('cls')

        print(choice4())

        input('\nDruk op enter om door te gaan...')

    elif choice == '5':
        # Windows Screen Clear
        os.system('cls')

        print(choice5())

        input('\nDruk op enter om door te gaan...')

    elif choice == '6':
        # Windows Screen Clear
        os.system('cls')
        
        print(choice6())

        input('\nDruk op enter om door te gaan...')

    elif choice == 'w':
        # Windows Screen Clear
        os.system('cls')

        """
        Print alle statestieken naar een bestand

        !OUTPUT BESTAND WORDT OVERSCHREVEN!
        """

        choice1 = choice1()

        os.system('cls')
        print('2. Gemiddeld salaris voor functie X')
        choice2 = choice2()
        choice3 = choice3()
        choice4 = choice4()
        choice5 = choice5()

        os.system('cls')
        print('6. Aantal medewerkers met functie X bij afdeling Y')
        choice6 = choice6()

        os.system('cls')
        with open('output.txt', 'w') as f:
            f.write(f'Statestieken berekend op: {datetime.now()}\n')
            f.write('--------------------------------------------\n')
            f.write(choice1 + '\n')
            f.write('--------------------------------------------\n')
            f.write(choice2 + '\n')
            f.write('--------------------------------------------\n')
            f.write(choice3 + '\n')
            f.write('--------------------------------------------\n')
            f.write(choice4 + '\n')
            f.write('--------------------------------------------\n')
            f.write(choice5 + '\n')
            f.write('--------------------------------------------\n')
            f.write(choice6 + '\n')
            f.write('--------------------------------------------\n')

        print('Alle gegevens zijn weggeschreven naar het bestand output.txt')
        input('\nDruk op enter om door te gaan...')

    elif choice == 'x':
        # Windows Screen Clear
        os.system('cls')
        isRunning = False
        print('Het programma wordt afgesloten')
