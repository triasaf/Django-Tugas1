# Tugas 3 PBP - Aplikasi Mywatchlist

## Aplikasi

[Tautan untuk aplikasi yang sudah di-*deploy*](https://djangoprojecttugas2.herokuapp.com/mywatchlist/)  


## Jelaskan perbedaan antara JSON, XML, dan HTML!  
* JSON (JavaScript Object Notation) adalah sebuah format yang bersifat *lightweight*, digunakan untuk menyimpan dan memindahkan data. Biasa digunakan ketika data dikirimkan dari server ke sebuah situs web. JSON relatif lebih ringkas dibanding format data lainnya, mempunyai jumlah karakter yang lebih sedikit, dan lebih mudah di-*parse*. Namun, JSON memiliki kesulitan dalam menggabungkan kumpulan informasi dari sistem yang berbeda.

* XML (eXtensible Markup Language) adalah sebuah markup language seperti HTML (HyperText Markup Language), dengan keduanya diturunkan dari SGML (Standard Generalized Markup Language), yang dirancang untuk menyimpan dan memindahkan data. XML memungkinkan penulisan komen dan dokumennya cenderung lebih sulit diinterpretasi oleh mesin. Dokumen sebuah XML cenderung cukup panjang dibandingkan HTML dan JSON.

* HTML (HyperText Markup Lanugage) adalah sebuah markup language untuk pembuatan situs web, memungkinkan pembuatan struktur seperti paragraf, tabel, tautan menggunakan *tags* dan *attributes*. HTML bertujuan untuk menampilkan data dibandingkan menyimpan atau memindahkan data. Syntax HTML cukup singkat dan menghasilkan text yang diformat.

## Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?  
Dalam pengembangan sebuah platform, pertukaran data pasti terjadi antara client dan server. Data delivery merupakan metode yang digunakan pengembang untuk menjembatani pertukaran data tersebut. Beberapa format data yang digunakan dalam data delivery adalah HTML, JSON, dan XML. Dengan masing-masing mempunyai kegunaannya yang dapat disesuaikan dengan kebutuhan aplikasi.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
* Membuat aplikasi bernama mywatchlist dengan command `python manage.py startapp mywatchlist`
* Membuat fungsi untuk menghandle request html pada views.py lalu melakukan routing dari fungsi tersebut kepada urls yang sesuai pada file mywatchlist/urls dengan menambahkan `path('', show_mywatchlist, name='show_mywatchlist'),` dan `path('mywatchlist/', include('mywatchlist.urls')),` pada file project_django/urls
* Membuat class baru pada file mywatchlist/models.py dengan atribut yang sesuai dengan ketentuan tugas, lalu menjalankan `python manage.py makemigrations` dan `python manage.py migrate`. Setelah itu dibuatkan file .json pada mywatchlist/fixtures dengan data-data yang diinginkan dan dilakukan `python manage.py loaddata initial_mywatchlist_data.json` untuk meng-*load* data.
* Untuk menampilkan data dalam bentuk JSON, XML, dan HTML, perlu dibuat fungsi pada views yang menspesifikasikan return value agar sesuai dengan bentuk yang diinginkan.
* Setelah itu dilakukan routing pada file mywatchlist/urls.py dengan menambahkan path xml/, json/, dan html/ seperti pada langkah di awal.
* Setelah sudah bisa ditampilkan pada local, dilakukan add, commit, push lalu mendeploy aplikasi melalui Github Actions.

## Attachment Postman
![Postman URL XML](https://user-images.githubusercontent.com/74708022/191639333-abe73d0e-e532-4f36-9930-540807581282.png)  

![Postman URL JSON](https://user-images.githubusercontent.com/74708022/191639472-9c00617c-79f6-4065-91aa-e7cca08df794.png)  

![Postman URL HTML](https://user-images.githubusercontent.com/74708022/191639502-8b95cf93-d394-46e9-adf2-759373a8e218.png)