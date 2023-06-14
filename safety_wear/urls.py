from django.urls import path
from . import views

urlpatterns = [
    path("home",views.index),
    path("",views.index),
    path("products",views.productsPage),
    path("all",views.allProducts),
    path("randoms",views.randoms),
    path("feedback",views.feedback),
    path("category/<str:name>/",views.by),
    path("product/<int:pk>/",views.product),
    path("product/<str:name>/",views.theProduct),
    
]