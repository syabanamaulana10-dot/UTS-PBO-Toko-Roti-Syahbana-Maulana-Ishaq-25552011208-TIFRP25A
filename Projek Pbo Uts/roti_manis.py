# Subclass roti manis mewarisi ProdukRoti
from produk_roti import ProdukRoti

class RotiManis(ProdukRoti):
    def __init__(self, kode, nama, harga, stok):
        super().__init__(kode, nama, harga, stok)
        self.__jenis = "Manis"

    def get_jenis_roti(self):
        return self.__jenis

    def tampilkan_info(self):
        super().tampilkan_info()