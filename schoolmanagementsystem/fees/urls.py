from django.urls import path
from fees import views

urlpatterns = [
    path("insert/fee/", views.insert_fee, name="insert_fee"),
    path("manage/fee/", views.manage_fees, name="manage_fees"),
    path("edit/fee/<int:id>/", views.edit_fee, name="edit_fee"),
    path("delete/fee/<int:id>/", views.delete_fee, name="delete_fee"),
    path("history/fee/<int:id>/", views.fees_history, name="fees_history"),
    path("insert/feeitem/", views.insert_feeitem, name="insert_feeitem"),
    path("manage/feeitems/", views.manage_feeitems, name="manage_feeitems"),
    path("edit/feeitems/<int:id>", views.edit_feeitems, name="edit_feeitems"),
    path("delete/feeitems/<int:id>", views.delete_feeitem, name="delete_feeitem"),
]
