from django import forms
from .views import Posts

class UserForm(forms.Form):
    name = forms.CharField(required=False,min_length=5,max_length=15,label='Ваше имя',help_text='adsad',widget=forms.TextInput(attrs={'class': 'myClass',"placeholder":'Name'}))
    age = forms.IntegerField(min_value=1,max_value=100,widget=forms.NumberInput(attrs={'class': 'myClass','value':52}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'myClass'}))
    # required_css_class = 'myClass'

class UserLogin(forms.Form):
    name = forms.CharField(label='Имя',widget=forms.TextInput(attrs={'placeholder':"Имя"}), required=False)
    email = forms.EmailField(label='Почта',widget=forms.EmailInput(attrs={'placeholder':"Почта"}),required=False)
    password = forms.CharField(label='Пароль',widget=forms.TextInput(attrs={'placeholder': 'Пароль'}),required=False)

class AddPost(forms.ModelForm):
    model = Posts
    field = '__all__'
