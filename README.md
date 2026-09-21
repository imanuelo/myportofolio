Name : Juan Imanuel

NPM : 2506619455

Class : PBP A

# Deskripsi Proyek
Proyek ini merupakan website portofolio pribadi yang dibuat menggunakan Django. Website ini menampilkan informasi seperti profil, pengalaman, proyek, dan pendidikan.


## Testing dan Run Project
Untuk memastikan websitenya berjalan dengan baik, gunakan:

python manage.py check, atau
python manage.py test main

Perintah diatas digunakan untuk mengecek apakah terdapat error pada proyek sebelum menjalankan server

Jika tidak ada error maka bisa langsung gunakan:

python manage.py runserver

Untuk menjalankan server



## Refleksi Tugas 2
1. Ketika pengguna membuka halaman Projects, browser akan mengirimkan permintaan ke website. Permintaan tersebut pertama kali diproses oleh urls.py yang ada di proyek portofolio. File ini berfungsi untuk mengatur URL utama pada proyek dan meneruskan permintaan ke aplikasi main. Setelah diteruskan ke aplikasi main, permintaan akan diperiksa oleh main/urls.py untuk menentukan halaman yang sesuai. Karena pengguna membuka halaman Projects, Django akan menjalankan view yang menangani halaman tersebut. View kemudian mengambil data Projects dari model yang terhubung dengan database. Data yang sudah didapatkan kemudian dikirim dari view ke template. Di dalam template, data tersebut ditampilkan menggunakan Django Template Language. Setelah template selesai diproses, Django menghasilkan halaman HTML dan mengirimkannya kembali ke browser sehingga pengguna dapat melihat daftar Projects. Jadi, secara sederhana alurnya adalah browser mengirim request, kemudian request diteruskan dari URL proyek ke URL aplikasi, lalu view mengambil data dari model dan mengirimkannya ke template untuk ditampilkan di browser.

2. Karena data akan lebih mudah untuk dikelola dan diubah. Jika data ditulis langsung di dalam template, setiap kali ingin menambahkan, mengubah, atau menghapus data, kita harus mengubah kode HTML secara manual. Dengan menggunakan model, data dapat dikelola melalui database tanpa perlu mengubah template. Contohnya, ketika ingin menambahkan project baru, kita cukup menambahkan data project tersebut ke database.

3. Makemigrations digunakan untuk membuat file migrasi berdasarkan perubahan yang dilakukan pada model. File migrasi tersebut berisi informasi mengenai perubahan yang perlu dilakukan pada struktur database. Sedangkan migrate digunakan untuk menerapkan perubahan tersebut ke database. Jadi, makemigrations digunakan untuk membuat catatan atau instruksi perubahan database, sedangkan migrate digunakan untuk menjalankan perubahan tersebut.

## Deklarasi AI Tugas 2
Dalam pengerjaan tugas ini, saya menggunakan ChatGPT sebagai bantuan untuk memahami konsep Django, serta merapikan beberapa kode.



## Tugas 3
1. ModelForm digunakan karena dapat membuat form berdasarkan model Django tanpa harus membuat semua field secara manual, sehingga lebih praktis digunakan. Dengan ModelForm, data yang diisi juga lebih mudah divalidasi dan disimpan ke database.
{% csrf_token %} digunakan untuk melindungi form dari CSRF (Cross-Site Request Forgery) yaitu serangan yang dapat membuat user mengirimkan request tanpa sengaja. Token ini memastikan request benar-benar berasal dari form yang dibuat oleh aplikasi kita.

2. JSON lebih disukai karena formatnya yang lebih sederhana, ringan, dan mudah dibaca dibandingkan XML. JSON juga lebih praktis digunakan untuk pertukaran data antara frontend dan backend dalam aplikasi web.

3. Ketika user mengakses URL yang mengarah ke fungsi view untuk mendapatkan data dalam format JSON. Fungsi view mengambil data dari database melalui model Django, misalnya dengan Education.objects.all() atau Project.objects.all(). Data tersebut kemudian diberikan ke serializers.serialize() untuk diubah menjadi format JSON. Setelah itu, JSON dikembalikan melalui HttpResponse. Serialization diperlukan karena data dari database masih berupa objek atau QuerySet Django, sehingga perlu diubah menjadi format JSON agar dapat dikirim dan digunakan oleh aplikasi lain.

## Deklarasi AI Tugas 3
Dalam pengerjaan tugas ini, saya menggunakan ChatGPT sebagai alat bantu untuk memahami konsep Django, serta mengecek apakah ada barisan kode yang error.

Seluruh kode dan implementasi tetap saya pelajari, dan sesuaikan secara manual dengan kebutuhan proyek dan instruksi tugas.