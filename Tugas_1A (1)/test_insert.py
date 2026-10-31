import time
from linked_list import LinkedList

# INSERT MENGGUNAKAN LIST      
produk_list = []

mulai = time.perf_counter()
for i in range (1,1000001):
    id_produk = f"DJI{i:06d}"
    produk_list.append(id_produk)

selesai = time.perf_counter()
waktu_eksekusi = selesai - mulai

print(len(produk_list))
print(f"Waktu eksekusi List: {waktu_eksekusi:.6f} detik")


# INSERT MENGGUNAKAN LINKED LIST      
linked_list = LinkedList()

mulai = time.perf_counter()

for i in range(1,1000001):
    id_produk = f"DJI{i:06d}"
    linked_list.append(id_produk)

selesai = time.perf_counter()

waktu_eksekusi = selesai - mulai

print("\nINSERT LINKED LIST")
print(f"Jumlah data: 1000000")
print(f"Waktu insert Linked List: {waktu_eksekusi:.6f} detik\n")

# INSERT MENGGUNAKAN DICT     
produk_dict = {}

mulai = time.perf_counter()

for i in range(1, 1000001):
    id_produk = f"DJI{i:06d}"
    produk_dict[id_produk] = id_produk

selesai = time.perf_counter()
waktu_eksekusi = selesai - mulai

print(len(produk_dict))
print(f"Waktu eksekusi Dict: {waktu_eksekusi:.6f} detik")