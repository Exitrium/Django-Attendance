from django.http import HttpResponse
from django.shortcuts import render

from .models import Student


# Create your views here.

def index(request):
    all_studs = Student.objects.all()
    context = {'all_studs':all_studs}
    return render(request, 'StudentList/index.html', context)

def newpage(request):
    return HttpResponse('<h1>Katrina Estaño</h2>')

def studlist(request, stud_id):
    return HttpResponse('<h2> Student Details for:' + str(stud_id) + '</h2>')

