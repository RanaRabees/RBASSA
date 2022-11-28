from .models import UserFormpy
class UserFormpy(UserFormpy.ModelForm):
    
    class Meta:
        model = 'name','father_name','age','password','email','gender','about_you','user_image','DOB'
        fields = ("CharField,""TextField","FileField","DateField")

