from django import forms
from .models import Course
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class AddCourse(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        # self.helper.form_action = ''
        # self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit', 'Add Course'))

    class Meta:
        model = Course
        fields = ['course_name', 'stu_class']
        