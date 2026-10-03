Name : Juan Imanuel

NPM : 2506619455

Class : PBP A

# Deskripsi Proyek
Proyek ini merupakan website portofolio pribadi yang dibuat menggunakan Django. Website ini menampilkan informasi seperti profil, pengalaman, proyek, dan pendidikan.

Website ini dikembangkan secara bertahap melalui beberapa tugas dengan menerapkan konsep Django seperti Model-View-Template (MVT), ModelForm, JSON API, Authentication, dan Authorization.


## Testing dan Run Project
Untuk memastikan websitenya berjalan dengan baik, gunakan perintah:

python manage.py check, atau

Perintah tersebut digunakan untuk memeriksa konfigurasi dan mendeteksi masalah yang ada pada proyek Django.

Untuk menjalankan test pada aplikasi main, gunakan:

python manage.py test main

Jika tidak terdapat error, maka server dapat dijalankan menggunakan:

python manage.py runserver

Setelah server berjalan, website dapat diakses melalui alamat yang ditampilkan oleh Django.



## Refleksi Tugas 2
1. Ketika pengguna membuka halaman Projects, browser akan mengirimkan permintaan ke website. Permintaan tersebut pertama kali diproses oleh urls.py yang ada di proyek portofolio. File ini berfungsi untuk mengatur URL utama pada proyek dan meneruskan permintaan ke aplikasi main. Setelah diteruskan ke aplikasi main, permintaan akan diperiksa oleh main/urls.py untuk menentukan halaman yang sesuai. Karena pengguna membuka halaman Projects, Django akan menjalankan view yang menangani halaman tersebut. View kemudian mengambil data Projects dari model yang terhubung dengan database. Data yang sudah didapatkan kemudian dikirim dari view ke template. Di dalam template, data tersebut ditampilkan menggunakan Django Template Language. Setelah template selesai diproses, Django menghasilkan halaman HTML dan mengirimkannya kembali ke browser sehingga pengguna dapat melihat daftar Projects. Jadi, secara sederhana alurnya adalah browser mengirim request, kemudian request diteruskan dari URL proyek ke URL aplikasi, lalu view mengambil data dari model dan mengirimkannya ke template untuk ditampilkan di browser.

2. Karena data akan lebih mudah untuk dikelola dan diubah. Jika data ditulis langsung di dalam template, setiap kali ingin menambahkan, mengubah, atau menghapus data, kita harus mengubah kode HTML secara manual. Dengan menggunakan model, data dapat dikelola melalui database tanpa perlu mengubah template. Contohnya, ketika ingin menambahkan project baru, kita cukup menambahkan data project tersebut ke database.

3. Makemigrations digunakan untuk membuat file migrasi berdasarkan perubahan yang dilakukan pada model. File migrasi tersebut berisi informasi mengenai perubahan yang perlu dilakukan pada struktur database. Sedangkan migrate digunakan untuk menerapkan perubahan tersebut ke database. Jadi, makemigrations digunakan untuk membuat catatan atau instruksi perubahan database, sedangkan migrate digunakan untuk menjalankan perubahan tersebut.

## Deklarasi AI Tugas 2
Dalam pengerjaan tugas ini, saya menggunakan ChatGPT sebagai bantuan untuk memahami konsep Django, serta merapikan beberapa kode.



## Refleksi Tugas 3
1. ModelForm digunakan karena dapat membuat form berdasarkan model Django tanpa harus membuat semua field secara manual, sehingga lebih praktis digunakan. Dengan ModelForm, data yang diisi juga lebih mudah divalidasi dan disimpan ke database.
{% csrf_token %} digunakan untuk melindungi form dari CSRF (Cross-Site Request Forgery) yaitu serangan yang dapat membuat user mengirimkan request tanpa sengaja. Token ini memastikan request benar-benar berasal dari form yang dibuat oleh aplikasi kita.

2. JSON lebih disukai karena formatnya yang lebih sederhana, ringan, dan mudah dibaca dibandingkan XML. JSON juga lebih praktis digunakan untuk pertukaran data antara frontend dan backend dalam aplikasi web.

