class HashTable:
    def __init__(self):
        self.data = {}

    def tambah_data(self, nim, nama, jurusan):
        mahasiswa = {
            "nim": nim,
            "nama": nama,
            "jurusan": jurusan
        }
        self.data[nim] = mahasiswa

    def cari_data(self, nim):
        if nim in self.data:
            return self.data[nim]
        else:
            return None