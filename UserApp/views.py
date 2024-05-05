from django.shortcuts import render
from AdminApp.models import Category,Cake

# Create your views here.
def homepage(request):
    cats = Category.objects.all()
    cake = Cake.objects.all()
    return render(request,"master.html",{"cats":cats,"Cake":cake})

