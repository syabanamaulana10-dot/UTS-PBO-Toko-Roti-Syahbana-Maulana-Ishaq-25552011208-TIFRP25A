# Class transaksi yang berhubungan dengan pelanggan dan beberapa produk
class Penjualan:
    def __init__(self, nomor, pelanggan):
        self.__nomor = nomor
        self.__pelanggan = pelanggan
        self.__daftar_produk = []
        self.__total = 0
        self.__status = "Berlangsung"

    # Menambahkan produk ke transaksi dan mengurangi stoknya
    def tambah_produk(self, produk, jumlah):
        if jumlah <= 0 or jumlah > produk.get_stok():
            return False

        if not produk.kurangi_stok(jumlah):
            return False

        subtotal = produk.get_harga() * jumlah
        self.__daftar_produk.append((produk, jumlah, subtotal))
        self.__total += subtotal
        return True

    # Menyelesaikan transaksi jika ada produk yang dibeli
    def selesaikan(self):
        if not self.__daftar_produk:
            return False

        self.__status = "Selesai"
        return True

    def get_status(self):
        return self.__status

    # Class transaksi menampilkan struknya sendiri
    def tampilkan_struk(self):
        print("\n=== STRUK PENJUALAN ===")
        print("Nomor transaksi:", self.__nomor)
        print("Pelanggan      :", self.__pelanggan.get_nama())
        print("Telepon        :", self.__pelanggan.get_telepon())
        print("Status         :", self.__status)
        print("-----------------------")

        for produk, jumlah, subtotal in self.__daftar_produk:
            print(
                produk.get_nama(),
                "x", jumlah,
                "=", f"Rp{subtotal:,.0f}".replace(",", ".")
            )

        print("-----------------------")
        print("Total:", f"Rp{self.__total:,.0f}".replace(",", "."))