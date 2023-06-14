from django.shortcuts import render

def index(request):

    context ={
        
    }
    return render(request,"index.html",context)

def portfolio(request):

    context = {

    }
    return render(request,"portfolio.html",context)

def sign(request):

    return render(request,"sign.html")

def trial(request):

    return render(request,"try.html")

def profile(request):

    return render(request,"profile.html")