https://moch.raydzan-inifootballshop.pbp.cs.ui.ac.id

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

jawaban : Saat mengerjakan saya juga sambil memahami dan tidak hanya sekedar mengikuti tutorial

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

jawaban: 

browser -> urls.py -> views.py -> models.py -> templates html -> response

pada browser ada http request lalu pada urls mencocokan pola url dan meneruskan ke view
lalu pada view melanjutkan ke modelspy dengan eksekusi query ke DB
setelah itu render context pada template dan hasilnya response html kembali ke browser

3. Jelaskan peran settings.py dalam proyek Django!

jawavab : settings.py adalah pusat konfigurasi proyek

4. Bagaimana cara kerja migrasi database di Django?

jawaban : python manage.py makemigrations untuk membaca perubahan yang terjadi dan lalu
python manage.py migrate untuk migrating

5. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?

jawaban : testing dan migrasi yang terintgrasi untuk mahasiswa


6. Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?

jawaban :  aman sih gak ada