from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages

def shows(request):
    
    context = {
        'all_shows': Show.objects.all(),
    }
    return render(request, 'shows.html', context)

def new(request):
    print("njgrvfekknsgrjkmvfjnsh")

    #context ={
    #    'showID': Show.objects.get(id=showID)
    #}
    #new_show = Show.objects.create(title=request.POST['title'])
    #getID = Show.objects.get(id = "showID")
    #context = {
    #    'new_show':new_show,
    #    'getID':showID,
    #}
    return render(request, 'create.html')

def create(request):
    errors = Show.objects.basic_validator(request.POST)
    print(errors)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/shows/new')
    #else:
    #    show = Show.objects.get(id=showID)
    #    show.title = request.POST['title']
    #    show.network = request.POST['network']
    #    show.date = request.POST['date']
    #    show.desc = request.POST['desc']
    #    show.save()
        #messages.success(request, "Show successfully updated")
       # return redirect(f'/shows/{showID}')
    newshow = Show.objects.create(title = request.POST['title'], network = request.POST['network'], date = request.POST['date'], desc = request.POST['desc'])
    #getID = Show.objects.get(id=request.POST['showID'])
    print(newshow)
    #new_show = Show.objects.create(title=request.POST['title'], network=request.POST['network'], date=request.POST['date'], desc=request.POST['desc'] )
    #getID = Show.objects.get(id=showID)
    
    return redirect(f'shows/{newshow.id}')

def showinfo(request, showID):
    context = {
        'show': Show.objects.get(id=showID)
    }
   # 'new_show': new_show,
#        'showID': showID,
#    }
    return render(request, 'showinfo.html', context)

def edit(request, showID):
    context = {
        'show': Show.objects.get(id=showID)
    }

    return render(request, 'edit.html', context)
def update(request, showID):
    errors = Show.objects.basic_validator(request.POST)
    print (errors)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/shows/{showID}/edit')
    else:
        show = Show.objects.get(id=showID)
        show.title = request.POST['title']
        show.network = request.POST['network']
        show.date = request.POST['date']
        show.desc = request.POST['desc']
        show.save()
        messages.success(request, "Show successfully updated")
    return redirect(f'/shows/{showID}')

def destroy(request, showID):
    c = Show.objects.get(id=showID)
    c.delete()
    return redirect('/shows')

def index(request):
    return redirect('/shows')
