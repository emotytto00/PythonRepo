class Hissi():


    def __init__(self, alin=0, ylin=9):
        self.alin = alin
        self.ylin = ylin
        self.tämä_kerros = alin


    def siirry_kerrokseen(self, numero):
        if numero > self.tämä_kerros:
            if numero > self.ylin:
                print('Instructions unclear, went out of elevator bounds :/')
            else:
                while self.tämä_kerros < numero:
                    self.kerros_ylös()
        elif numero < self.tämä_kerros:
            if numero < self.alin:
                print('Instructions unclear, went out of elevator bounds :/')
            else:
                while self.tämä_kerros > numero:
                    self.kerros_alas()



    def kerros_ylös(self):
        if self.tämä_kerros + 1 > self.ylin:
            print(f'Et pääse korkeemmalle kun {self.tämä_kerros} bro')
        else:
            self.tämä_kerros += 1
        print(f'Olet saapunut {self.tämä_kerros}. kerrokseen!')

    def kerros_alas(self):
        if self.tämä_kerros - 1 < self.alin:
            print(f'Et pääse alemmaksi kun {self.tämä_kerros}. brouski')
        else:
            self.tämä_kerros -= 1
        print(f'Olet saapunut {self.tämä_kerros} kerrokseen!')

class Talo():

    def __init__(self, alin, ylin, hissit):
        self.alin = alin
        self.ylin = ylin
        self.hissit = hissit

        self.hissilista = []
        for i in range(self.hissit):
            self.hissilista.append(Hissi(self.ylin, self.alin))

    def aja_hissiä(self, hissinro, minne):
        tämä_hissi = self.hissilista[hissinro]
        tämä_hissi.siirry_kerrokseen(minne)


huussi = Talo(0, 10, 4)
huussi.aja_hissiä(2, 4)