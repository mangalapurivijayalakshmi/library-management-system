"""
URL configuration for library_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView
from app.views import *

urlpatterns = [
    path('', RedirectView.as_view(url='book_list/')),
    path('admin/', admin.site.urls),
    path('book_list/', book_list, name='book_list'),
    path('add_books/', add_books, name='add_books'),
    path('edit/<int:id>/', edit_book, name='edit_book'),
    path('delete/<int:id>/', delete_book, name='delete_book'),
    path('issue/<int:id>/', issue_book, name='issue_book'),
    path('return/<int:transaction_id>/', return_book, name='return_book'),
    path('transactions/', transaction_list, name='transaction_list'),
]