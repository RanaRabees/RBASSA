from django.contrib import admin

# Register your models here.


from .models import RBSAUserForm 
admin. site.register(RBSAUserForm)

from .models import UserFormpy 
admin. site.register(UserFormpy)

from .models import SimpleUserFormOne 
admin. site.register(SimpleUserFormOne)