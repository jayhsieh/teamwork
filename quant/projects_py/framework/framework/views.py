from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def dwarf_home(request):
    return render(request, 'index.html')
    #return HttpResponse("dwarf_home")