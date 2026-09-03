from django.urls import path
from library import views

urlpatterns = [
    path("insert/book/", views.insert_book, name="insert_book"),
    path("manage/books/", views.manage_books, name="manage_books"),
    path("book/details/<int:id>/", views.book_details, name="book_details"),
    path("edit/book/<int:id>/", views.edit_book, name="edit_book"),
    path("delete/book/<int:id>/", views.delete_book, name="delete_book"),
    path("insert/book/issue/", views.insert_book_issue, name="insert_book_issue"),
    path("manage/book/issues/", views.manage_book_issues, name="manage_book_issues"),
    path("return/book/<int:id>/", views.return_book, name="return_book"),
    path("edit/book/issues/<int:id>/", views.edit_book_issue, name="edit_book_issue"),
    path("delete/book/issues/<int:id>/", views.delete_book_issue, name="delete_book_issue"),
]
