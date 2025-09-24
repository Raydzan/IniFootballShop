## 1. Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya

jawaban: AuthenticationForm adalah form bawaan Django yang digunakan untuk proses login. Form ini tersedia di modul django.contrib.auth.forms dan biasanya dipakai bersama dengan LoginView untuk mengautentikasi pengguna berdasarkan username dan password.

kelebihanya: 1. bawaan django
2. terintegrasi dengan sistem auth django.
3. validasi keamanan sudah ada.
4. mudah dikustomisasi.

kekuranganya: 1. Terbatas hanya username dan password
2. tampilan standar.
3. kurang fleksibel untuk kebutuhan kompleks.
4. tidak ada fitur bawaan tambahan.


## 2. Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?

jawaban: autentikasi adalah proses untuk memverifikasi identitas pengguna, yaitu memastikan apakah seseorang benar-benar siapa yang ia klaim. Misalnya, saat seorang user memasukkan username dan password, sistem akan mencocokkannya dengan data yang tersimpan di database. Jika cocok, berarti identitasnya sah. Sementara itu, otorisasi adalah proses menentukan hak akses pengguna setelah identitasnya diverifikasi. Jadi setelah berhasil login, sistem akan mengecek apa saja yang boleh atau tidak boleh dilakukan oleh pengguna tersebut.

implementasinya:
1. Autentikasi di Django
Django menyediakan Authentication System melalui django.contrib.auth.
2. Otorisasi di Django
Django mengatur izin melalui:
* Permissions (izin per aksi) misalnya add_user, change_user, delete_post.
* Groups: sekumpulan permission yang bisa diberikan ke banyak user.
* Decorators / Mixins untuk proteksi.

## 3. Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?

jawaban: 
kelebihan cookies:
1. Sederhana dan langsung dibrowser. 
2. Persisten.
3. Dapat diakses antar request.

kekurangan cookies:
1. Rentan manipulasi.
2. Ukuran terbatas.
3. Membebani bandwidth.

kelebihan session:
1. Lebih aman.
2. Bisa menyimpan data lebih besar.
3. Kontrol penuh diserver.

kekurangan session:
1. Membebani server.
2. Butuh mekanisme tracking.
3. Bisa hilang saat server restart.

## 4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?

jawaban: tidak sepenuhnya aman secara default karena masih ada sejumlah risiko yang harus diwaspadai. Misalnya, jika aplikasi tidak menggunakan HTTPS, cookies bisa disadap (sniffing) oleh pihak ketiga melalui serangan man-in-the-middle. Selain itu, data dalam cookie juga bisa dimanipulasi karena tersimpan di sisi klien, apalagi jika tidak dienkripsi. Cookies juga rentan dicuri lewat serangan Cross-Site Scripting (XSS) jika kode aplikasi tidak aman, serta dapat dimanfaatkan dalam serangan CSRF karena browser akan selalu mengirimkan cookies secara otomatis ke server. Django menyediakan beberapa lapisan perlindungan bawaan:
1. SESSION_COOKIE_HTTPONLY = True
2. SESSION_COOKIE_SECURE = True
3. django.contrib.sessions

## 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

jawaban: 1. membuat kerangka template global (harusnya di tugas 2)
2. membuat form login dan logout
3. menambahkan sistem cookie
4. menambahkan sistem last login 
5. mencoba membuat dummy account
6. dan terakhir menghubungkan antara product ke user