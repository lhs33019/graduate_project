from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext

# Create your views here.
def handler404(request, exception, template_name="404.html"):
    response = render_to_response("404.html")
    response.status_code = 404
    return response

def blank(request):
    return render(request, 'blank.html')

def buttons(request):
    return render(request, 'buttons.html')

def cards(request):
    return render(request, 'cards.html')

def charts(request):
    return render(request, 'charts.html')

def forgot_password(request):
    return render(request, 'forgot-password.html')

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def posting(request):
    return render(request, 'posting.html')

def register(request):
    return render(request, 'register.html')

def tables(request):
    return render(request, 'tables.html')

def utilities_animation(request):
    return render(request, 'utilities-animation.html')

def utilities_border(request):
    return render(request, 'utilities-border.html')

def utilities_color(request):
    return render(request, 'utilities-color.html')

def utilities_other(request):
    return render(request, 'utilities-other.html')

def logout(request):
    return render(request, 'login.html')

def get404(request):
    return render(request, '404.html')