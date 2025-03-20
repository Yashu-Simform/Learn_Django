from django import forms
from crispy_forms.helper import FormHelper
from .models import TeacherProfile
from crispy_forms.layout import Submit
from django.contrib.auth.models import User

class TeacherRegistration(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        # self.helper.form_action = ''
        # self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit', 'Submit'))

    class Meta:
        model = TeacherProfile
        fields = ['name', 'email', 'mobile_number', 'address', 'specialization', 'password']


class TeacherLogin(forms.ModelForm):

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'placeholder':'Pehchan bata apni...'}
        ),
        error_messages={'required': 'Email kon dalega!'},
    )
    
    password = forms.CharField(
        help_text='Password must contain at least one special character [!, @, #, $, ...]',
        widget=forms.PasswordInput(
            # Can set any attribute of an element here
            attrs={'placeholder':'Chabi dalo tala kholo...'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        # self.helper.form_action = ''
        # self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit', 'Submit'))

    class Meta:
        model = User
        fields = ['email', 'password']