from django.shortcuts import render, redirect
from basic.models import Cafe
from basic.forms import CafeForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def loadinfo(request):
    return render(request, 'map_info.html')

def loadlist(request):
    cafes = Cafe.objects.all()
    return render(request, 'cafe_list.html', {'cafes': cafes})

def loadmap(request):
    cafes = Cafe.objects.all()
    return render(request, 'cafe_map.html', {'cafes': cafes})

def new_cafe(request):
    if request.method == "POST":
        form = CafeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/cafe_list/')
    else:
        form = CafeForm()
    return render(request, 'cafe_edit.html', {'form': form})

def edit_cafe(request, Engname):
    cafe = Cafe.objects.get(Engname=Engname)
    if request.method == "POST":
        form = CafeForm(request.POST, instance=cafe)
        if form.is_valid():
            form.save()
            return redirect('/cafe_list/')
    else:
        form = CafeForm(instance=cafe)
    return render(request, 'cafe_edit.html', {'form': form})

def delete_cafe(request, Engname):
    cafe = Cafe.objects.get(Engname=Engname).delete()
    return redirect('/cafe_list/')

def loadtest(request):
    cafes = Cafe.objects.all()
    return render(request, 'test.html', {'cafes': cafes})

