import os
import time
os.system("cls")

# Mendefinisikan class Barang
class Barang:
    def __init__(self, nama, pengirim, penerima, berat, tujuan):
        # Inisialisasi objek Barang dengan properti nama, pengirim, penerima, berat, dan tujuan
        self.nama = nama
        self.pengirim = pengirim
        self.penerima = penerima
        self.berat = berat
        self.tujuan = tujuan
        self.next = None

# Mendifinisikan class Antrian
class Antrian:
    def __init__(self):
        # Inisialisasi objek Antrian dengan properti head (pertama kali head bernilai None)
        self.head = None

    def tambah_barang(self, nama, pengirim, penerima, berat, tujuan):
        # Membuat objek baru dengan properti nama, pengirim, penerima, berat, dan tujuan
        barang_baru = Barang(nama, pengirim, penerima, berat, tujuan)

        if self.head is None:
            # Jika head kosong, maka objek barang_baru menjadi head
            self.head = barang_baru
        else:
            # Jika head tidak kosong, maka cari elemen terakhir dan tambahkan barang_baru sebagai elemen berikutnya
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = barang_baru

    def hapus_barang(self, nama):
        if self.head is None:
            # Jika head kosong, tampilkan pesan antrian kosong
            print()
            print("~ Antrian kosong ~".center(50))
            #print("====================================================\n")
            return

        if self.head.nama == nama:
            # Jika nama barang di head sesuai dengan nama yang dicari, maka head diganti dengan elemen berikutnya
            self.head = self.head.next
            return

        curr = self.head
        while curr.next is not None:
            if curr.next.nama == nama:
                # Jika nama barang pada elemen berikutnya sesuai dengan nama yang dicari, maka elemen berikutnya dihapus
                curr.next = curr.next.next
                return
            curr = curr.next
        # Jika nama barang tidak ditemukan, tampilkan pesan barang tidak ditemukan
        print("Barang tidak ditemukan\n")

    def lihat_antrian(self):
        if self.head is None:
            # Jika head kosong, tampilkan pesan antrian kosong
            print()
            print("~ Antrian kosong ~".center(50))
            print("====================================================\n")
            return

        # Jika tidak kosong, iterasi dari head ke tail dan tampilkan detail setiap node
        curr = self.head
        while curr is not None:
            print("Nama Barang : ", curr.nama)
            print("Pengirim    : ", curr.pengirim)
            print("Penerima    : ", curr.penerima)
            print("Berat       : ", curr.berat)
            print("Tujuan      :",  curr.tujuan)
            print("====================================================\n")
            curr = curr.next

    def rubah_barang(self, nama):
            if self.head is None:
                print()
                print("~ Antrian kosong ~".center(50))
                print("====================================================\n")
                return

            curr = self.head
            while curr is not None:
                # Jika nama barang ditemukan, tampilkan pesan untuk mengubah data
                if curr.nama == nama:
                    print("Data barang ditemukan, silahkan rubah data berikut:")
                    curr.nama = input("Nama barang : ")
                    curr.pengirim = input("Pengirim : ")
                    curr.penerima = input("Penerima : ")
                    curr.berat = input("Berat (Kg) : ")
                    curr.tujuan = input("Tujuan (Alamat Penerima) : ")
                    print("Perintah Berhasil!")
                    return
                curr = curr.next
                # Jika nama barang tidak ditemukan, tampilkan pesan kesalahan
                print("Barang tidak ditemukan\n")
                main()

# Fungsi utama program
def main():
    # Membuat objek dari kelas Antrian
    antrian = Antrian()

    # Perulangan program
    while True:
        # Tampilkan menu
        print("======= Jasa Pengiriman Barang Bintang Prima =======\n")
        print("1. Tambah Barang")
        print("2. Hapus Barang")
        print("3. Lihat Antrian")
        print("4. Merubah Data di Dalam Antrian")
        print("5. Keluar")
        print("\n====================================================\n")

        # Input pilihan menu dari user
        pilihan = input("Pilih menu : ")
        print("\n====================================================\n")

        # Cek pilihan menu
        if pilihan == '1':
            time.sleep(2)
            os.system ("Cls")
            print()
            print("\t\t~ Menu Tambah Barang ~\n")
            print("Note: ~ Berat barang pengiriman minimal 1Kg! ~")
            print("====================================================\n")

            # Input data barang
            nama = input("Nama barang: ")
            pengirim = input("Nama Pengirim: ")
            penerima = input("Nama Penerima: ")
            berat = input("Berat (Kg): ")
            tujuan = input("Tujuan (Alamat Penerima): ")

            # Panggil metode tambah_barang dari objek antrian
            antrian.tambah_barang(nama, pengirim, penerima, berat, tujuan)
            print()
            print("Barang berhasil ditambahkan".center(50))
            print("====================================================\n")

        elif pilihan == '2':
            time.sleep(2)
            os.system("cls")
            print("\t\t~ Menu Hapus Barang di Antrian ~\n")

            # Tampilkan antrian
            print("List Barang yang Ada di Antrian: \n")
            antrian.lihat_antrian()
            print()

            # Input nama barang yang akan dihapus
            nama = input("Nama barang : ")

            # Panggil metode hapus_barang dari objek antrian
            antrian.hapus_barang(nama)
            print()
            print("~ Perintah Berhasil ~".center(50))
            print("====================================================\n")

        elif pilihan == '3':
            os.system("cls")
            print("====================================================")

            # Tampilkan antrian
            print("List Barang yang Ada di Antrian: \n")
            time.sleep(2)
            antrian.lihat_antrian()

        elif pilihan == '4':
            time.sleep(2)
            os.system ("cls")
            print("====================================================\n")
            print("  ~ Menu Merubah Data yang Ada di Dalam Antrian ~\n")

            # Tampilkan antrian
            antrian.lihat_antrian()
            print()

            # Input nama barang yang akan diubah
            nama = input("Nama barang : ")

            # Panggil metode rubah_barang dari objek antrian
            antrian.rubah_barang(nama)

            print("~ Perintah Berhasil ~".center(50))
            print("====================================================\n")

        elif pilihan == '5':
            time.sleep(2)
            os.system ("Cls")
            print("~ Keluar dari program berhasil ~\n".center(50))
            print("====================================================")

            # Keluar dari perulangan
            break

        else:
            os.system("cls")
            print("~ Menu tidak ditemukan ~\n")
            time.sleep(1)

# Jalankan program
if __name__ == '__main__':
    main()