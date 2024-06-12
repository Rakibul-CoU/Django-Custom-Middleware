from django.urls import path

from api.views import book_list

urlpatterns = [
    path("books/", book_list, name="book_list")
]