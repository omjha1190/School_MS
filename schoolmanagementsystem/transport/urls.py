from django.urls import path
from transport import views

urlpatterns = [
    path("insert/driver/", views.insert_driver, name="insert_driver"),
    path("manage/drivers/", views.manage_drivers, name="manage_drivers"),
    path("edit/drivers/<int:id>/", views.edit_driver, name="edit_driver"),
    path("delete/drivers/<int:id>/", views.delete_driver, name="delete_driver"),
    path("insert/bus/", views.insert_bus, name="insert_bus"),
    path("manage/buses/", views.manage_buses, name="manage_buses"),
    path("edit/bus/<int:id>/", views.edit_bus, name="edit_bus"),
    path("delete/bus/<int:id>/", views.delete_bus, name="delete_bus"),
]
