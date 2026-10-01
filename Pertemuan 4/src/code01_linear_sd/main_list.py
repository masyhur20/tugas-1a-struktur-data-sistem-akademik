from services.mahasiswa_reader import MahasiswaReader

def main():
    # Membuat objek pembaca CSV
    reader = MahasiswaReader("data/data_mahasiswa_dummy_200.csv")

    # Membaca data dan menghasilkan list mahasiswa
    list_mahasiswa = reader.baca_data()

    # Menampilkan beberapa data
    for mhs in list_mahasiswa[:5]:
        mhs.info()

    # Menampilkan data indeks ke 99
    list_mahasiswa[99].info()

if __name__ == "__main__":
    main()