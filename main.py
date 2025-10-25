import datetime

# Struktur data Santri
class Santri:
    def __init__(self, id, nama, kelas, saldo=0.0):
        self.id = id
        self.nama = nama
        self.kelas = kelas
        self.saldo = saldo

# Struktur data Transaksi
class Transaksi:
    def __init__(self, id, id_santri, jenis, jumlah, tanggal, status):
        self.id = id
        self.id_santri = id_santri
        self.jenis = jenis
        self.jumlah = jumlah
        self.tanggal = tanggal
        self.status = status

# Fungsi mendapatkan tanggal saat ini
def get_current_date():
    now = datetime.datetime.now()
    return now.strftime("%d/%m/%Y")

# Kelas utama sistem pembayaran
class SistemPembayaranSyariah:
    def __init__(self):
        self.daftar_santri = []
        self.daftar_transaksi = []
        self.next_santri_id = 1
        self.next_transaksi_id = 1
        
        # Data dummy
        self.tambah_santri("Arya Alamsa", "TPA 1")
        self.tambah_santri("Achmad Reyzaldi", "MTs 2")
        self.tambah_santri("Muhammad Ali", "MA 3")

    def tambah_santri(self, nama, kelas):
        santri = Santri(self.next_santri_id, nama, kelas)
        self.daftar_santri.append(santri)
        self.next_santri_id += 1

    def tampilkan_daftar_santri(self):
        print("\n=== DAFTAR SANTRI ===")
        print(f"{'ID':<5}{'Nama':<20}{'Kelas':<15}{'Saldo':<15}")
        print("-" * 55)
        for s in self.daftar_santri:
            print(f"{s.id:<5}{s.nama:<20}{s.kelas:<15}Rp {s.saldo:,.2f}")

    def lakukan_pembayaran(self):
        print("\n=== PEMBAYARAN SYARIAH SANTRI ===")
        self.tampilkan_daftar_santri()

        try:
            id_santri = int(input("Masukkan ID Santri: "))
        except ValueError:
            print("Input tidak valid!")
            return

        santri = next((s for s in self.daftar_santri if s.id == id_santri), None)
        if not santri:
            print("Santri tidak ditemukan!")
            return

        print(f"Santri: {santri.nama} ({santri.kelas})")
        print(f"Saldo saat ini: Rp {santri.saldo:,.2f}\n")

        print("Jenis Pembayaran:")
        print("1. SPP Bulanan")
        print("2. Daftar Ulang")
        print("3. Infaq")
        print("4. Pembangunan")

        pilihan = input("Pilih jenis (1-4): ")
        jenis_dict = {
            "1": "SPP Bulanan",
            "2": "Daftar Ulang",
            "3": "Infaq",
            "4": "Pembangunan"
        }
        jenis = jenis_dict.get(pilihan, "Lainnya")

        try:
            jumlah = float(input("Masukkan jumlah pembayaran: Rp "))
        except ValueError:
            print("Jumlah tidak valid!")
            return

        if jumlah <= 0:
            print("Jumlah harus lebih dari 0!")
            return

        print("\nKonfirmasi Pembayaran:")
        print(f"Santri: {santri.nama}")
        print(f"Jenis: {jenis}")
        print(f"Jumlah: Rp {jumlah:,.2f}")
        konfirmasi = input("Lanjutkan pembayaran? (y/n): ")

        if konfirmasi.lower() == 'y':
            transaksi = Transaksi(
                self.next_transaksi_id,
                santri.id,
                jenis,
                jumlah,
                get_current_date(),
                "Lunas"
            )
            self.daftar_transaksi.append(transaksi)
            santri.saldo += jumlah
            self.next_transaksi_id += 1

            print("\nPembayaran berhasil!")
            print(f"ID Transaksi: {transaksi.id}")
            print(f"Saldo terkini: Rp {santri.saldo:,.2f}")

            print("\n=== PRINSIP SYARIAH ===")
            print("1. Transaksi bebas dari riba")
            print("2. Dana digunakan untuk kemaslahatan umat")
            print("3. Transaksi jelas dan transparan")
        else:
            print("Pembayaran dibatalkan.")

    def tampilkan_riwayat_transaksi(self):
        print("\n=== RIWAYAT TRANSAKSI ===")
        if not self.daftar_transaksi:
            print("Belum ada transaksi.")
            return
        print(f"{'ID':<5}{'ID Santri':<10}{'Jenis':<20}{'Jumlah':<15}{'Tanggal':<12}{'Status':<10}")
        print("-" * 75)
        for t in self.daftar_transaksi:
            print(f"{t.id:<5}{t.id_santri:<10}{t.jenis:<20}Rp {t.jumlah:,.2f}   {t.tanggal:<12}{t.status:<10}")

    def tampilkan_dashboard(self):
        print("\n=== DASHBOARD SISTEM PEMBAYARAN SYARIAH ===")
        total_santri = len(self.daftar_santri)
        total_transaksi = len(self.daftar_transaksi)
        total_dana = sum(t.jumlah for t in self.daftar_transaksi)

        print(f"Total Santri: {total_santri}")
        print(f"Total Transaksi: {total_transaksi}")
        print(f"Total Dana: Rp {total_dana:,.2f}")

        if self.daftar_santri:
            santri_tertinggi = max(self.daftar_santri, key=lambda s: s.saldo)
            print(f"Santri dengan kontribusi tertinggi: {santri_tertinggi.nama} (Rp {santri_tertinggi.saldo:,.2f})")

        print("\nPrinsip Syariah yang Dianut:")
        print("1. Bebas dari riba dan ketidakjelasan")
        print("2. Transparansi dalam pengelolaan dana")
        print("3. Dana digunakan untuk kemaslahatan bersama")
        print("4. Adil dalam pembagian manfaat")

    def jalankan(self):
        while True:
            print("\n=== SISTEM PEMBAYARAN SYARIAH SANTRI ===")
            print("1. Lakukan Pembayaran")
            print("2. Tampilkan Daftar Santri")
            print("3. Tampilkan Riwayat Transaksi")
            print("4. Tampilkan Dashboard")
            print("5. Tambah Santri Baru")
            print("0. Keluar")
            pilihan = input("Pilihan: ")

            if pilihan == "1":
                self.lakukan_pembayaran()
            elif pilihan == "2":
                self.tampilkan_daftar_santri()
            elif pilihan == "3":
                self.tampilkan_riwayat_transaksi()
            elif pilihan == "4":
                self.tampilkan_dashboard()
            elif pilihan == "5":
                nama = input("Masukkan nama santri: ")
                kelas = input("Masukkan kelas santri: ")
                self.tambah_santri(nama, kelas)
                print("Santri berhasil ditambahkan!")
            elif pilihan == "0":
                print("Terima kasih telah menggunakan Sistem Pembayaran Syariah Santri.")
                break
            else:
                print("Pilihan tidak valid!")

            input("\nTekan Enter untuk melanjutkan...")

# Jalankan program utama
if __name__ == "__main__":
    sistem = SistemPembayaranSyariah()
    sistem.jalankan()
