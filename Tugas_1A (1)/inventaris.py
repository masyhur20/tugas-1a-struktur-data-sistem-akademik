
class Inventaris:
    def __init__(self):
        self.produk_dict = {}

    def tambah_produk(self, produk):
        if produk.id_produk in self.produk_dict:
            return False  # Produk dengan ID yang sama sudah ada

        self.produk_dict[produk.id_produk] = produk
        return True

    def hapus_produk(self, id_produk):
        if id_produk in self.produk_dict:
            del self.produk_dict[id_produk]
            return True
        return False

    def cari_produk(self, id_produk):
        return self.produk_dict.get(id_produk)