# Class induk untuk semua jenis roti
class ProdukRoti:
    def __init__(self, kode, nama, harga, stok):
        if not kode.strip() or not nama.strip():
            raise ValueError("Kode dan nama harus diisi")
        if harga < 0 or stok < 0:
            raise ValueError("Harga dan stok tidak boleh negatif")

        # Data dasar produk dibuat private
        self.__kode = kode
        self.__nama = nama
        self.__harga = harga
        self.__stok = stok

    # Getter untuk membaca data produk
    def get_kode_produk(self):
        return self.__kode

    def get_nama(self):
        return self.__nama

    def get_harga(self):
        return self.__harga

    def get_stok(self):
        return self.__stok

    def get_jenis_roti(self):
        return "Umum"

    # Mengubah harga dengan validasi
    def ubah_harga(self, harga_baru):
        if harga_baru < 0:
            return False

        self.__harga = harga_baru
        return True

    # Mengelola jumlah stok
    def tambah_stok(self, jumlah):
        if jumlah <= 0:
            return False

        self.__stok += jumlah
        return True

    def kurangi_stok(self, jumlah):
        if jumlah <= 0 or jumlah > self.__stok:
            return False

        self.__stok -= jumlah
        return True

    # Status stok dihitung otomatis
    def cek_status_stok(self):
        if self.__stok == 0:
            return "Habis"
        elif self.__stok <= 5:
            return "Stok menipis"
        return "Tersedia"

    # Setiap objek produk menampilkan datanya sendiri
    def tampilkan_info(self):
        print("Kode  :", self.__kode)
        print("Nama  :", self.__nama)
        print("Jenis :", self.get_jenis_roti())
        print("Harga :", f"Rp{self.__harga:,.0f}".replace(",", "."))
        print("Stok  :", self.__stok)
        print("Status:", self.cek_status_stok())