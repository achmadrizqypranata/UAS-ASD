import datetime
import getpass
from prettytable import PrettyTable

class Akun:
    def __init__(self, username, pin, e_money, usia, gender):
        self.username = username
        self.pin = pin
        self.e_money = e_money
        self.usia = usia
        self.gender = gender
        self.cart = []
        self.transaction_count = 0
        self.last_transaction_date = datetime.date.today()

class Admin(Akun):
    def __init__(self, username, pin):
        super().__init__(username, pin, 0, 0, "admin")

class Pembeli(Akun):
    def __init__(self, username, pin, e_money, usia, gender):
        super().__init__(username, pin, e_money, usia, gender)

class Barang:
    def __init__(self, nama, jumlah, harga, kategori):
        self.nama = nama
        self.jumlah = jumlah
        self.harga = harga
        self.kategori = kategori

def jam_kerja():
    sekarang = datetime.datetime.now()
    return sekarang.hour >= 8 and sekarang.hour < 16

def total_harga(items):
    return sum(item.harga * item.jumlah for item in items)

def diskon(total_harga):
    if total_harga >= 350000:
        return total_harga * 0.75
    elif total_harga >= 100000:
        return total_harga * 0.85
    return total_harga

def sapaan(usia, gender):
    if usia < 13:
        return "Dek"
    elif usia >= 30:
        if gender == "L":
            return "Pak"
        elif gender == "P":
            return "Bu"
    else:
        return "Kak"

def print_header(title, additional_lines=None):
    print("=" * 50)
    print("{:^50}".format(title))
    if additional_lines:
        for line in additional_lines:
            print("{:^50}".format(line))
    print("=" * 50)

def menu_admin(items):
    while True:
        print_header("Menu Admin")
        print("1. Tambah Barang\n2. Lihat Barang\n3. Update Barang\n4. Hapus Barang\n5. Keluar")
        pilihan = input("Pilih opsi: ")

        if pilihan == '1':
            nama = input("Nama Barang: ")
            jumlah = int(input("Jumlah: "))
            harga = int(input("Harga: "))
            kategori = pilih_kategori()
            items.append(Barang(nama, jumlah, harga, kategori))
            print("Barang berhasil ditambahkan.")

        elif pilihan == '2':
            print_header("Daftar Barang")
            for index, item in enumerate(items):
                print(f"{index + 1}. {item.nama} - {item.jumlah} pcs - Rp{item.harga} - {item.kategori}")

        elif pilihan == '3':
            print("\nDaftar Barang:")
            for index, item in enumerate(items):
                print(f"{index + 1}. {item.nama} - {item.jumlah} pcs - Rp{item.harga} - {item.kategori}")
            id_barang = int(input("Pilih ID Barang yang ingin diupdate: ")) - 1
            if 0 <= id_barang < len(items):
                print("\n--- Update Barang ---")
                print("1. Update Jumlah")
                print("2. Update Harga")
                print("3. Update Kategori")
                opsi_update = input("Pilih opsi: ")

                if opsi_update == '1':
                    jumlah_baru = int(input("Jumlah baru: "))
                    items[id_barang].jumlah = jumlah_baru
                    print("Jumlah barang berhasil diupdate.")
                elif opsi_update == '2':
                    harga_baru = int(input("Harga baru: "))
                    items[id_barang].harga = harga_baru
                    print("Harga barang berhasil diupdate.")
                elif opsi_update == '3':
                    kategori_baru = pilih_kategori()
                    items[id_barang].kategori = kategori_baru
                    print("Kategori barang berhasil diupdate.")
                else:
                    print("Opsi tidak valid.")
            else:
                print("ID Barang tidak valid.")
        elif pilihan == '4':
            print("\nDaftar Barang:")
            for index, item in enumerate(items):
                print(f"{index + 1}. {item.nama} - {item.jumlah} pcs - Rp{item.harga} - {item.kategori}")
            id_barang = int(input("Pilih ID Barang yang ingin dihapus: ")) - 1
            if 0 <= id_barang < len(items):
                items.pop(id_barang)
                print("Barang berhasil dihapus.")
            else:
                print("ID Barang tidak valid.")
        elif pilihan == '5':
            break
        else:
            print("Opsi tidak valid, silakan coba lagi.")

def pilih_kategori():
    print("Kategori:")
    print("1. Game Fisik")
    print("2. Game Digital")
    print("3. DLC")
    kategori_pilihan = input("Pilih kategori (1/2/3): ")
    if kategori_pilihan == '1':
        return "Game Fisik"
    elif kategori_pilihan == '2':
        return "Game Digital"
    elif kategori_pilihan == '3':
        return "DLC"
    else:
        print("Kategori tidak valid.")
        return pilih_kategori()

