# Dokumentasi Program

Nama: Muhammad Dian Nurdiansyah


Nim:  2209116022

# Cara Kerja Program
1. Program yang saya buat ini adalah sebuah sistem antrian pengiriman barang yang menggunakan konsep linked list. Program ini terdiri dari dua kelas yaitu class Barang dan kelas Antrian. Kelas Barang memiliki properti nama, pengirim, penerima, berat, dan tujuan. Sedangkan kelas Antrian memiliki properti head untuk merepresentasikan elemen pertama pada antrian.

2. Ketika program dijalankan, akan muncul sebuah menu dengan lima pilihan. Pilihan pertama adalah untuk menambah barang pada antrian, pilihan kedua adalah untuk menghapus barang dari antrian, pilihan ketiga adalah untuk melihat seluruh antrian, pilihan keempat adalah untuk merubah data barang yang ada di dalam antrian, dan pilihan kelima adalah untuk keluar dari program.

3. Ketika user memilih opsi tambah barang, program akan meminta user untuk menginput data barang seperti nama barang, pengirim, penerima, berat, dan tujuan. Data barang tersebut akan disimpan dalam bentuk objek dan ditambahkan ke dalam antrian menggunakan metode tambah_barang.

4. Ketika user memilih opsi hapus barang, program akan meminta user untuk menginput nama barang yang ingin dihapus dari antrian. Program akan mencari elemen dalam antrian dengan nama barang yang sama dan menghapusnya menggunakan metode hapus_barang.

5. Ketika user memilih opsi lihat antrian, program akan menampilkan seluruh elemen dalam antrian beserta dengan data yang dimilikinya menggunakan metode lihat_antrian.

6. Ketika user memilih opsi rubah data di dalam antrian, program akan meminta user untuk menginput nama barang yang akan dirubah. Program akan mencari elemen dalam antrian dengan nama barang yang sama dan meminta user untuk menginput data baru untuk barang tersebut menggunakan metode rubah_barang. Program akan terus berjalan sampai user memilih opsi keluar dari program.

# Fungsionalitas Program
Program ini adalah aplikasi sederhana untuk mengelola antrian pengiriman barang. Program ini menggunakan OOP (Object Oriented Programming) dengan dua buah class yaitu Barang dan Antrian. Class Barang digunakan untuk membuat objek barang dengan properti nama, pengirim, penerima, berat, dan tujuan.

Class Antrian digunakan untuk mengelola antrian pengiriman barang. Class ini memiliki beberapa method, yaitu:
tambah_barang: untuk menambahkan barang ke antrian.
hapus_barang: untuk menghapus barang dari antrian berdasarkan nama barang.
lihat_antrian: untuk melihat daftar barang dalam antrian.
rubah_barang: untuk mengubah data barang dalam antrian.
Fungsi main() adalah fungsi utama dari program. Fungsi ini membuat objek dari kelas Antrian dan memulai perulangan program yang menampilkan menu pilihan. Kemudian program akan meminta input dari user sesuai dengan pilihan yang dipilih. Setiap input akan memanggil salah satu method yang ada pada kelas Antrian untuk menambahkan, menghapus, melihat, atau mengubah data barang dalam antrian.

Program ini juga menggunakan modul os dan time. Modul os digunakan untuk membersihkan layar setiap kali user memilih menu tertentu. Sedangkan modul time digunakan untuk memberikan jeda sebelum program membersihkan layar.
