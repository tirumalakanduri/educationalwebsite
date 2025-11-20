from django import forms
from educationalapplication.models import Registration, Contactreg



class  ParentregForm(forms.ModelForm):
    class Meta : 
        model = Registration
        fields = "__all__"

class ContactregForm(forms.ModelForm):
    class Meta:
        model = Contactreg
        fields = "__all__"



