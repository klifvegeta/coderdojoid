class Segitiga():
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi

    def hitung_luas(self):
        return (self.alas * self.tinggi) / 2

    def get_info(self):
        print('Informasi segitiga. Alas= ', self.alas, ', tinggi = ', self.tinggi)

segitiga = Segitiga(2, 5)
segitiga.get_info()
print(segitiga.hitung_luas())