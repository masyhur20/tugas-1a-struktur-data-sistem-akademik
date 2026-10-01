from collections import deque

class Queue:
    def __init__(self):
        self.antrean = deque()

    def tambah_data(self, nim, nama, jurusan):
        mahasiswa = {
            "nim": nim,
            "nama": nama,
            "jurusan": jurusan
        }
        self.antrean.append(mahasiswa)

    def tampilkan_data(self):
        if len(self.antrean) == 0:
            print("Tidak ada data mahasiswa dalam antrean.")
            return

        else:
            print("\nData Mahasiswa dalam Antrean:")
            for mahasiswa in self.antrean:
                print(f"\nNIM: {mahasiswa['nim']}")
                print(f"Nama: {mahasiswa['nama']}")
                print(f"Jurusan: {mahasiswa['jurusan']}")

    def proses_antrean(self):
        if len(self.antrean) > 0:
            return self.antrean.popleft()
        else:
            return None