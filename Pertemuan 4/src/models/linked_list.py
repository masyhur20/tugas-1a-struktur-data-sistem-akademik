from models.linked_list_node import Node


class LinkedList:
    def __init__(self, head = None):
        self.head = head


    # Menambah data di awal
    def add_first(self, data):
        node_baru = Node(data)

        node_baru.next = self.head
        self.head = node_baru


    # Menambah data di akhir
    def add_last(self, data):
        node_baru = Node(data)

        if self.head is None:
            self.head = node_baru
            return

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = node_baru


    # Menambah data berdasarkan index
    def add_at(self, index, data):

        if index == 0:
            self.add_first(data)
            return

        node_baru = Node(data)

        current = self.head
        posisi = 0

        while current is not None:

            if posisi == index - 1:
                node_baru.next = current.next
                current.next = node_baru
                return

            current = current.next
            posisi += 1

        print("Index tidak ditemukan")


    # Menghapus data pertama
    def remove_first(self):

        if self.head is None:
            return None

        data_hapus = self.head.data

        self.head = self.head.next

        return data_hapus


    # Menghapus data terakhir
    def remove_last(self):

        if self.head is None:
            return None


        # jika hanya satu node
        if self.head.next is None:
            data_hapus = self.head.data
            self.head = None
            return data_hapus


        current = self.head

        while current.next.next is not None:
            current = current.next


        data_hapus = current.next.data

        current.next = None

        return data_hapus



    # Menghapus data berdasarkan index
    def remove_at(self, index):

        if self.head is None:
            return None


        if index == 0:
            return self.remove_first()


        current = self.head
        posisi = 0


        while current.next is not None:

            if posisi == index - 1:

                data_hapus = current.next.data

                current.next = current.next.next

                return data_hapus


            current = current.next
            posisi += 1


        return None



    # Mencari data
    def find(self, data):

        current = self.head
        index = 0


        while current is not None:

            if current.data == data:
                return index


            current = current.next
            index += 1


        return -1



    # Menampilkan isi linked list
    def display(self):

        current = self.head

        while current is not None:

            print(current.data, end=" -> ")

            current = current.next


        print("None")