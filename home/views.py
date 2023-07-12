from django.shortcuts import render
from datetime import datetime
from home.models import users
# Create your views here.
def index(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        q=users(username=username,password=password,date=datetime.today())
        q.save()
    return render(request,'first.html')
