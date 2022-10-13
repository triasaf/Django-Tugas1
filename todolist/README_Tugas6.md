# Tugas 6 PBP - Aplikasi To Do List

## Aplikasi

[Tautan untuk aplikasi yang sudah di-*deploy*](https://djangoprojecttugas2.herokuapp.com/todolist/)  


## Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.
Synchronous programming memproses operasi secara sekuensial, artinya request dihandle secara satu per satu pada server (single-thread), menunggu 1 selesai sebelum lanjut ke request berikutnya  
Sedangkan asynchronous programming dapat memproses banyak request secara bersamaan karena bersifat multi-threaded.  
Karena perbedaan tersebut, asynchronous programming dapat mengupdate suatu tampilan website secara asinkronus, yaitu tanpa adanya refresh.

## Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
Paradigma event-driven programming adalah paradigma dimana sebuah program dieksekusi dan di-handle berdasarkan event yang terjadi. Event akan ditangkap oleh suatu listener dan dilanjutkan dengan handling oleh event handler berupa sebuah function. Pada program ini, terdapat event-driven programming pada implementasi menambahkan task baru.
```
<button type="button" class="btn btn-primary" id="addtaskbutton" data-bs-dismiss="modal">Add</button>
```

```
document.getElementById("addtaskbutton").onclick = addTodolist
```

```
  function addTodolist() {
    fetch("{% url 'todolist:add_todolist_item' %}", {
          method: "POST",
          body: new FormData(document.querySelector('#formtask'))
      }).then(refreshTodolist)
    return false
  }
```

```
def add_todolist_item(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        description = request.POST.get("description")

        new_barang = Task(user=request.user, title=title, description=description, date=datetime.datetime.now(), is_finished=False)
        new_barang.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()
```

## Jelaskan penerapan asynchronous programming pada AJAX.
Penerapan asynchronous programming pada AJAX menyebabkan website tidak perlu refresh browser ketika ada suatu update yang terjadi pada database atau tampilan. Ini dimungkinkan karena AJAX telah melakukan pertukaran data antara web browser dan web server karena AJAX dapat mengakses data dari sumber eksternal meskipub website sudah selesai loading, berbeda dengan sebuah HTTP request.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
Semua pekerjaan saya pada tugas 6 ini berdasarkan implementasi contoh solusi asdos pada [Solusi Tutorial 5](https://github.com/pbp-fasilkom-ui/tutorial-5-example).

- Membuat fungsi `get_todolist_json` pada views untuk mereturn http response berupa database dalam bentuk json lalu dirouting pada url `todolist/json`
```
def get_todolist_json(request):
    todolist_item = Task.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', todolist_item))
```
- Membuat fungsi asinkronus javascript `getTodolist` pada `todolist.html` yang melakukan fetch terhadap url tersebut
```
  async function getTodolist() {
    return fetch("{% url 'todolist:get_todolist_json' %}").then((res) => res.json())
  }
```
- fungsi `getTodolist` akan dimanfaatkan pada fungsi asinkronus `refreshTodolist` yang mengupdate html agar sesuai dengan database yang ada. Perlu dicatat bahwa implementasi status belum selesai pada versi ini.
```
  async function refreshTodolist() {
        document.getElementById("cardcontainer").innerHTML = ""
        const todolist = await getTodolist()
        let htmlString = ``
        todolist.forEach((item) => {
          htmlString += `<div class="col-md-4">
      <div class="card" style="width: 18rem;">
        <img src="https://drive.google.com/uc?export=view&id=17KEpEig6Y5PX9nUwZl1INRzj9Xuuz9NS" class="card-img-top"
          alt="...">
        <div class="card-body">
          <h5 class="card-title">${item.fields.title}</h5>
          <h6 class="card-subtitle mb-2 text-muted">${item.fields.date}</h6>
          <p class="card-text">${item.fields.description}</p>
          <p class="card-text"></p> 
          {% if task.is_finished %}
          <p class="card-text">Finished</p>
          {% else %}
          <p class="card-text">Not Finished</p>
          {% endif %}
          
          
          
        </div>
      </div>
    </div>` 
        })
        
        document.getElementById("cardcontainer").innerHTML = htmlString
  }
```
- Membuat fungsi `add_todolist_item` pada views untuk menambahkan objek baru ke database lalu dirouting pada url `todolist/add`
```
def add_todolist_item(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        description = request.POST.get("description")

        new_barang = Task(user=request.user, title=title, description=description, date=datetime.datetime.now(), is_finished=False)
        new_barang.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()
```
- Membuat fungsi `addTodolist` pada `todolist.html` yang melakukan fetch terhadap url tersebut dengan method POST dan dengan body berisi FormData dari `form` yang dibuat pada `todolist.html`
```
  function addTodolist() {
    fetch("{% url 'todolist:add_todolist_item' %}", {
          method: "POST",
          body: new FormData(document.querySelector('#formtask'))
      }).then(refreshTodolist)
    return false
  }
```
```
...
<form id="formtask">
    {% csrf_token %}
    <div class="mb-3">
        <label for="recipient-name" class="col-form-label">Title:</label>
        <input type="text" class="form-control" id="field_title" name="title">
            </div>
            <div class="mb-3">
              <label for="message-text" class="col-form-label">Description:</label>
              <textarea class="form-control" id="field_desc" name="description"></textarea>
            </div>
          </form>
...
```
- Membuat implementasi sebuah button untuk menambah task baru yang akan menampilkan modal berisi form yang di-refer pada fungsi `addTodolist`
- Menambahkan implementasi jQuery agar dokumen selalu melakukan `refreshTodolist` pada setiap kali di-load
```
$(document).ready(function()  {
    refreshTodolist();
  });
```