Name : Juan Imanuel

NPM : 2506619455

Class : PBP A

### Tugas 2

1. Ketika pengguna membuka halaman Projects, browser akan mengirimkan permintaan ke website. Permintaan tersebut pertama kali diproses oleh urls.py yang ada di proyek portofolio. File ini berfungsi untuk mengatur URL utama pada proyek dan meneruskan permintaan ke aplikasi main. Setelah diteruskan ke aplikasi main, permintaan akan diperiksa oleh main/urls.py untuk menentukan halaman yang sesuai. Karena pengguna membuka halaman Projects, Django akan menjalankan view yang menangani halaman tersebut. View kemudian mengambil data Projects dari model yang terhubung dengan database. Data yang sudah didapatkan kemudian dikirim dari view ke template. Di dalam template, data tersebut ditampilkan menggunakan Django Template Language. Setelah template selesai diproses, Django menghasilkan halaman HTML dan mengirimkannya kembali ke browser sehingga pengguna dapat melihat daftar Projects. Jadi, secara sederhana alurnya adalah browser mengirim request, kemudian request diteruskan dari URL proyek ke URL aplikasi, lalu view mengambil data dari model dan mengirimkannya ke template untuk ditampilkan di browser.

2. Karena data akan lebih mudah untuk dikelola dan diubah. Jika data ditulis langsung di dalam template, setiap kali ingin menambahkan, mengubah, atau menghapus data, kita harus mengubah kode HTML secara manual. Dengan menggunakan model, data dapat dikelola melalui database tanpa perlu mengubah template. Contohnya, ketika ingin menambahkan project baru, kita cukup menambahkan data project tersebut ke database.

3. Makemigrations digunakan untuk membuat file migrasi berdasarkan perubahan yang dilakukan pada model. File migrasi tersebut berisi informasi mengenai perubahan yang perlu dilakukan pada struktur database. Sedangkan migrate digunakan untuk menerapkan perubahan tersebut ke database. Jadi, makemigrations digunakan untuk membuat catatan atau instruksi perubahan database, sedangkan migrate digunakan untuk menjalankan perubahan tersebut.


### Deklarasi AI
Dalam pengerjaan tugas ini, saya menggunakan ChatGPT sebagai bantuan untuk memahami konsep Django, serta merapikan beberapa kode.