def menu_pembeli(pembeli, items):
    while True:
        hari_ini = datetime.date.today()
        if pembeli.last_transaction_date != hari_ini:
            pembeli.transaction_count = 0
            pembeli.last_transaction_date = hari_ini

        sapaan_usia = sapaan(pembeli.usia, pembeli.gender)

        additional_info = [
            f"Saldo e-money Anda: Rp{pembeli.e_money}",
            f"Transaksi hari ini: {pembeli.transaction_count}/3",
            "",
            "--- Menu Pembeli ---",
            "1. Top Up e-Money",
            "2. Beli Barang",
            "3. Cek Isi Keranjang",
            "4. Checkout",
            "5. Logout",
            "",
            "Selamat Datang di Raisky Game Shop, Selamat berkhilaf >w<!"
        ]
        print_header(f"Halo {sapaan_usia} {pembeli.username}", additional_info)

        pilihan = input("Pilih opsi: ")
        if pilihan == '1':
            jumlah = int(input("Masukkan jumlah top up: "))
            pembeli.e_money += jumlah
            print(f"Top up berhasil. Saldo e-money sekarang: Rp{pembeli.e_money}")
        elif pilihan == '2':
            print_header("Daftar Barang yang Tersedia")
            for index, item in enumerate(items):
                print(f"{index + 1}. {item.nama} - {item.jumlah} pcs - Rp{item.harga} - {item.kategori}")
            nomor_barang = int(input("Pilih nomor barang yang ingin dibeli: ")) - 1
            if 0 <= nomor_barang < len(items):
                jumlah = int(input("Masukkan jumlah yang ingin dibeli: "))
                if items[nomor_barang].jumlah >= jumlah:
                    barang_terpilih = Barang(items[nomor_barang].nama, jumlah, items[nomor_barang].harga, items[nomor_barang].kategori)
                    pembeli.cart.append(barang_terpilih)
                    items[nomor_barang].jumlah -= jumlah
                    print("\nBarang berhasil ditambahkan ke keranjang.")
                else:
                    print("Jumlah barang tidak mencukupi.")
            else:
                print("Nomor barang tidak valid.")
        elif pilihan == '3':
            print_header("Isi Keranjang")
            if not pembeli.cart:
                print("Keranjang kamu kosong.")
            else:
                for item in pembeli.cart:
                    print(f"{item.nama} - {item.jumlah} pcs - Rp{item.harga} - {item.kategori}")
        elif pilihan == '4':
            if pembeli.transaction_count >= 3:
                print("Anda telah mencapai batas transaksi harian. Datang lagi besok :3")
                continue

            if not pembeli.cart:
                print("Keranjang kosong, tidak bisa checkout.")
                continue

            total_biaya = total_harga(pembeli.cart)
            diskon_diterima = diskon(total_biaya)
            if total_biaya != diskon_diterima:
                print(f"Selamat! Anda mendapatkan diskon: Rp{total_biaya - diskon_diterima}")
            total_biaya = diskon_diterima

            print(f"Total biaya setelah diskon: Rp{total_biaya}")
            if pembeli.e_money < total_biaya:
                print("Saldo e-money tidak cukup.")
                top_up_choice = input("Apakah Anda ingin top up? (ya/tidak): ").lower()
                if top_up_choice == 'ya':
                    jumlah_top_up = int(input("Masukkan jumlah top up: "))
                    pembeli.e_money += jumlah_top_up
                    print(f"Top up berhasil. Saldo e-money sekarang: Rp{pembeli.e_money}")
                    continue
                else:
                    print("Transaksi tidak dilanjutkan karena saldo tidak mencukupi.")
                    continue

            pembeli.e_money -= total_biaya
            pembeli.transaction_count += 1
            pembeli.last_transaction_date = datetime.date.today()

            nota_pembelian = PrettyTable()
            nota_pembelian.field_names = ["Nama Barang", "Jumlah", "Harga per Item", "Total Harga"]
            for item in pembeli.cart:
                nota_pembelian.add_row([item.nama, item.jumlah, f"Rp{item.harga}", f"Rp{item.harga * item.jumlah}"])
            nota_pembelian.add_row(["", "", "Total Bayar", f"Rp{total_biaya}"])

            print("\n--- Nota Pembelian ---")
            print(nota_pembelian)

            pembeli.cart.clear()
            print(f"Pembelian berhasil. Sisa e-money: Rp{pembeli.e_money}")

            transaksi_lagi = input("Apakah Anda ingin melakukan transaksi lain? (ya/tidak): ").lower()
            if transaksi_lagi != "ya":
                print("Terima kasih telah berbelanja, sampai jumpa lagi XD")
                break
        elif pilihan == '5':
            break
        else:
            print("Opsi tidak valid, silakan coba lagi.")

