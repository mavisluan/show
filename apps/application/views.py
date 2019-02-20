from django.shortcuts import render, redirect, HttpResponse
from .models import Show


def index(request):
    context = {
        'all_shows': Show.objects.all()
    }
    return render(request, 'application/index.html', context)


def new(request):
    return render(request, 'application/new.html')


def process_add(request):
    if request.method == "POST":
        Show.objects.create(title=request.POST['title'], network=request.POST['network'],
                            release_date=request.POST['release_date'], description=request.POST['description'])

        return redirect('/shows')


def show_info(request, id):
    context = {"show": Show.objects.get(id=id)}
    return render(request, 'application/show_info.html', context)


def edit(request, id):
    context = {"show": Show.objects.get(id=id)}
    return render(request, 'application/edit_show.html', context)


def process_edit(request, id):
    if request.method == "POST":
        show = Show.objects.get(id=id)
        show.title = request.POST['title']
        show.network = request.POST['network']
        show.release_date = request.POST['release_date']
        show.description = request.POST['description']
        show.save()

        return redirect(f"/shows/{id}")


def process_delete(request, id):
    show = Show.objects.get(id=id)
    show.delete()

    return redirect(f"/shows")
