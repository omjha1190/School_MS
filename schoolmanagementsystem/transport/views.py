from django.shortcuts import render, redirect
from .models import Driver, Bus

# Create your views here.
def insert_driver(req):
    if req.method == "POST":
        driver = Driver()
        driver.name = req.POST.get('name')
        driver.phone = req.POST.get('phone')
        driver.address = req.POST.get('address')
        driver.license_number = req.POST.get('license_number')
        driver.cover_image = req.FILES.get('cover_image')
        driver.save()
        return redirect(manage_drivers)
    return render(req, "transport/insert_driver.html")

def manage_drivers(req):
    data = {
        "drivers" : Driver.objects.all(),
    }
    return render(req, "transport/manage_drivers.html", data)

def edit_driver(req, id):
    data = {
        "driver" : Driver.objects.get(id=id),
    }
    if req.method == "POST":
        driver = Driver.objects.get(id=id)
        driver.name = req.POST.get('name')
        driver.phone = req.POST.get('phone')
        driver.address = req.POST.get('address')
        driver.license_number = req.POST.get('license_number')
        driver.cover_image = req.FILES.get('cover_image')
        driver.save()
        return redirect(manage_drivers)
    return render(req, "transport/insert_driver.html", data)

def delete_driver(req, id):
    data = {}
    try:
        driver = Driver.objects.get(id=id)
        driver.delete()
        return redirect(manage_drivers)
    except Driver.DoesNotExist:
        data ['error'] = "This Driver does not exit"
    return redirect(manage_drivers)    

def insert_bus(req):
    data = {
        "drivers" : Driver.objects.all()
    }
    if req.method == "POST":
        bus = Bus()
        bus.bus_number = req.POST.get('bus_number')
        bus.registration_number = req.POST.get('registration_number')
        bus.route = req.POST.get('route')
        bus.driver = Driver.objects.get(id=req.POST.get('driver'))
        bus.save()
        return redirect("manage_buses")
    return render(req, "transport/insert_bus.html", data)

def manage_buses(req):
    data = {
        "buses" : Bus.objects.all()
    }
    return render(req, "transport/manage_buses.html", data)

def edit_bus(req, id):
    data = {
        "bus" : Bus.objects.get(id=id),
    }
    if req.method == "POST":
        bus = Bus.objects.get(id=id)
        bus.bus_number = req.POST.get('bus_number')
        bus.registration_number = req.POST.get('registration_number')
        bus.route = req.POST.get('route')
        bus.driver = Driver.objects.get(id=req.POST.get('driver'))
        bus.save()
        return redirect("manage_buses")
    return render(req, "transport/insert_bus.html", data)

def delete_bus(req, id):
    data = {}
    try :
        bus = Bus.objects.get(id=id)
        bus.delete()
        return redirect("manage_buses")
    except Bus.DoesNotExist:
        data ['error'] = "This bus is not available"
    return redirect("manage_buses")