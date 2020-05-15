from django.shortcuts import render
from django.http import HttpResponse
from testapp.models import User

# Create your views here.
def gotohome(request):
    return render(request, 'testapp/UIhome.html')

def addPage(request):
    return render(request, 'testapp/UIAdd.html')

def adduser(request):
    if request.method == "POST":
        name=request.POST.get('U_name')
        pass1=request.POST.get('U_pass')
        print(name,pass1)
        u=User(U_name=name,U_pass=pass1)
        u.save()
        return HttpResponse("User has been added!")

def deletePage(request):
    return render(request, 'testapp/UIDelete.html')

def deleteuser(request):
    if request.method == "POST":
        id=request.POST.get('U_id')
        user=User.objects.get(id=id)
        user.delete()
        return HttpResponse("User is deleted...")

def searchPage(request):
    return render(request, 'testapp/UISearch.html')

def searchuser(request):
    if request.method == "POST":
        id=request.POST.get('U_id')
        user=User.objects.get(id=id)
        return HttpResponse("User name : "+user.U_name+" User password : "+user.U_pass)

def updatePage(request):
    return render(request, 'testapp/UIUpdate.html')

def updateuser(request):
    if request.method == "POST":
        id=request.POST.get('U_id')
        user=User.objects.get(id=id)
        password=request.POST.get('U_pass')
        user.U_pass=password
        user.save()
        return HttpResponse("User is updated!")


def userDetails(request):
    data=User.objects.all()
    return render(request, 'testapp/UIUsers.html', {'users': data})

def loginPage(request):
    return render(request, 'testapp/UIlogin.html')

def login(request):
    if request.method == "POST":
        name=request.POST.get('U_name')
        pass1=request.POST.get('U_pass')
        password=User.objects.values('U_pass').filter(U_name=name)
        print(password[0]['U_pass'])
        print(pass1)
        if pass1==password[0]['U_pass']:
            return HttpResponse("Welcome "+name)
        else:
            return HttpResponse("Wrong password!")
