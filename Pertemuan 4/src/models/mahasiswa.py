class Mahasiswa:
    def __init__(self, indeks, nim, nama, prodi, ipk):
        self.indeks = indeks
        self.nim = nim
        self.nama = nama
        self.prodi = prodi
        self.ipk = ipk

    def info(self):
        print("========================")
        print("Indeks   :", self.indeks)
        print("NIM      :", self.nim)
        print("Nama     :", self.nama)
        print("Prodi    :", self.prodi)
        print("IPK      :", self.ipk)
        print("Predikat :", self.predikat())

    def predikat(self):
        if self.ipk >= 3.50:
            return "Sangat Memuaskan"
        elif self.ipk >= 3.00:
            return "Memuaskan"
        elif self.ipk >= 2.75:
            return "Cukup"
        else:
            return "Kurang"
