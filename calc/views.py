from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html',{'name':'Nataraj'})

def add(request):
    if request.method == 'POST':
        # Handle the form data (for example, adding two numbers)
        num1 = int(request.POST.get('num1'))
        num2 = int(request.POST.get('num2'))
        result = num1 + num2
        return HttpResponse(f"The result is {result}")
    else:
        return HttpResponse("Invalid request method.")