3. Ketika user mengakses URL yang mengarah ke fungsi view untuk mendapatkan data dalam format JSON. Fungsi view mengambil data dari database melalui model Django, misalnya dengan Education.objects.all() atau Project.objects.all(). Data tersebut kemudian diberikan ke serializers.serialize() untuk diubah menjadi format JSON. Setelah itu, JSON dikembalikan melalui HttpResponse. Serialization diperlukan karena data dari database masih berupa objek atau QuerySet Django, sehingga perlu diubah menjadi format JSON agar dapat dikirim dan digunakan oleh aplikasi lain.

## Deklarasi AI Tugas 3
Dalam pengerjaan tugas ini, saya menggunakan ChatGPT sebagai alat bantu untuk memahami konsep Django, serta mengecek apakah ada barisan kode yang error.

Seluruh kode dan implementasi tetap saya pelajari, dan sesuaikan secara manual dengan kebutuhan proyek dan instruksi tugas.



## Tugas 4
Sebelum mengerjakan tugas 4, saya telah menyelesaikan tutorial 4 dan belajar mengenai konsep Authentication dan Authorization. Di tugas 4 ini saya menerapkan kedua konsep tersebut untuk membatasi tindakan yang dapat dilakukan oleh setiap pengguna. Terdapat empat role, yaitu:

1. Pengunjung yang belum login; hanya dapat melihat data yang ada pada website. Untuk memberikan Star pada Project, pengunjung harus login terlebih dahulu.

2. Pengguna yang sudah login; dapat melihat data serta memberikan atau membatalkan Star pada Project. Namun, tidak dapat menambah/mengubah Project maupun Education.

3. Editor (dibuat menggunakan fitur Group pada Django Admin). Editor memiliki hak yang sama seperti pengguna yang sudah login, bedanya dapat mengubah/mengedit data Project dan Education. Editor tidak dapat menambah/menghapus data.

4. Pemilik portofolio (superuser); dapat melihat data, memberikan atau membatalkan Star, serta menambah/mengubah dan menghapus data Project maupun Education.

## Deklarasi AI Tugas 4
Dalam pengerjaan tugas ini, saya menggunakan ChatGPT sebagai alat bantu untuk memahami konsep Authentication dan Authorization pada Django, khususnya membantu untuk mengecek bagian kode yang masih error.

Link percakapan dengan ChatGPT:
https://chatgpt.com/share/6aba7d54-7eac-83ec-b4eb-db78a1a845a0



## Refleksi Tugas 5
1. Debouncing adalah teknik untuk menunda pemanggilan suatu fungsi hingga jeda waktu berlalu tanpa adanya event baru. Pada pencarian yang menggunakan AJAX, teknik ini mencegah request yang dikirim setiap kali pengguna mengetik, sehingga jumlah request dan beban server dapat dikurangi serta proses pencarian jadi lebih efisien.

2. await digunakan untuk menunggu sampai proses fetch() selesai sebelum baris kode berikutnya dijalankan. Tanpa adanya await, kode akan langsung melanjutkan prosesnya tanpa menunggu hasil dari fetch(), sehingga data yang dibutuhkan mungkin belum tersedia ketika digunakan.

3. Cross-Site Scripting (XSS) adalah serangan ketika penyerang berhasil menyisipkan kode JavaScript miliknya ke dalam halaman web yang kemudian dijalankan di browser pengguna lain. Data yang ditampilkan melalui AJAX/JavaScript lebih rentan karena data tersebut dimasukan ke halaman web secara langsung oleh JavaScript. Jika data tersebut tidak di escape, kode berbahaya dapat dijalankan oleh browser. Sedangkan Django secara otomatis melakukan escaping pada data yang ditampilkan menggunakan {{}}.

## Deklarasi AI Tugas 5
Pada pengerjaan tugas 5, saya menggunakan ChatGPT sebagai alat bantu untuk memahami materi terkait AJAX serta mengecek kode untuk mencari kemungkinan adanya penulisan kode yang typo/error.

Link percakapan dengan ChatGPT:
https://chatgpt.com/share/6ac0f7c9-a8f0-83ec-9154-9a7f00aab680