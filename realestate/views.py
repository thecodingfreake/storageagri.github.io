from django.shortcuts import render
from itertools import chain
from django.http import HttpResponse
from .models import *

# Create your views here.
def frontpage(request):
    return render(request,'frontpage.html')


def login(request):
    return render(request,'login.html')


def check(request):
    n1=request.POST['user']
    n2=request.POST['password']
    user=Users.objects.all().values()
    for i in user:
        if i['user']==n1 and i['password']==n2:
            return render(request,'mainpage.html')
    return render(request,'login.html')

area=''
def selection(request):
    n1=request.POST['place']
    n2=request.POST['type']
    print(n2)
    global area
    area=n1
    if n1=='Thanjavur' :
        option=Thanjavur.objects.filter(type=n2).values()
        return render(request,'thanjavur.html',{'values':option})
    if n1=='Sivangangai' :
        option=Sivangangai.objects.filter(type=n2).values()
        return render(request,'thanjavur.html',{'values':option})
    if n1=='Thiruvallur' :
        option=Thiruvallur.objects.filter(type=n2).values()
        return render(request,'thanjavur.html',{'values':option})

def register(request):
    user1=request.POST.get('username')
    password1=request.POST.get('password1')
    password2=request.POST.get('password2')
    print(user1,password1,password2)
    if password1 is not None:
        if password1==password2:
            user=Users(user=user1,password=password1)
            user.save()
            return render(request,'login.html')
    return render(request,'register.html')

def comment(request):
    name1=request.POST.get('name')
    email1=request.POST.get('email')
    number1=request.POST.get('number')
    comment1=request.POST.get('comment')
    if name1 is not None:
        user=Comments(name=name1,email=email1,number=number1,comment=comment1)
        user.save()
        return render(request,'frontpage.html')
    return render(request,'comments.html')


def about(request):
    user=Comments.objects.all()
    return render(request,'about.html',{'review':user})

def contact(request):
    name1=request.POST.get('name')
    email1=request.POST.get('email')
    number1=request.POST.get('number')
    comment1=request.POST.get('comment')
    if name1 is not None:
        user=Comments(name=name1,email=email1,number=number1,comment=comment1)
        user.save()
        return render(request,'frontpage.html')
    return render(request,'comments.html')


def viewproperty(request):
    id1=request.POST.get('property')
    id1=id1.split(',')
    if id1[1]=='Thanjavur':
        option=Thanjavur.objects.filter(id=int(id1[0])).values()
        print(option)
        return render(request,'viewproperty.html',{'option':option})
    elif id1[1]=='Sivagangai':
        option=Sivangangai.objects.filter(id=int(id1[0])).values()    
        print(option)
        return render(request,'viewproperty.html',{'option':option})
    elif id1[1]=='Thiruvallur':
        option=Thiruvallur.objects.filter(id=int(id1[0])).values()
        print(option)
        return render(request,'viewproperty.html',{'option':option})
    return render(request,'viewproperty.html')
    

def posts(request):
    name1=request.POST.get('name')
    email1=request.POST.get('email')
    number1=request.POST.get('number')
    image1=request.POST.get('image')
    date1=request.POST.get('date')
    type1=request.POST.get('shed type')
    location1=request.POST.get('location')
    area1=request.POST.get('area')
    address1=request.POST.get('address')
    if name1 is not None:
        if location1=='Thanjavur':        
            a=str(image1).find('d/')
            b=str(image1).find('/view')
            image1=str(image1)[a+2:b]
            user=Thanjavur(owner=name1,date=date1,type=type1,image=image1,address=address1,size=area1)
            user.save()
            return render(request,'frontpage.html')
        elif location1=='Thiruvallur':
            user=Thiruvallur(owner=name1,date=date1,type=type1,image=image1,address=address1,size=area1)
            user.save()
            return render(request,'frontpage.html')
        elif location1=='Sivagangai':
            user=Sivangangai(owner=name1,date=date1,type=type1,image=image1,address=address1,size=area1)
            user.save()
            return render(request,'frontpage.html')
    else:
        return render(request,'posting.html')
    

def open(request):
        option1=Thanjavur.objects.filter(type='open shed').values()
        option2=Sivangangai.objects.filter(type='open shed').values()
        option=Thiruvallur.objects.filter(type='open shed').values()
        option3=list(chain(option,option1,option2))
        return render(request,'thanjavur.html',{'values':option3})


def closed(request):
        option1=Thanjavur.objects.filter(type='closed shed').values()
        option2=Sivangangai.objects.filter(type='closed shed').values()
        option=Thiruvallur.objects.filter(type='closed shed').values()
        option3=list(chain(option,option1,option2))
        return render(request,'thanjavur.html',{'values':option3})


def cold(request):
        option1=Thanjavur.objects.filter(type='cold shed').values()
        option2=Sivangangai.objects.filter(type='cold shed').values()
        option=Thiruvallur.objects.filter(type='cold shed').values()
        option3=list(chain(option,option1,option2))
        return render(request,'thanjavur.html',{'values':option3})


def contact(request):
    name1=request.POST.get('name')
    email1=request.POST.get('email')
    number1=request.POST.get('number')
    message1=request.POST.get('message')
    if name1 is not None:
        user=Contacts(name=name1,email=email1,number=number1,message=message1)
        user.save()
        return render(request,'frontpage.html')
    return render(request,'contact.html')