class Array:
    def __init__(self):
        self.data = []

    # Menambah data di awal
    def add_first(self, data):
        self.data.insert(0, data)

    # Menambah data di akhir
    def add_last(self, data):
        self.data.append(data)

    # Menambah data berdasarkan index
    def add_at(self, index, data):
        self.data.insert(index, data)

    # Menghapus data pertama
    def remove_first(self):
        if len(self.data) == 0:
            return None

        return self.data.pop(0)

    # Menghapus data terakhir
    def remove_last(self):
        if len(self.data) == 0:
            return None

        return self.data.pop()

    # Menghapus data berdasarkan index
    def remove_at(self, index):
        if index < 0 or index >= len(self.data):
            return None

        return self.data.pop(index)

    # Mencari data
    def find(self, data):
        if data in self.data:
            return self.data.index(data)

        return -1

    # Menampilkan data
    def display(self):
        print(self.data)