hytti = str(input('Syötä hyttiluokka (LUX, A, B, C):'))


if hytti in 'LUX':
    print('LUX on parvekkeellinen hytti yläkannella.')
elif hytti in 'A':
    print('B on ikkunaton hytti autokannen yläpuolella.')
elif hytti in 'B':
    print('B on ikkunaton hytti autokannen yläpuolella.')
elif hytti in 'C':
    print('C on ikkunaton hytti autokannen alapuolella')
else:
    print('Virheellinen hyttiluokka')
