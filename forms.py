from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class MyRegistrationForm(UserCreationForm):
	#email = forms.EmailField(required=True)
	#username = forms.RegexField(label=("Username"), max_length=30, regex=r'^[\w.@+-]+$', error_messages={'invalid': ("This value may contain only letters, numbers and @/./+/-/_ characters.")})
	#password1 = forms.CharField(label=("Password"), widget=forms.PasswordInput)
	#password2 = forms.CharField(label=("Password confirmation"), widget=forms.PasswordInput)
	#passkey = forms.CharField(label=("Tester Key"), widget=forms.PasswordInput)
	
	#email = forms.EmailField(required=True)
	#username = forms.RegexField(max_length=30, regex=r'^[\w.@+-]+$', error_messages={'invalid': ("This value may contain only letters, numbers and @/./+/-/_ characters.")})
	username = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder':'username', 'class':'loginInputs'}))
	email = forms.EmailField(label="", required=True, widget=forms.TextInput(attrs={'placeholder':'email', 'class':'loginInputs'}))
	password1 = forms.CharField(label="",  widget=forms.PasswordInput(attrs={'placeholder':'password', 'class':'loginInputs'}))
	password2 = forms.CharField(label="",  widget=forms.PasswordInput(attrs={'placeholder':'password confirmation', 'class':'loginInputs'}))
	passkey = forms.CharField(label="",  widget=forms.PasswordInput(attrs={'placeholder':'tester key', 'class':'loginInputs'}))
	
	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2')
		
	def save(self, commit=True):
		user = super(MyRegistrationForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		
		if commit:
			user.save()
			
		return user
