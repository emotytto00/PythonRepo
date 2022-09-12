vuodenaika = ('Talvi', 'Kevät', 'Kesä', 'Syksy')

kuukausi = int(input('Anna kuukauden numero: '))

if 1 <= kuukausi < 2:
    print(vuodenaika[0])
elif 3 <= kuukausi <= 5:
    print(vuodenaika[1])
elif 6 <= kuukausi <= 8:
    print(vuodenaika[2])
elif 9 <= kuukausi <= 11:
    print(vuodenaika[3])
else:
    print(vuodenaika[0])

