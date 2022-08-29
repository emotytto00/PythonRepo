sukupuoli = str(input('Anna sukupuoli: '))
hemoG = int(input('Kerro hemoglobiiniarvosi (g/l)'))

if sukupuoli in 'nainen':
    if hemoG < 117:
        print('Hemoglobiinisi on alhainen')
    elif 117 <= hemoG <= 175:
        print('Hemoglobiinisi on normaali')
    else:
        print('Hemoglobiinisi on korkea')

if sukupuoli in 'mies':
    if hemoG < 134:
        print('Hemoglobiinisi on alhainen')
    elif 134 <= hemoG <= 195:
        print('Hemoglobiinisi on normaali')
    else:
        (print('Hemoglobiinisi on korkea'))