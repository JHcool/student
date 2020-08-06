from django import forms

class PostForm(forms.Form):
    cName = forms.CharField(max_length=20, initial='')
    cSex = forms.CharField(max_length=2, initial='M')
    cBirthday = forms.DateField()
    cEmail = forms.EmailField(max_length=100, required=False, initial='')
    cPhone = forms.CharField(max_length=50, required=False, initial='')
    cAddr = forms.CharField(max_length=255, required=False, initial='')