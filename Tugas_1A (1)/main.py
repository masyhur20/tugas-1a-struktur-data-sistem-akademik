from produk import Produk
from inventaris import Inventaris

def tampilkan_produk(produk):
    harga = f"Rp{produk.harga:,.0f}".replace(',', '.')

    print(
        f"ID: {produk.id_produk}, "
        f"Nama: {produk.nama}, "
        f"Brand: {produk.brand}, "
        f"Kategori: {produk.kategori}, "
        f"Harga: {harga}, "
        f"Stok: {produk.stok}"
    )

def main():
    inventaris = Inventaris()

    while True:
        print("\nSistem Inventaris Perusahaan M-Tech")
        print("1. Tambah Produk")
        print("2. Hapus Produk")
        print("3. Tampilkan Produk")
        print("4. Cari Produk")
        print("5. Keluar")
        pilihan = input("Pilih menu (1-5): ").strip()

        if pilihan not in ["1", "2", "3", "4", "5"]:
            print("Pilihan tidak valid. Silakan pilih menu (1-5).")
            continue
    
        if pilihan == "1":
            while True:
                id_produk = input ("Id produk (ketik 'back' untuk kembali): ").strip()
                if id_produk.lower() == "back":
                    break

                nama_produk = input("Nama produk: ")
                brand_produk = input("Brand produk: ")
                kategori_produk = input("Kategori produk: ")

                try:
                    harga_produk = int(input("Harga produk: "))
                    stok_produk = int(input("Stok produk: "))

                    if harga_produk < 0 or stok_produk < 0:
                        print("Harga dan stok harus berupa angka positif. Silakan coba lagi.")
                        continue

                except ValueError:
                    print("Harga dan stok harus berupa angka. Silakan coba lagi.")
                    continue

                produk = Produk(
                    id_produk, 
                    nama_produk, 
                    brand_produk, 
                    kategori_produk, 
                    harga_produk, 
                    stok_produk
                )

                if inventaris.tambah_produk(produk):
                    print(f"Produk dengan ID {id_produk} berhasil ditambahkan.\n")

                else:
                    print(f"Produk dengan ID {id_produk} sudah ada. Silakan gunakan ID yang berbeda.\n")


        elif pilihan == "2":
            id_produk = input("Masukkan ID produk yang ingin dihapus: ").strip()
            if inventaris.hapus_produk(id_produk):
                print(f"Produk dengan ID {id_produk} berhasil dihapus.")
            else:
                print(f"Produk dengan ID {id_produk} tidak ditemukan.")

        elif pilihan == "3":
            print("\nDaftar Produk Tersedia:")

            if not inventaris.produk_dict:
                print("Tidak ada produk yang tersedia.")

            else:
                for produk in inventaris.produk_dict.values():
                    tampilkan_produk(produk)


        elif pilihan == "4":
            id_produk = input("Masukkan ID produk yang ingin dicari: ").strip()
            produk = inventaris.cari_produk(id_produk)
            if produk:
                print(f"Produk ditemukan:")
                tampilkan_produk(produk)

            else:
                print(f"Produk dengan ID {id_produk} tidak ditemukan.")

        elif pilihan == "5":
            print("Terima kasih telah menggunakan Sistem Inventaris Perusahaan M-Tech.")
            break

if __name__ == "__main__":
    main()



    