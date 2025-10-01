## 1.  Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!

jawaban: dari yang paling kuat ke paling lemah:
1. !important : akan selalu diprioritaskan di atas aturan biasa, meskipun specificity-nya lebih rendah.
2. Inline style : CSS langsung di atribut elemen
3. ID selector : Spesifik sekali, karena hanya untuk satu elemen.
4. Class selector, attribute selector, pseudo-class
5. Element/tag selector & pseudo-element
dengan catatan jika ada yang sama, maka aturan yang ditulis paling akhir difile CSS akan digunakan

## 2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design, serta jelaskan mengapa!

jawaban: Responsive design penting karena pengguna mengakses web dari berbagai perangkat dengan ukuran layar berbeda. Tanpa desain responsif, tampilan bisa berantakan dan menyulitkan navigasi, sehingga mengurangi kenyamanan pengguna. Contohnya, Tokopedia dan YouTube sudah menerapkan responsive design sehingga tampilannya menyesuaikan di ponsel maupun desktop, sementara banyak website pemerintah lama belum responsif sehingga sulit digunakan di perangkat mobile.

## 3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!

jawaban: 
1. Margin adalah ruang di luar border, berfungsi memberi jarak antara elemen dengan elemen lain di sekitarnya.

2. Border adalah garis yang mengelilingi elemen, berada di antara margin dan padding. Border bisa diberi warna, ketebalan, dan style tertentu.

3. Padding adalah ruang di dalam border, yaitu jarak antara konten elemen (teks, gambar, dll.) dengan batas border.

contoh implementasi:
.box {
  margin: 20px;
  border: 2px solid black;
  padding: 15px;
}

## 4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!

jawaban: 
1. Flexbox (Flexible Box Layout)

Konsep: Flexbox digunakan untuk mengatur elemen di satu dimensi saja, baik baris (row) atau kolom (column). Elemen di dalam flex container bisa otomatis menyesuaikan ukuran ruang kosong agar tetap rapi.
Kegunaan: Cocok untuk menyusun elemen yang berurutan, seperti navbar, daftar produk horizontal, tombol, atau form.

2. Grid Layout

Konsep: CSS Grid berfokus pada dua dimensi (baris dan kolom sekaligus). Dengan grid, kita bisa membuat layout kompleks seperti tabel modern, tapi jauh lebih fleksibel.
Kegunaan: Cocok untuk layout halaman secara keseluruhan, misalnya membagi area menjadi header, sidebar, konten utama, dan footer.

## 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

jawaban: 
1. Aktifkan app & humanize di settings.py INSTALLED_APPS (main, django.contrib.humanize).
2. menggunakan tempat css yang dapat dijangkau lalu pada setiap yang menggunakan resource pakaikan
<!-- {% load static %} -->
3. Menambahkan models stock
4. Menambahkan field stock
5. View login/register/logout pakai auth bawaan Django. Setelah login, simpan last_login di cookie agar bisa ditampilkan
6. Beri @login_required pada halaman private
7. Di update_product & delete_product, cek kepemilikan
8. Buat main/context_processors.py untuk mengambil langsung dari category
9. Perubahan besar pada show_main untuk filter yours dan all
10. Membuat design awal dengan teknik crazy eight di kertas
11. Navbar kiri: burger + brand.
Navbar kanan: identitas pembuat dari context processor + link Logout (merah).
Drawer kiri: loop product_categories
12. Panel atas menampilkan user yang login + last_login + tombol Tambah Produk.
13. Header “Daftar produk” + bar filter:
14. Products box (panel putih) membungkus grid; empty state berada di LUAR grid supaya bisa full-width & center
