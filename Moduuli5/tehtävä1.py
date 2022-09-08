import random

lkm = int(input('Anna noppien lukumäärä: '))
summa = 0
for luku in range(lkm):
    heitto = random.randint(1,6)
    print(f'Heitosta tuli {heitto}!')
    summa = summa + heitto
print(f'Summa oli huikeat {summa}')