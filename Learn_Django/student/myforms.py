from django import forms

class Registration(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    city = forms.CharField()
    student_class = forms.ChoiceField(choices=[(1, '1'),(2, '2'),(3, '3'),(4, '4'),(5, '5'),(6, '6'),(7, '7'),(8, '8'),(9, '9'),(10, '10'),(11, '11'),(12, '12')])

    def clean(self):
        cleaned_data = super().clean()

        name_value = cleaned_data.get('name')
        email_value = cleaned_data.get('email')

        if ('gandu' in name_value) or ('gandu' in email_value):
            self.add_error('name', 'Bad words are included!')

class LogIn(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'placeholder':'Pehchan bata apni...'}
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            # Can set any attribute of an element here
            attrs={'placeholder':'Chabi dalo tala kholo...'}))