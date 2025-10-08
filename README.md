## 1. Apa perbedaan antara synchronous request dan asynchronous request?

jawaban: sinkronus dilakukan secara nerurutan dan menunggu giliran. jadi jalanya satu per satu, saat browser mengirim request ke server, browser akan menunggu responsnya dulu sebelum bisa melakukan hal lain. selama menunggu, halaman web akan berhenti sampai respons diterima. 

sedangkan asinkronus berarti tidak harus menunggu, bisa berjalan bersamaan dengan hal lain. jadi browser tidak menunggu server sampai selesai memproses. aplikasi bisa tetap berjalan atau menampilkan hal lain sementara menunggu respons.

## 2. Bagaimana AJAX bekerja di Django (alur request–response)?

jawaban: user klik -> JS kirim fetch dengan bawa data serta CSRF -> urls.py (view django) -> view: validasi, logic, database (jika berhasil kembalikan JSON, jika gagal kembalikan error JSON) -> JS terima respons (parse JSON, update DOM)

## 3. Apa keuntungan menggunakan AJAX dibandingkan render biasa di Django?

jawaban: ajax di django memungkinkan pertukaran data antara browser dan server tanpa memuat ulang seluruh halaman. hal ini membuat proses lebih cepat, efisien, dan interaktif dibandingkan render biasa yang selalu ngereload halaman penuh.

## 4. Bagaimana cara memastikan keamanan saat menggunakan AJAX untuk fitur Login dan Register di Django?

jawaban: untuk menjaga keamanan login dan register dengan ajax di django, pastikan aplikasi menggunakan https dan mengaktifkan pengaturan aman seperti CSRF_COOKIE_SECURE dan SESSION_COOKIE_HTTPONLY. sertakan csrf token di setiap request, lakukan validasi input di server, serta gunakan pesan error umum agar tidak bocor informasi pengguna. batasi percobaan login dengan rate limiting, rotasi sesi setelah login, dan batasi akses cors hanya untuk domain resmi

## 5.  Bagaimana AJAX mempengaruhi pengalaman pengguna (User Experience) pada website?

jawaban: ajax membuat pengalaman pengguna (user experience) di website menjadi jauh lebih cepat, halus, dan interaktif. dengan ajax, halaman tidak perlu dimuat ulang sepenuhnya setiap kali pengguna berinteraksi. cukup bagian tertentu yang diperbarui. hal ini membuat transisi antar aksi terasa instan, mengurangi waktu tunggu, dan menjaga posisi pengguna di halaman.
