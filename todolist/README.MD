# Tugas 4 PBP - Aplikasi To Do List

## Aplikasi

[Tautan untuk aplikasi yang sudah di-*deploy*](https://djangoprojecttugas2.herokuapp.com/todolist/)  


## Apa kegunaan {% csrf_token %} pada elemen `<form>` ? 
csrf = cross-site request forgery
Kegunaan csrf token adalah menambahkan argumen pada sebuah request dengan sebuah token berupa angka besar yang digenerasi secara random. Token ini akan berbeda tiap kali aplikasi dijalankan oleh user yang berbeda. Token ini akan dibandingkan dengan token seorang user ketika user tersebut ingin melakukan POST atau GET, dan hanya akan dilanjutkan ketika token sama. Ini digunakan untuk keperluan keamanan sebuah aplikasi

Referensi: https://stackoverflow.com/questions/5207160/what-is-a-csrf-token-what-is-its-importance-and-how-does-it-work

## Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen `<form>`?
Jika tidak ada csrf token, aplikasi akan tetap berjalan dengan semestinya, tetapi ada kemungkinan keamanan data dalam aplikasi terancam. Hal ini karena tanpa adanya token yang dihasilkan csrf token, ruang umum dapat mengakses request seorang user, dan melakukan fitur yang tersedia pada aplikasi tersebut, dalam kasus aplikasi ini, berarti ruang umum dapat mengubah status task, menghapus sebuah task, atau melakukan logout.

Referensi: https://stackoverflow.com/questions/5207160/what-is-a-csrf-token-what-is-its-importance-and-how-does-it-work

## Apakah kita dapat membuat elemen `<form>` secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? 
Kita bisa saja membuat elemen form tanpa menggunakan form.as_table. Jika menggunakan itu, mungkin ada beberapa variable yang ada di database tidak memerlukan di-POST sehingga kita dapat membuat form manual untuk mengatasinya. 


Ya, kita bisa membuat elemen form secara manual tanpa generator 

## Jelaskan secara gambaran besar bagaimana cara membuat `<form>` secara manual.
Berikut merupakan contoh pembuatan form secara manual
```
<form method="POST" action="">
        {% csrf_token %}
        <table>
            <tr>
                <td>Title:</td>
                <td><input type="text" name="title" class="form-control"></td>
            </tr>
                    
            <tr>
                <td>Description: </td>
                <td><input type="text" name="description" class="form-control"></td>
            </tr>
        </table>

        <input type="submit" name="submit" value="Create"/>
</form>
```
Form dibuat langsung di html. Ditandai dengan pembatas `<form> </form>` dengan method POST, lalu untuk keperluan kerapihan, dibuat tabel karena perlu ada 2 input pada form ini, masing-masing dalam sebuah tr. Textfield yang akan diisi oleh user ditandai dengan awalan input, dilanjutkan dengan beberapa argumen yang dibutuhkan. name merupakan argumen yang penting karena dibutuhkan untuk retrieval data. Dibawah tabel input, diperlukan tombol submit untuk menyimpan hasil input user.

## Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML. 
Hasil input dari user bisa diakses melalui `request.POST.get({nama_input})` pada `todolist/views.py`. Data kemudian digunakan untuk membuat instansi objek class pada `todolist/models.py` dengan menggunakan method `{ClassName}.objects.create(args)` dengan `args` disesuaikan berdasarkan atribut yang ada pada class tersebut.   
Pada tahap ini, data dari input user pada form sudah masuk ke database, sekarang diperlukan untuk dimunculkan pada html. Untuk itu, objek ini perlu di pass dalam `context` yang ada pada fungsi yang bertujuan untuk menampilkan html, pada kasus ini, `show_todolist`. Dalam fungsi itu, instansi objek baru akan diambil pada statement `{ClassName}.objects.filter(user=request.user)` yang masuk ke context dalam bentuk list.  
Setelah di dalam context, kita dapat mengakses data tersebut pada file html. Tiap objek pada list tersebut akan diiterasi pada sebuah `for-loop`. Dalam `for-loop` tersebut, kita dapat mengakses tiap atribut pada objek tersebut untuk ditampilkan sesuai format yang kita inginkan.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas. 
- Melakukan perintah `python manage.py startapp todolist` untuk menginisiasi file-file yang dibutuhkan untuk membuat aplikasi baru
- Membuat fungsi untuk menghandle request html pada views.py lalu melakukan routing dari fungsi tersebut kepada urls yang sesuai pada file `todolist/urls` dengan menambahkan `path('', show_todolist, name='show_todolist'),` dan `path('todolist/', include('todolist.urls')),` pada file `project_django/urls`
- Membuat class baru pada file `todolist/models.py` dengan atribut yang sesuai dengan ketentuan tugas, lalu menjalankan `python manage.py makemigrations` dan `python manage.py migrate`.
- Membuat fungsi login, logout, dan register pada `todolist/views.py` untuk menghandle registrasi, login, logout, serta implementasi COOKIES
- Melakukan routing untuk fungsi-fungsi tersebut pada file `todolist/urls.py` dengan menambahkan masing-masing fungsi pada urlpatterns
- Membuat fungsi `create_task` pada `todolist/views.py` dengan implementasi retrieval data pada form manual seperti yang dijelaskan pada poin sebelumnya. Hal ini mencakup membuat file html yang berisi form serta tombol submit.
- Membuaat fungsi untuk menghapus task dan mengubah status task, `deletetask` dan `finishtask`, dengan logika yang cukup simpel memanfaatkan method dari objects.
- Melakukan routing untuk masing-masing fungsi tersebut pada file `todolist/urls.py`
- Menambahkan button untuk `finishtask` dan `deletetask` pada `todolist.html`
- Setelah semua sudah berjalan semestinya pada local, dilakukan add, commit, dan push, lalu deployment melalui Github Actions.