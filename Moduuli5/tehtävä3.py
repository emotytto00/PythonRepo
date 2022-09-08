numero = int(input('Anna luku: '))
jako = False
if numero != 2 and not numero % 2:
    jako = True
for i in range(2,numero):
    if not numero % i:
        jako = True
    if jako:
        break
if jako:
    print(f'{numero} ei ole alkuluku')
else:
    print(f'{numero} on alkuluku')
