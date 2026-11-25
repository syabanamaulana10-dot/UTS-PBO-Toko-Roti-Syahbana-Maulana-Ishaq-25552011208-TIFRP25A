# Subclass roti tawar mewarisi ProdukRoti
from produk_roti import ProdukRoti

class RotiTawar(ProdukRoti):
    def __init__(self, kode, nama, harga, stok):
        super().__init__(kode, nama, harga, stok)
        self.__jenis = "Tawar"

    def get_jenis_roti(self):
        return self.__jenis

    def tampilkan_info(self):
        super().tampilkan_info()