def daftar(buyers):
    username = input("Masukkan username: ")
    pin = getpass.getpass("Masukkan PIN: ")
    e_money = int(input("Masukkan saldo e-money awal: "))
    usia = int(input("Masukkan usia: "))
    gender = input("Masukkan gender (L/P): ")
    buyers.append(Pembeli(username, pin, e_money, usia, gender))
    print("Registrasi berhasil, silakan login.")

def main():
    admin = Admin("rizqy", "123789")
    pembeli = [
        Pembeli("Akmal", "1234", 2000000, 20, "L"),
        Pembeli("Agus", "5678", 1000000, 25, "L"),
        Pembeli("Sarah", "9876", 1500000, 22, "P"),
        Pembeli("Cindy", "6789", 2500000, 19, "P")
    ]

    items = [
        Barang("The Legend of Zelda: Breath of the Wild - Physical", 10, 650000, "Game Fisik"),
        Barang("Animal Crossing: New Horizons - Digital", 15, 550000, "Game Digital"),
        Barang("Cyberpunk 2077 - Physical", 12, 750000, "Game Fisik"),
        Barang("Elden Ring - Digital", 8, 800000, "Game Digital"),
        Barang("Minecraft Java Edition - Digital", 20, 350000, "Game Digital"),
        Barang("Super Mario Odyssey - DLC", 30, 200000, "DLC"),
        Barang("Red Dead Redemption 2 - Physical", 6, 850000, "Game Fisik"),
        Barang("Assassin's Creed Valhalla - Digital", 10, 700000, "Game Digital"),
        Barang("GTA V Premium Edition - Physical", 14, 600000, "Game Fisik"),
        Barang("Fortnite - V-Bucks Pack", 50, 150000, "Game Digital"),
        Barang("Halo Infinite - Season Pass", 25, 300000, "DLC"),
        Barang("The Witcher 3: Wild Hunt Expansion Pass - DLC", 15, 250000, "DLC"),
        Barang("FIFA 22 - Ultimate Edition - Digital", 18, 850000, "Game Digital"),
        Barang("Monster Hunter World: Iceborne - DLC", 20, 400000, "DLC"),
        Barang("Dark Souls III - The Fire Fades Edition - Physical", 7, 700000, "Game Fisik"),
        Barang("Call of Duty: Modern Warfare - Digital", 30, 800000, "Game Digital"),
        Barang("Sekiro: Shadows Die Twice - Physical", 9, 750000, "Game Fisik"),
        Barang("Fallout 4: Game of the Year Edition - Physical", 10, 600000, "Game Fisik"),
        Barang("Destiny 2: Beyond Light - DLC", 12, 350000, "DLC"),
        Barang("NBA 2K22 - Digital", 20, 700000, "Game Digital"),
        Barang("The Sims 4 - Eco Lifestyle - DLC", 15, 300000, "DLC"),
        Barang("Battlefield 2042 - Digital", 13, 780000, "Game Digital"),
        Barang("Ghost of Tsushima - Director's Cut - Physical", 8, 900000, "Game Fisik"),
        Barang("Death Stranding - Digital", 11, 650000, "Game Digital"),
        Barang("Horizon Zero Dawn - Complete Edition - Physical", 10, 500000, "Game Fisik")
    ]

    if jam_kerja():
        print_header("Menu Dashboard Raisky Game Shop")
        
        while True:
            print("\n1. Login sebagai Admin")
            print("2. Login sebagai Pembeli")
            print("3. Keluar")
            pilihan = input("Pilih opsi: ")

            if pilihan == '1':
                username = input("Username: ")
                pin = getpass.getpass("PIN: ")

                if username == admin.username and pin == admin.pin:
                    print("Login berhasil sebagai admin.")
                    menu_admin(items)
                else:
                    print("Username atau PIN salah.")
            elif pilihan == '2':
                print("\n1. Login")
                print("2. Registrasi")
                pilihan = input("Pilih opsi: ")

                if pilihan == '1':
                    username = input("Username: ")
                    pin = getpass.getpass("PIN: ")

                    pembeli_ini = next((b for b in pembeli if b.username == username and b.pin == pin), None)
                    if pembeli_ini:
                        print("Login berhasil sebagai pembeli.")
                        menu_pembeli(pembeli_ini, items)
                    else:
                        print("Username atau PIN salah.")
                elif pilihan == '2':
                    daftar(pembeli)
                else:
                    print("Opsi tidak valid.")
            elif pilihan == '3':
                print("Terima kasih telah mengunjungi shop kami ^^")
                break
            else:
                print("Opsi tidak valid, silakan coba lagi.")
    else:
        print("Maaf, toko kami hanya buka pada jam kerja (08.00 - 16.00).")

if __name__ == "__main__":
    main()
