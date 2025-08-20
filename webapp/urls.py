from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('register', views.register, name='register'),
    path('my_login', views.my_login, name='login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('my_logout', views.my_logout, name='logout'),
    path('create_record', views.create_record, name='createrecord'),
    path('view/<int:record_id>', views.view_record, name='view_record'),
    path('update/<int:record_id>', views.update_record, name='update_record'),
    path('delete/<int:record_id>', views.delete_record, name='delete_record'),
    path('search', views.search_record, name='search_record'),




]





