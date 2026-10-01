class Data_Array:
    def __init__(self):
        self.data = []

    def tambah_data(self, nim, nama, jurusan):
        mahasiswa = {
            "nim": nim,
            "nama": nama,
            "jurusan": jurusan
        }

        self.data.append(mahasiswa)

    def tampilkan_data(self):
        if len(self.data) == 0:
            print("Tidak ada data mahasiswa.")
            return

        else:
            print("\nData Mahasiswa:")
            for mahasiswa in range(len(self.data)):
                print(f"\nNIM: {self.data[mahasiswa]['nim']}")
                print(f"Nama: {self.data[mahasiswa]['nama']}")
                print(f"Jurusan: {self.data[mahasiswa]['jurusan']}")