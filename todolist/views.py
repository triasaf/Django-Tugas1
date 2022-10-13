from django.shortcuts import render
from todolist.models import Task

from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.core import serializers
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt



#
def get_todolist_json(request):
    todolist_item = Task.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', todolist_item))


# TODO: belom bener
def add_todolist_item(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        description = request.POST.get("description")

        new_barang = Task(user=request.user, title=title, description=description, date=datetime.datetime.now(), is_finished=False)
        new_barang.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

@csrf_exempt 
def deleteTask(request, pk):
    if request.method =='DELETE' :
        task_selected = Task.objects.get(id=pk)
        Task.delete(task_selected)

        return JsonResponse(b"DELETED", status=201)
    

    


# Show html function
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    list_task = Task.objects.filter(user= request.user)

    # transfer data from database to html
    context = {
        'list_task' : list_task,
        'name' : 'Trias Ahmad Fairuz',
        'id' : '2106633645',
        'last_login': request.COOKIES['last_login'],
        'username' : request.user.username,
    }
    return render(request, "todolist.html", context)

# create new task function
def create_task(request):
    if request.method == 'POST':
        # get the information needed to create a Task object from html form
        title = request.POST.get('title')
        description = request.POST.get('description')
        date = datetime.datetime.now()
        user = request.user
        Task.objects.create(title=title, description=description, date=date, user=user, is_finished=False)
        return redirect('todolist:show_todolist')

    return render(request, "create_task.html")

# finish task function
def finishtask(request, pk):
    task_selected = Task.objects.get(id=pk)
    task_selected.is_finished = True
    task_selected.save()
    return redirect('todolist:show_todolist')

# delete task function
def deletetask(request, pk):
    task_selected = Task.objects.get(id=pk)
    Task.delete(task_selected)
    return redirect('todolist:show_todolist')


def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response