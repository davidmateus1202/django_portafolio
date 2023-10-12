from django.shortcuts import render, redirect
from .models import Project
from .forms import Postform



def home(request):
    projects = Project.objects.all()
    return render(request, "home.html", {"projects": projects})

def crear_publicacion(request):

    if request.method == 'POST':
        form = Postform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = Postform()
    context = {
        'form': form
    }
    return render(request, "portafolio/crear_portafolio.html", context)







    return render(request, "portafolio/crear_portafolio.html")
