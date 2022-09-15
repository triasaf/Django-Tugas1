# Tugas 2 PBP - Aplikasi Katalog

Tautan untuk aplikasi yang sudah di-*deploy*: https://djangoprojecttugas2.herokuapp.com/katalog/

## Bagan 
![image]("D:\TRIAS\Matkul\Semester 3\PBP E\Tugas\Tugas 2\Bagan MVT.png")

## Virtual Environment

### Jelaskan kenapa menggunakan virtual environment?
Virtual environment adalah sebuah Python environment yang memungkinkan isolasi dari instalasi Python interpreter, libraries, dan scripts dengan yang ada pada local. Isolasi ini diperlukan agar setiap project yang dibuat dapat dispesifikasi keperluan-keperluannya, seperti versi Python dan library yang di-install. Versi Python dan library yang berbeda untuk setiap project merupakan hal yang cukup sering ditemukan dalam industri pengembangan web.

### Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Ya, kita tetap dapat membuat aplikasi Django tanpa menggunakan sebuah virtual environment. Namun, seperti yang sudah dijelaskan tadi, perlu diperhatikan versi Python beserta versi libraries yang digunakan pada aplikasi tersebut dengan yang ter-install pada local.

## Implementasi MVT

### Membuat sebuah fungsi pada views.py.
Pertama, perlu dilakukan import untuk file models.py yang berada pada folder katalog. Import ini diperlukan agar views.py dapat mengakses database yang disimpan pada file models.py. Setelah itu, semua instansi data disimpan pada suatu variabel list dan dimasukkan dalam scope context, beserta dengan informasi nama dan NPM. Ini akan diteruskan ke fungsi yang dibuat. Fungsi pada views.py ini memanggil fungsi render yang akan menampilkan konten yang ada dalam scope context dalam HTML melalui file katalog.html.

### Membuat sebuah routing untuk memetakan fungsi yang telah kamu buat pada views.py.
Untuk routing, perlu dilakukan perubahan terhadap urls.py pada folder project_django dan urls.py pada folder katalog.  

Untuk urls.py pada folder project_django, perlu ditambahkan ```path('katalog/', include('katalog.urls')),``` pada variabel urlpatterns agar Django dapat melakukan routing ke file urls.py yang ada pada folder katalog ketika menjalankan aplikasi katalog.  

Untuk urls.py pada folder katalog, perlu dilakukan import untuk file views.py yang berada pada folder katalog. Agar file urls melakukan routing terhadap fungsi yang dibuat pada views.py, perlu ditambahkan  

```
app_name = 'katalog'

urlpatterns = [
    path('', show_catalog, name='show_catalog'),
]
```

agar file urls.py ini di-state kembali untuk aplikasi katalog dan akan routing terhadap fungsi show_catalog


### Memetakan data yang didapatkan ke dalam HTML.
Semua keperluan routing sudah dipenuhi, sehingga sekarang hanya diperlukan perubahan pada file katalog.html agar menampilkan hal yang diinginkan. Dimulai dari mencantumkan nama dan NPM, yaitu dengan menggunakan syntax {{nama_variabel}} untuk kedua variabel tersebut yang sudah ditulis pada views.py. Setelah itu, perlu dilakukan for loop untuk mengakses dan mencetak semua atribut data yang ada pada variabel list di views.py.

### Melakukan deployment ke Heroku.
Setelah implementasi MVT sudah benar, yang diketahui dengan menjalankan manage.py runserver dan melihat aplikasi dari local, akan dilakukan deployment agar aplikasi dapat diakses secara publik. Untuk ini, pertama perlu dibuat aplikasi dari situs web Heroku. Aplikasi ini saya hubungkan dengan repository GitHub yang bersesuaian yaitu untuk Tugas 2 PBP ini. Setelah itu, perlu ditambahkan repository secret yaitu HEROKU_API_KEY yang didapatkan dari situs web Heroku, dan HEROKU_APP_NAME sesuai dengan yang dibuat pada situs web Heroku. Pada tab Actions di repository Tugas 2, dapat dilihat riwayat deployment dan perlu di-run ulang deployment yang gagal. Jika sudah ada centang hijau, dapat dibuka situs aplikasi Heroku sesuai dengan nama aplikasi yang diberikan. 