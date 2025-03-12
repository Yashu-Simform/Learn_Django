from django import forms
from crispy_forms.helper import FormHelper
from .models import TeacherProfile
from crispy_forms.layout import Submit

class TeacherRegistration(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        # self.helper.form_action = ''
        # self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit', 'Submit'))

    class Meta:
        model = TeacherProfile
        fields = ['name', 'email', 'mobile_number', 'address', 'specialization']