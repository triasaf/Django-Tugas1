# Tugas 5 PBP - Aplikasi To Do List

## Aplikasi

[Tautan untuk aplikasi yang sudah di-*deploy*](https://djangoprojecttugas2.herokuapp.com/todolist/)  

## Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?
### Inline  
Mendefinisikan css yang digunakan pada tiap-tiap elemen dalam file html, contoh: `<h1 style="color:white;padding:30px;">Halo Dunia</h1>`  

Berguna untuk mencoba-coba dan menguji perubahan serta perbaikan yang cepat, tetapi sangat tidak efisien karena harus diterapkan untuk tiap elemen

### Internal  
Mendefinisikan css yang digunakan dalam file html, terpisah dengan elemen html, dan ditandai oleh tag `<style></style>`, contoh: 
```
...
<style>
h1 {
    color: red;
    padding: 60px;
} 
</style>
...
<h1>Halo Dunia</h1>
...
```

Kelebihan untuk inline adalah perubahan hanya pada 1 halaman dan tidak perlu upload file baru. Kekurangannya jika ada styling CSS sama yang ingin digunakan pada file yang berbeda.

### External  
Mendefinisikan css yang digunakan pada file css yang terpisah dengan file html. Contohnya `style.css`, dapat dihubungkan ke file html dengan merefernya pada tag head suatu html:

file `style.css`
```
h1 {
    color: red;
    padding: 60px;
} 
```

file `my.html`
```
...
<head>
    <link rel="stylesheet" type="text/css" href="style.css" />
</head>
...
<h1>Halo Dunia</h1>
```
Ukuran file HTML lebih kecil, struktur lebih rapih, dan loading menjadi cepat, tetapi file CSS harus diload terlebih dahulu sebelum tampilan muncul sempurna.

## Jelaskan tag HTML5 yang kamu ketahui.
- `<h1></h1>` sampai `<h6></h6>` untuk heading dari besar ke kecil
- `<a></a>` untuk link
- `<form></form>` untuk menerima input seperti login pada tugas 4 dan 5
- `<img></img>` untuk mencantumkan gambar
- `<table></table>` untuk membuat tabel serta `<tr></tr>` `<th></th>` dan `<td></td>` untuk table row, table header, dan table data
- dan masih banyak lagi

## Jelaskan tipe-tipe CSS selector yang kamu ketahui.

- `*` -> Universal Selector untuk memilih semua elemen
- `.` -> Class Selector untuk memilih semua elemen dalam suatu class
- `#` -> ID Selector untuk memilih semua elemen dengan id tertentu
- Type Selector untuk memilih semua elemen dengan tipe tertentu, contoh: `h1` untuk semua elemen dalam `<h1></h1>`

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
- Mencari [referensi bootstrap login page](https://mdbootstrap.com/docs/standard/extended/login/) pada browser.
- Mengambil bagian seperti tambahan argumen class, agar tampilan sesuai dengan yang diinginkan.
- Menyesuaikan dengan ketentuan soal dan fungsionalitas aplikasi, seperti tipe input untuk field username, dan untuk button submit.
- Menyesuaikan page `logout`, `register`, dan `create_task` dengan styling yang sama.
- Mencari [referensi bootstrap implementasi card](https://codepen.io/nikki-peel/pen/RwavQer) pada browser.
- Mengambil bagian seperti tambahan argumen class, terutama class card, agar sesuai dengan tampilan yang diinginkan.
- Menyesuaikan dengan ketentuan soal dan fungsionalitas aplikasi, seperti implementasi `for-loop` untuk setiap task, dan button untuk `delete task` dan `finish task`
- Menyimpan perubahan lalu melakukan add, commit, push. 