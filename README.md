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
- Baris kode tersebut adalah untuk mendefinisikan kelas Barang, yang memiliki properti nama, pengirim, penerima, berat, tujuan, dan next. Properti next ini berguna untuk menghubungkan objek Barang pada Antrian. Dalam class ini terdapat sebuah constructor (init) yang akan dipanggil ketika objek dari class Barang dibuat.

- Pada constructor, terdapat beberapa parameter yaitu nama, pengirim, penerima, berat, dan tujuan yang akan digunakan untuk menginisialisasi properti-properti objek Barang. Properti-properti tersebut adalah nama, pengirim, penerima, berat, tujuan, dan next.

- Properti "nama" merepresentasikan nama dari barang yang akan dikirim. Properti "pengirim" merepresentasikan nama dari pengirim barang. Properti "penerima" merepresentasikan nama dari penerima barang. Properti "berat" merepresentasikan berat barang dalam satuan kilogram. Properti "tujuan" merepresentasikan alamat tujuan pengiriman barang. Properti "next" akan digunakan untuk menyimpan alamat dari objek Barang berikutnya (jika ada) pada linked list.

![class antrian](https://user-images.githubusercontent.com/94899238/225825280-9e642e7b-b9e7-4c05-b439-1d932fec612e.png)
- Baris kode tersebut adalah untuk mendefinisikan kelas Antrian, yang memiliki properti head. Properti head ini menunjukkan elemen pertama dari antrian. Fungsi tambah_barang() digunakan untuk menambahkan objek Barang ke dalam Antrian. Jika Antrian masih kosong (head == None), maka objek Barang akan menjadi head. Jika tidak, objek Barang akan ditambahkan sebagai elemen terakhir dari Antrian. Metode ini memastikan bahwa setiap objek Barang yang ditambahkan ke antrian diposisikan di akhir dari antrian, sehingga ketika sebuah objek barang dihapus dari antrian, maka objek berikutnya akan menjadi elemen paling depan dari antrian.

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

# Output yang Dihasilkan

![Screenshot 2023-03-17 142837](https://user-images.githubusercontent.com/94899238/225835641-fbd58e4c-37bd-40ff-b5c1-e6773b367867.png)
- Gambar diatas merupakan tampilan awal dari program ini, berisikan pilihan-pilihan untuk menambah data barang antrian, menghapus data barang di antrian, melihat antrian, bahkan merubah data yang telah ada di antrian.

![Screenshot 2023-03-17 143744](https://user-images.githubusercontent.com/94899238/225836794-d51ec004-b17b-4a0c-8348-af3ad8349984.png)
- Jika pengguna (admin) menginput 1 atau pilihan pertama, maka program akan mengarahkan pengguna ke menu tambah data barang. Disini pengguna diminta untuk menginput data-data seputar barang tersebut, seperti Nama barang, nama pengirim, nama penerima, berat barang, serta tujuan pengiriman.

![Screenshot 2023-03-17 144001](https://user-images.githubusercontent.com/94899238/225838027-d9158cc6-0a3b-410a-a76e-2ae6de24a0a8.png)
- Jika pengguna (admin) menginput pilihan kedua, maka program akan mengarahkan ke menu menghapus data barang di antrian. Disini program menampilkan data barang yang sudah ada di antrian agar memudahkan admin memilih data mana yang perlu dihapus, untuk menghapus suatu data barang pengguna cukup menginput nama dari data yang sudah ada secara baik dan benar.

![Screenshot 2023-03-17 144026](https://user-images.githubusercontent.com/94899238/225839039-90209a4b-8fe0-468f-8303-401e87d03fe2.png)
- Jika pengguna (admin) menginput pilihan ketiga, maka program akan menampilkan data yang sudah ada di antrian.

![Screenshot 2023-03-17 145752](https://user-images.githubusercontent.com/94899238/225846501-c9199dd9-3e3a-4390-bd30-f3935a2a7b61.png)
![Screenshot 2023-03-17 145808](https://user-images.githubusercontent.com/94899238/225846908-e655be14-f4f1-456a-84ba-efc9bc7363f2.png)
- Jika pengguna (admin) menginput pilihan ketiga, maka program akan mengarahkan penggunna menuju menu merubah data yang sudah ada di dalam antrian. Disini program kembali menampilkan list antrian yang telah tersedia di antrian, setelah itu program meminta pengguna menginput nama dari data yang telah ada dan yang diinginkan untuk dirubah datanya secara baik dan benar agar program dapat berjalan dengan benar.
