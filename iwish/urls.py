from django.urls import path
from . import views

urlpatterns = [
    # path("",views.index,name="home"),
    path("portfolio",views.portfolio,name="porfolio"),
    path("try",views.trial),
    path("sign",views.sign),
    path("profile",views.profile),
    # path("portfolio/iq",views.projectOption),
]