from django.shortcuts import render

# Create your views here.
def posting(request):
    return render(request, 'posting.html')

def home(request):
    return render(request, 'home.html')