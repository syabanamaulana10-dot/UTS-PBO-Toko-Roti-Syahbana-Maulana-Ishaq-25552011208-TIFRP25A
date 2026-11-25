# Class untuk menyimpan data pelanggan
class Pelanggan:
    def __init__(self, kode, nama, telepon):
        if not kode.strip() or not nama.strip() or not telepon.strip():
            raise ValueError("Data pelanggan harus diisi")

        # Atribut pelanggan dibuat private
        self.__kode = kode
        self.__nama = nama
        self.__telepon = telepon

    # Getter untuk membaca data pelanggan
    def get_kode(self):
        return self.__kode

    def get_nama(self):
        return self.__nama

    def get_telepon(self):
        return self.__telepon

    # Menampilkan data pelanggan
    def tampilkan_info(self):
        print("Kode pelanggan:", self.__kode)
        print("Nama pelanggan:", self.__nama)
        print("Telepon       :", self.__telepon)