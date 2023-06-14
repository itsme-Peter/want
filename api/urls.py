from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [

    path("all",views.list_created),
    path("auth/",obtain_auth_token),
    path("create",views.product_alt),
    path("<int:pk>/",views.product_detail),

    path("add",views.add),
]