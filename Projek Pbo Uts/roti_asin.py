# Subclass roti asin mewarisi ProdukRoti
from produk_roti import ProdukRoti

class RotiAsin(ProdukRoti):
    def __init__(self, kode, nama, harga, stok):
        super().__init__(kode, nama, harga, stok)
        self.__jenis = "Asin"

    def get_jenis_roti(self):
        return self.__jenis

    def tampilkan_info(self):
        super().tampilkan_info()