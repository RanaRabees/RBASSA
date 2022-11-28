from django.http import HttpResponse
from django.shortcuts import render
from . import views
from BlackHole.models import RBSAUserForm
from BlackHole.models import UserFormpy
from BlackHole.models import SimpleUserFormOne

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_even(value):
    if value % 2 != 0:
        raise ValidationError(
            _('%(value)s is not an even number'),
            params={'value': value},
        )

# Create your views here.

def home(request):
    return render(request, 'home.html')


def contact(request):
    return render(request, 'contact.html')


def form(request):
    
    d = ""
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        age = request.POST.get('age')
        data = SimpleUserFormOne(
            name=name,
            email=email,
            password=password,
            age=age,
        )
    data.save()
    print(data)
    import json
    User_data = {
        'name': name,
        'email': email,
        'password': password,
        'age': age,
    }
    with open('User_Simple_Data.json', 'a') as d:
        json.dump(User_data, d, indent=4)
    d = "Good Luck 👻 Bro Your Data Has Been Sent Succefully"
    return render(request, 'fullview.html', {
        'd': d,
        'name': name,
        'email': email,
        'password': password,
        'age': age,
    })


def formpy(request):
    # def validate_even(value):
    #     if value % 2 != 0:
    #         raise ValidationError(
    #         _('%(value)s is not an even number'),
    #         params={'value': value},
    #     )
    d = ""
    if request.method == 'POST':        
        name = request.POST.get('name')
        father_name = request.POST.get('father_name')
        age = request.POST.get('age')
        password = request.POST.get('password')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        about_you = request.POST.get('about_you')
        user_image = request.FILES.get('user_image')
        DOB = request.POST.get('DOB')
        data = UserFormpy(
            name=name,
            father_name=father_name,
            age=age,
            password=password,
            email=email,
            gender=gender,
            about_you=about_you,
            user_image=user_image,
            DOB=DOB,
        )
    data.save()
    print(data)
    import json
    User_data = {
        'name': name,
        'father_name': father_name,
        'age': age,
        'password': password,
        'email': email,
        'gender': gender,
        'about_you': about_you,
        'user_image':  None,
        'DOB': DOB,
    }
    with open('User_Data_Forms.json', 'a') as d:
        json.dump(User_data, d, indent=4)
    d = "Good Luck 👻 Bro Your Data Has Been Sent Succefully"
    return render(request, 'formpy.html', {
        'd': d,
        'name': name,
        'father_name': father_name,
        'age': age,
        'password': password,
        'email': email,
        'gender': gender,
        'about_you': about_you,
        'user_image': user_image,
        'DOB': DOB,
    })


def index(request):
    d = ""
    if request.method == 'POST':
        name = request.POST.get('name')
        father_name = request.POST.get('father_name')
        age = request.POST.get('age')
        howmany = request.POST.get('howmany')
        cardnumber = request.POST.get('cardnumber')
        password = request.POST.get('password')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        about_you = request.POST.get('about_you')
        user_image = request.FILES.get('user_image')
        DOB = request.POST.get('DOB')
        data = RBSAUserForm(
            name=name,
            father_name=father_name,
            age=age,
            howmany=howmany,
            cardnumber=cardnumber,
            password=password,
            email=email,
            gender=gender,
            about_you=about_you,
            user_image=user_image,
            DOB=DOB,
        )
    data.save()
    print(data)
    import json
    User_data = {
        'name': name,
        'father_name': father_name,
        'age': age,
        'howmany': howmany,
        'cardnumber': cardnumber,
        'password': password,
        'email': email,
        'gender': gender,
        'about_you': about_you,
        'user_image':  None,
        'DOB': DOB,
    }
    with open('User_Data.json', 'a') as d:
        json.dump(User_data, d, indent=4)
    d = "Good Luck 👻 Bro Your Data Has Been Sent Succefully"
    return render(request, 'index.html', {
        'd': d,
        'name': name,
        'father_name': father_name,
        'age': age,
        'howmany': howmany,
        'cardnumber': cardnumber,
        'password': password,
        'email': email,
        'gender': gender,
        'about_you': about_you,
        'user_image': user_image,
        'DOB': DOB,
    })

def fullview(request):   
    return render(request, 'fullview.html')