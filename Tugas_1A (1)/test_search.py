import time
from linked_list import LinkedList

# SEARCH MENGGUNAKAN LIST      
# produk_list = []

# for i in range (1,1000001):
#     id_produk = f"DJI{i:06d}"
#     produk_list.append(id_produk)

#     print(len(produk_list))

# target_id = "DJI1000000"

# mulai = time.perf_counter()

# for _ in range (10000):
#     if target_id in produk_list:
#         pass

# selesai = time.perf_counter()
# waktu_eksekusi = selesai - mulai

# print(f"Waktu eksekusi: {waktu_eksekusi:.6f} detik")


# SEARCH MENGGUNAKAN LINKED LIST
# linked_list = LinkedList()

# for i in range(1, 100001):
#     id_produk =  f"DJI{i:06d}"
#     linked_list.append(id_produk)
    
# target_id = "DJI100000"
# mulai = time.perf_counter()

# for _ in range(10000):
#     linked_list.search(target_id)

# selesai = time.perf_counter()

# waktu_eksekusi = selesai - mulai

# print(f"Waktu search Linked List: {waktu_eksekusi:.6f} detik")


# SEARCH MENGGUNAKAN DICT  
produk_dict = {}
for i in range (1,1000001):
    id_produk = f"DJI{i:06d}"
    produk_dict[id_produk] = id_produk

print(len(produk_dict))

target_id = "DJI1000000"

mulai = time.perf_counter()
for _ in range (10000):
    if target_id in produk_dict:
        pass

selesai = time.perf_counter()
waktu_eksekusi = selesai - mulai

print(f"Waktu eksekusi: {waktu_eksekusi:.6f} detik")


