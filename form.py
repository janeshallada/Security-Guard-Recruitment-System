from django import forms
from .models import Guards

class Guard_form(forms.ModelForm):
    class Meta:
        model=Guards
        fields=("user1","guardname","firstname","lastname","email","mobileno","age","gender","idtype","idnumber","qualification","pic","address","passphoto","status","remark","level","rlevel")

