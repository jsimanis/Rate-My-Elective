from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from website.models import Review
from website.models import Contact, Course, Department

from django.contrib.auth import get_user_model

User = get_user_model()



'''
Custom implementation for the AuthenticationForm
All other methods/attributes are inherited.
The specified methods/attributes override AuthenticationForm
'''
class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': '',
            'id': 'username'
        }))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': '',
            'id': 'password',
        }))


'''
Custom implementation for the UserCreationForm
All other methods/attributes are inherited.
The specified methods/attributes override UserCreationForm
'''
class UserRegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '',
            'id': 'username'
        }))
    email = forms.EmailField(
        label="Email",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '',
            'id': 'email'
        }))
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': '',
            'id': 'password',
        }))
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': '',
            'id': 'password_confirm',
        }))
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class ReviewForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
      super(ReviewForm, self).__init__(*args, **kwargs)

    year_taken = forms.CharField(
      label="Year Taken",
      widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': '',
        'id': 'year'
      })
    )
    content = forms.CharField(
      label="Content",
      widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': '',
        'id': 'content'
      })
    )

    class Meta:
      model = Review
      fields = ["author", "course", "year_taken", "content"]

class ContactForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)

    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': '',
            'id': 'name'
        }))
    email = forms.EmailField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': '',
            'id': 'email',
        }))
    query = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'placeholder': '',
            'id': 'query',
        }))
    class Meta:
      model = Contact
      fields = ["name", "email", "query"]

class AddClassForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AddClassForm, self).__init__(*args, **kwargs)
        self.fields['department'].widget.attrs.update({'class': 'form-control'})
        self.fields['course_number'].widget.attrs.update({'class': 'form-control'})


    department = forms.ModelChoiceField(Department.objects.all())
    course_number = forms.IntegerField(min_value = 100, max_value=499)
    
    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': '',
            'id': 'name'
        }))

    description = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'placeholder': '',
            'id': 'query',
        }))
    class Meta:
      model = Course
      fields = [ "department", "course_number","name", "description"]

class AddDeptForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AddDeptForm, self).__init__(*args, **kwargs)

    code = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': '',
            'id': 'name'
        }))
    
    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': '',
            'id': 'name'
        }))

    class Meta:
      model = Department
      fields = [ "code", "name"]



