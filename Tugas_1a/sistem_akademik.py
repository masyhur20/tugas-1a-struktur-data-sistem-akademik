### SISTEM PELAYANAN SPBU PASTI PAS ###

### NAMA    : M. MUSTHOFA MASYHUR           DOSEN PENGAMPU  : MUHAMMAD AFFANDES, S.T, M.T.
### NIM     : 12550111055                   MATA KULIAH     : STRUKTUR DATA
### KELAS   : 3B                            TUGAS           : 1A


from data_array import Data_Array
from queue import Queue
from stack import Stack
from hashtable import HashTable

data_mahasiswa = Data_Array()
data_antrean = Queue() 
undo = Stack()
data_hash = HashTable()

def main():
    while True:
        print("\n Sistem Penilaian Akademik Mahasiswa Universitas Indonesia")
        print("1. Data Mahasiswa")
        print("2. Sistem Antrean")
        print("3. Pencarian Data Mahasiswa")
        print("4. Keluar")
        pilihan = input("Pilih menu (1-4): ")

        if pilihan == "1":
            while True:
                print("\nMenu Data Mahasiswa:")
                print("1. Tambah Data Mahasiswa")
                print("2. Tampilkan Data Mahasiswa")
                print("3. Undo")
                print("4. Kembali ke Menu Utama")
                sub_pilihan = input("Pilih menu (1-4): ")

                if sub_pilihan == "1":
                    nim = input("Masukkan NIM: ")
                    nama = input("Masukkan Nama: ")
                    jurusan = input("Masukkan Jurusan: ")

                    undo.history.append(data_mahasiswa.data.copy())

                    data_mahasiswa.tambah_data(nim, nama, jurusan)
                    data_hash.tambah_data(nim, nama, jurusan)
                    print("Data mahasiswa berhasil ditambahkan.")

                elif sub_pilihan == "2":
                    data_mahasiswa.tampilkan_data()

                elif sub_pilihan == "3":
                    data_terakhir = undo.undo()
                    
                    if data_terakhir is not None:
                        data_mahasiswa.data = data_terakhir
                        data_hash.data.clear()

                        for mahasiswa in data_mahasiswa.data:
                            data_hash.tambah_data(
                                mahasiswa['nim'], 
                                mahasiswa['nama'], 
                                mahasiswa['jurusan']
                            )
                
                        print("Data mahasiswa berhasil di-undo.")
                    
                    else:
                        print("Tidak ada data yang dapat di-undo.")
                            
                    
                elif sub_pilihan == "4":
                    break

                else:
                    print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")
        
            
        elif pilihan == "2":
            while True:
                print("\nMenu Sistem Antrean:")
                print("1. Tambah Data Mahasiswa ke Antrean")
                print("2. Tampilkan Data Mahasiswa dalam Antrean")
                print("3. Proses Antrean")
                print("4. Kembali ke Menu Utama")
                sub_pilihan = input("Pilih menu (1-4): ")

                if sub_pilihan == "1":
                    nim = input("Masukkan NIM: ")
                    nama = input("Masukkan Nama: ")
                    jurusan = input("Masukkan Jurusan: ")
                    data_antrean.tambah_data(nim, nama, jurusan)
                    print("Data mahasiswa berhasil ditambahkan ke antrean.")

                elif sub_pilihan == "2":
                    data_antrean.tampilkan_data()

                elif sub_pilihan == "3":
                    if data_antrean.antrean:
                        print("Mahasiswa yang diproses:")
                        mahasiswa = data_antrean.proses_antrean()
                        print(f"NIM: {mahasiswa['nim']}, Nama: {mahasiswa['nama']}, Jurusan: {mahasiswa['jurusan']}")
                    else:
                        print("Antrean kosong.")


                elif sub_pilihan == "4":
                    break

                else:
                    print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")

        elif pilihan == "3":
            nim = input("Masukkan NIM yang ingin dicari: ")
            mahasiswa = data_hash.cari_data(nim)

            if mahasiswa:
                print("\ndata Mahasiswa ditemukan: ")
                print(f"NIM: {mahasiswa['nim']}")
                print(f"Nama: {mahasiswa['nama']}")
                print(f"Jurusan: {mahasiswa['jurusan']}")
            else:
                print("Mahasiswa tidak ditemukan.")
                
        elif pilihan == "4":
                print("Terima kasih telah menggunakan Sistem Akademik.")
                break
        else:
            print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")


if __name__ == "__main__":
    main()