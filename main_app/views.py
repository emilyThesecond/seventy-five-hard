from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def diet(request):
    return render(request, 'diet.html')

def gallery(request):
    return render(request, 'gallery.html')

def rules(request):
    return render(request, 'rules.html')
