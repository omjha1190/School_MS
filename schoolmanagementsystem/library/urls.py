from django.urls import path
from library import views

urlpatterns = [
    path("insert/book/", views.insert_book, name="insert_book"),
    path("manage/books/", views.manage_books, name="manage_books"),
    path("book/details/<int:id>/", views.book_details, name="book_details"),
    path("edit/book/<int:id>/", views.edit_book, name="edit_book"),
    path("delete/book/<int:id>/", views.delete_book, name="delete_book"),
]
