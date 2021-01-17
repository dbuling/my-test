from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"home.html")

def user(request):
    return render(request,"user.html")

def support(request):
    return render(request,"support.html")

def exhibition(request):
    return render(request,"exhibition.html")

def news(request):
    return render(request,"news.html")

def education(request):
    return render(request,"education.html")

def logout(request):
    request.session.flush()
    return redirect('home.html')
