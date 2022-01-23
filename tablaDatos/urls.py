from django.urls import path

from tablaDatos import views

urlpatterns = [

    path('', views.basicTemplate),  # esta era nuestra primer view
    path('formProfile', views.formProfile, name="settingsProfile"),
    path('logIn', views.logIn, name="logIn"),
    path('linkAdmin/', views.linkAdmin, name="linkAdmin"),
    path('printProfile/', views.printProfile, name="printProfile"),
    path('printProfilelinkAdmin/', views.printProfilelinkAdmin,
         name="printProfilelinkAdmin"),
    path('printProfileBusqueda/', views.printProfileBusqueda,
         name="printProfileBusqueda"),
     path("buscarNombre/", views.buscarNombre)


]
