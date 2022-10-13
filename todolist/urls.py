from django.urls import path
from todolist.views import deletetask, finishtask, show_todolist, register, login_user, logout_user, create_task, get_todolist_json, add_todolist_item, deleteTask



app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'), 
    path('create-task/', create_task, name='create_task'),
    path('add/', add_todolist_item, name='add_todolist_item'),
    path('finishtask/<int:pk>', finishtask, name='finishtask'),
    path('json/', get_todolist_json, name='get_todolist_json'),
    path('deletetask/<int:pk>', deletetask, name='deletetask'),
    path('delete/<int:pk>', deleteTask,name='deleteTask')
    # path('xml/', show_mywatchlist_xml, name='show_mywatchlist_xml'),
    # path('json/', show_mywatchlist_json, name='show_mywatchlist_json'),
    # path('html/', show_mywatchlist, name='show_mywatchlist'),

]