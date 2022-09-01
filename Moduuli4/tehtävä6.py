import random
pisteet = int(input('Anna pisteiden lukumäärä'))
ympyräP = 0
neliöP = 0

for i in range(pisteet**2):
    rand_x = random.uniform(-1, 1)
    rand_y = random.uniform(-1, 1)
    origin_dis = (rand_y**2 + rand_x**2)
    if origin_dis <= 1:
        ympyräP += 1
    neliöP += 1
    pi = 4*(ympyräP/neliöP)
print(f'Piin desimaalit: {pi:.10f}')