import time
from linked_list import LinkedList

# DELETE MENGGUNAKAN LIST 
produk_list = []

for i in range(1, 1000001):
    id_produk = f"DJI{i:06d}"
    produk_list.append(id_produk)

target_id = "DJI1000000"

mulai = time.perf_counter()

produk_list.remove(target_id)

selesai = time.perf_counter()


print("DELETE LIST")
print(f"Waktu delete 1 data: {selesai - mulai:.6f} detik")


# DELETE MENGGUNAKAN LINKED LIST
linked_list = LinkedList()

for i in range(1, 1000001):
    id_produk = f"DJI{i:06d}"
    linked_list.append(id_produk)

target_id = "DJI1000000"

mulai = time.perf_counter()
linked_list.delete(target_id)
selesai = time.perf_counter()

print("\nDELETE LINKED LIST")
print(f"Waktu delete 1 data: {selesai - mulai:.9f} detik")


# DELETE MENGGUNAKAN DICT 
produk_dict = {}

for i in range(1, 1000001):
    id_produk = f"DJI{i:06d}"
    produk_dict[id_produk] = id_produk

target_id = "DJI1000000"

mulai = time.perf_counter()

del produk_dict[target_id]

selesai = time.perf_counter()

print("\nDELETE DICTIONARY")
print(f"Waktu delete Dict: {selesai - mulai:.9f} detik")