import time
from models.array import Array

def main():
    array = Array()

    print("=== ADD DATA ===")
    waktu_mulai = time.perf_counter() # Cek waktu awal
    array.add_first("Ahmad")
    array.add_last("Budi")
    array.add_last("Citra")
    array.add_at(1, "Dewi")
    waktu_selesai = time.perf_counter() # Cek waktu akhir
    array.display()
    durasi = waktu_selesai - waktu_mulai
    print("Waktu: ",durasi," detik")

    print("\n=== FIND DATA ===")
    data_cari = "Citra"
    waktu_mulai = time.perf_counter() # Cek waktu awal
    index = array.find(data_cari)
    waktu_selesai = time.perf_counter() # Cek waktu akhir

    print("Data",data_cari,"berada pada index:",index)
    durasi = waktu_selesai - waktu_mulai
    print("Waktu: ",durasi," detik")


    print("\n=== REMOVE DATA ===")
    waktu_mulai = time.perf_counter() # Cek waktu awal
    print("Hapus pertama:",array.remove_first())
    waktu_selesai = time.perf_counter() # Cek waktu akhir
    array.display()
    durasi = waktu_selesai - waktu_mulai
    print("Waktu: ",durasi," detik")

    waktu_mulai = time.perf_counter() # Cek waktu awal
    print("Hapus terakhir:",array.remove_last())
    waktu_selesai = time.perf_counter() # Cek waktu akhir
    array.display()
    durasi = waktu_selesai - waktu_mulai
    print("Waktu: ",durasi," detik")

    waktu_mulai = time.perf_counter() # Cek waktu awal
    print("Hapus index 1:",array.remove_at(1))
    waktu_selesai = time.perf_counter() # Cek waktu akhir
    array.display()
    durasi = waktu_selesai - waktu_mulai
    print("Waktu: ",durasi," detik")

if __name__ == "__main__":
    main()