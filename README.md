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
Program ini adalah aplikasi sederhana untuk mengelola antrian pengiriman barang. Program ini menggunakan OOP (Object Oriented Programming) dengan dua buah class yaitu Barang dan Antrian. **Class Barang** digunakan untuk membuat objek barang dengan properti nama, pengirim, penerima, berat, dan tujuan.

**Class Antrian** digunakan untuk mengelola antrian pengiriman barang. Class ini memiliki beberapa method, yaitu:

**tambah_barang**: untuk menambahkan barang ke antrian.

**hapus_barang**: untuk menghapus barang dari antrian berdasarkan nama barang.

**lihat_antrian**: untuk melihat daftar barang dalam antrian.

**rubah_barang**: untuk mengubah data barang dalam antrian.

**Fungsi main()** adalah fungsi utama dari program. Fungsi ini membuat objek dari kelas Antrian dan memulai perulangan program yang menampilkan menu pilihan. Kemudian program akan meminta input dari user sesuai dengan pilihan yang dipilih. Setiap input akan memanggil salah satu method yang ada pada kelas Antrian untuk menambahkan, menghapus, melihat, atau mengubah data barang dalam antrian.

Program ini juga menggunakan modul os dan time. Modul os digunakan untuk membersihkan layar setiap kali user memilih menu tertentu. Sedangkan modul time digunakan untuk memberikan jeda sebelum program membersihkan layar.

# Penjelasan Elemen-Elemen Penting dari Tiap Baris Program
![class barang](https://user-images.githubusercontent.com/94899238/225825022-28c2990a-ac35-4396-973e-ece42eff99d7.png)
- Baris kode tersebut adalah untuk mendefinisikan kelas Barang, yang memiliki properti nama, pengirim, penerima, berat, tujuan, dan next. Properti next ini berguna untuk menghubungkan objek Barang pada Antrian.

![class antrian](https://user-images.githubusercontent.com/94899238/225825280-9e642e7b-b9e7-4c05-b439-1d932fec612e.png)
- Baris kode tersebut adalah untuk mendefinisikan kelas Antrian, yang memiliki properti head. Properti head ini menunjukkan elemen pertama dari antrian. Fungsi tambah_barang() digunakan untuk menambahkan objek Barang ke dalam Antrian. Jika Antrian masih kosong (head == None), maka objek Barang akan menjadi head. Jika tidak, objek Barang akan ditambahkan sebagai elemen terakhir dari Antrian.

![hapus barang](https://user-images.githubusercontent.com/94899238/225825511-35cbd3a1-cb67-40d7-b3da-bb6ba5146452.png)
- Baris kode tersebut adalah untuk membuat fungsi hapus_barang(), yang digunakan untuk menghapus objek Barang dari Antrian berdasarkan nama. Jika Antrian masih kosong, maka akan ditampilkan pesan "Antrian kosong". Jika elemen pertama di Antrian memiliki nama yang sama dengan nama yang dihapus, maka elemen pertama akan dihapus. Jika tidak, maka Antrian akan diiterasi dari elemen kedua hingga elemen terakhir. Jika nama Barang ditemukan, maka Barang akan dihapus. Jika tidak, akan ditampilkan pesan "Barang tidak ditemukan".

![lihat antrian](https://user-images.githubusercontent.com/94899238/225825800-92d1b28b-ff49-4927-9cf2-b8589817e89c.png)
- Baris kode program di atas digunakan untuk menampilkan detail setiap node di dalam antrian. Fungsi lihat_antrian akan mengecek apakah head antrian kosong atau tidak. Jika head kosong, maka akan menampilkan pesan bahwa antrian kosong dan langsung keluar dari fungsi menggunakan pernyataan return.

Jika head tidak kosong, maka fungsi akan mengiterasi dari head ke tail dan menampilkan detail setiap node. Setiap detail node seperti nama barang, pengirim, penerima, berat, dan tujuan akan ditampilkan menggunakan pernyataan print. Setiap detail node juga akan dipisahkan dengan garis pemisah "===========================================".

![rubah barang](https://user-images.githubusercontent.com/94899238/225827345-e801ee9e-6f55-4bdd-998a-770133cc0f8b.png)
- Baris program ini berguna untuk mengubah data barang dalam sebuah antrian. Pertama, program akan memeriksa apakah antrian kosong atau tidak. Jika kosong, program akan menampilkan pesan bahwa antrian kosong dan program akan menghentikan eksekusi. Jika tidak kosong, program akan mencari nama barang yang ingin diubah dengan cara melakukan iterasi dari head sampai tail. Jika nama barang ditemukan, program akan menampilkan pesan untuk mengubah data dan program akan meminta inputan dari pengguna untuk mengubah nama barang, pengirim, penerima, berat, dan alamat tujuan. Setelah itu, program akan menampilkan pesan bahwa perintah berhasil dan menghentikan eksekusi. Namun, jika nama barang tidak ditemukan, program akan menampilkan pesan kesalahan dan memanggil fungsi main() untuk kembali ke menu utama.

![def main](https://user-images.githubusercontent.com/94899238/225827963-083c3921-970f-4090-9638-97c31a2926c4.png)
- Baris program di atas adalah fungsi utama program yang berisi perulangan while True yang berjalan terus menerus sampai program dihentikan. Selain itu, fungsi ini juga membuat objek dari kelas Antrian yang digunakan untuk menyimpan data barang yang diinputkan oleh pengguna. Pada baris selanjutnya, program menampilkan menu pilihan yang terdiri dari lima pilihan yaitu Tambah Barang, Hapus Barang, Lihat Antrian, Merubah Data di Dalam Antrian, dan Keluar. Setelah menampilkan pilihan menu, program akan meminta input pilihan dari pengguna.

![pilihan 1-5](https://user-images.githubusercontent.com/94899238/225828605-acbc7533-7d86-4c07-b2c2-e12a3485e033.png)
Program akan menampilkan menu dengan beberapa pilihan seperti tambah barang, hapus barang, lihat antrian, ubah data barang, dan keluar dari program dan semua pilihan ini telah terintegrasi daripada fungsi yang ada di class barang dan class antrian.

- Jika user memilih pilihan 1, program akan meminta input data barang seperti nama barang, pengirim, penerima, berat, dan tujuan. Data barang yang diinputkan akan disimpan dalam objek antrian menggunakan metode tambah_barang.

- Jika user memilih pilihan 2, program akan menampilkan antrian barang yang ada dan meminta input nama barang yang akan dihapus. Nama barang yang diinputkan akan dihapus dari objek antrian menggunakan metode hapus_barang.

- Jika user memilih pilihan 3, program akan menampilkan antrian barang yang ada menggunakan metode lihat_antrian.

- Jika user memilih pilihan 4, program akan menampilkan antrian barang yang ada dan meminta input nama barang yang akan diubah. Jika nama barang ditemukan pada objek antrian, program akan meminta input data baru untuk barang tersebut dan melakukan perubahan data menggunakan metode rubah_barang.

- Jika user memilih pilihan 5, program akan keluar dari perulangan dan program akan berhenti.

- Jika user memilih selain pilihan 1-5, program akan menampilkan pesan bahwa menu tidak ditemukan dan user akan diminta memilih kembali menu yang tersedia.

Program ini menggunakan beberapa library yaitu time dan os. Library time digunakan untuk menambahkan delay pada program agar tampilan menu tidak terlalu cepat, sedangkan library os digunakan untuk membersihkan layar setelah user memilih suatu pilihan menu.
