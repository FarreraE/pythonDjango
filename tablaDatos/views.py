from typing import List
from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from tablaDatos.models import UserData
from tablaDatos.forms import UserForm, LinkForm
# Create your views here.


def basicTemplate(request):
    if request.method == 'GET':

        #respuesta = f"Estoy buscando la camada nro: {request.GET['camada'] }"
        name = request.GET['name']
        findUser = UserData.objects.filter(name=name)

        return render(request, "basicTemplate.html", {"name": findUser, "surname": name})

    else:
        return HttpResponse("No enviaste datos")


def formProfile(request):

    if request.method == 'POST':

        # aquí mellega toda la información del html
        userForm = UserForm(request.POST)

        print(userForm)

        if userForm.is_valid:  # Si pasó la validación de Django

            dataFromForm = userForm.cleaned_data

            userNew = UserData()
            userNew.name = dataFromForm['name']
            userNew.surname = dataFromForm['surname']
            userNew.email = dataFromForm['email']
            userNew.password = dataFromForm['password']

            userNew.save()

        # Vuelvo al inicio o a donde quieran
            return render(request, "linkAdmin.html")

    else:
        userForm = UserForm()  # Formulario vacio para construir el html

    return render(request, "formProfile.html", {"formProfile": userForm})


def linkAdmin(request):
    return render(request, "linkAdmin.html")


def printProfile(request):
    userNew = UserData(name="hola", surname = "hola", email="hola", password ="123")
    userNew.save
    return render(request, "printProfile.html")


def printProfilelinkAdmin(request):
    return render(request, "printProfilelinkAdmin.html")


def printProfileBusqueda(request):
    return render(request, "printProfileBusqueda.html")


def logIn(request):
    print(request.POST)

    return render(request, "logIn.html")
