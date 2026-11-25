# Mengimpor class yang dipakai program
from roti_tawar import RotiTawar
from roti_manis import RotiManis
from roti_asin import RotiAsin
from pelanggan import Pelanggan
from penjualan import Penjualan

# Method mencari produk menggunakan kode
def cari_dengan_kode(daftar_produk, kode):
    for produk in daftar_produk:
        if produk.get_kode_produk().lower() == kode.lower():
            return produk
    return None

# Method Menambahkan produk dengan memilih jenis roti
def tambah_produk(daftar_produk):
    print("\nJenis roti:")
    print("1. Tawar")
    print("2. Manis")
    print("3. Asin")

    pilihan = input("Pilih jenis: ")

    try:
        if pilihan == "1":
            kelas_roti = RotiTawar
        elif pilihan == "2":
            kelas_roti = RotiManis
        elif pilihan == "3":
            kelas_roti = RotiAsin
        else:
            raise ValueError("Jenis roti harus manis, tawar, asin")
    except ValueError as error:
        print(error)
        return

    kode = input("Kode produk: ").strip()

    if cari_dengan_kode(daftar_produk, kode):
        print("Kode produk sudah digunakan.")
        return

    nama = input("Nama produk: ").strip()

    try:
        harga = float(input("Harga: "))
        stok = int(input("Stok: "))

        produk = kelas_roti(kode, nama, harga, stok)
        daftar_produk.append(produk)
        print("Produk berhasil ditambahkan.")

    except ValueError as error:
        print("Data tidak valid:", error)

# Method Mengurangi stok produk secara manual
def kurangi_stok_produk(daftar_produk):
    kode = input("Masukkan kode produk: ")
    produk = cari_dengan_kode(daftar_produk, kode)

    if produk is None:
        print("Produk tidak ditemukan.")
        return

    try:
        jumlah = int(input("Jumlah stok yang dikurangi: "))

        if produk.kurangi_stok(jumlah):
            print("Stok berhasil dikurangi.")
        else:
            print("Jumlah tidak valid atau stok tidak cukup.")

    except ValueError:
        print("Jumlah harus berupa angka.")

# Meminta setiap produk menampilkan informasinya
def tampilkan_produk(daftar_produk):
    if not daftar_produk:
        print("Belum ada produk.")
        return

    for produk in daftar_produk:
        print()
        produk.tampilkan_info()

# Mencari dan menampilkan satu produk
def cari_produk(daftar_produk):
    kode = input("Masukkan kode produk: ")
    produk = cari_dengan_kode(daftar_produk, kode)

    if produk:
        produk.tampilkan_info()
    else:
        print("Produk tidak ditemukan.")


# Mengubah harga dan menambah stok produk
def ubah_produk(daftar_produk):
    kode = input("Masukkan kode produk: ")
    produk = cari_dengan_kode(daftar_produk, kode)

    if produk is None:
        print("Produk tidak ditemukan.")
        return

    try:
        harga_baru = float(input("Harga baru: "))

        if not produk.ubah_harga(harga_baru):
            print("Harga tidak boleh negatif.")
            return

        stok_tambahan = int(input("Stok tambahan: "))

        if stok_tambahan > 0:
            produk.tambah_stok(stok_tambahan)

        print("Produk berhasil diubah.")

    except ValueError:
        print("Harga dan stok harus berupa angka.")

# Menampilkan status stok produk
def cek_status(daftar_produk):
    kode = input("Masukkan kode produk: ")
    produk = cari_dengan_kode(daftar_produk, kode)

    if produk:
        print("Nama  :", produk.get_nama())
        print("Stok  :", produk.get_stok())
        print("Status:", produk.cek_status_stok())
    else:
        print("Produk tidak ditemukan.")

# Membuat transaksi berisi satu atau beberapa produk
def buat_penjualan(daftar_produk, daftar_penjualan):
    if not daftar_produk:
        print("Belum ada produk untuk dijual.")
        return

    kode = input("Kode pelanggan: ")
    nama = input("Nama pelanggan: ")
    telepon = input("Nomor telepon: ")

    try:
        pelanggan = Pelanggan(kode, nama, telepon)
    except ValueError as error:
        print(error)
        return

    nomor = f"TRX{len(daftar_penjualan) + 1:03d}"
    transaksi = Penjualan(nomor, pelanggan)

    tampilkan_produk(daftar_produk)

    while True:
        kode_produk = input(
            "\nKode roti (ketik 'selesai' untuk mengakhiri): "
        )

        if kode_produk.lower() == "selesai":
            break

        produk = cari_dengan_kode(daftar_produk, kode_produk)

        if produk is None:
            print("Produk tidak ditemukan.")
            continue

        try:
            jumlah = int(input("Jumlah: "))

            if transaksi.tambah_produk(produk, jumlah):
                print("Produk masuk ke transaksi.")
            else:
                print("Jumlah tidak valid atau stok tidak cukup.")

        except ValueError:
            print("Jumlah harus berupa angka.")

    if transaksi.selesaikan():
        daftar_penjualan.append(transaksi)
        transaksi.tampilkan_struk()
    else:
        print("Transaksi kosong.")

# Menu utama aplikasi
def main():
    daftar_produk = []
    daftar_penjualan = []

    while True:
        print("\n=== TOKO ROTI ===")
        print("1. Tambah produk")
        print("2. Tampilkan produk")
        print("3. Cari produk")
        print("4. Ubah produk")
        print("5. Cek status stok")
        print("6. Buat penjualan")
        print("7. Kurangi stok produk")
        print("0. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tambah_produk(daftar_produk)
        elif pilihan == "2":
            tampilkan_produk(daftar_produk)
        elif pilihan == "3":
            cari_produk(daftar_produk)
        elif pilihan == "4":
            ubah_produk(daftar_produk)
        elif pilihan == "5":
            cek_status(daftar_produk)
        elif pilihan == "6":
            buat_penjualan(daftar_produk, daftar_penjualan)
        elif pilihan == "7":
            kurangi_stok_produk(daftar_produk)
        elif pilihan == "0":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak tersedia.")

# Memulai program
if __name__ == "__main__":
    main()