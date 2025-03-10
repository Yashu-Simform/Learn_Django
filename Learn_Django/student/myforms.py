from django import forms
from django.core import validators
import os
import json

class Registration(forms.Form):
    name = forms.CharField(
        required=True,
        error_messages={'required': 'Name is required!'}
    )
    email = forms.EmailField(
        required=True,
        error_messages={'required': 'Email kon dalega!'}
    )
    password = forms.CharField(
        required=True,
        help_text='Password must contain at least one special character [!, @, #, $, ...]',
        widget=forms.PasswordInput(
            # Can set any attribute of an element here
            render_value=True,
            attrs={'placeholder':'Apke tale ki chabi dijiye...'}))
    city = forms.CharField(
        required=True,
        error_messages={'required': 'city to dal pehle!'}
    )

    stu_class = forms.ChoiceField(choices=[(1, '1'),(2, '2'),(3, '3'),(4, '4'),(5, '5'),(6, '6'),(7, '7'),(8, '8'),(9, '9'),(10, '10'),(11, '11'),(12, '12')])


    def clean_password(self):
        cleaned_password = self.cleaned_data['password']

        special_characters = [
            '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',
            ':', ';', '<', '=', '>', '?', '@', '[', ']', '^', '_', '`', '{', '|', '}', '~'
        ]

        flag = False
        for c in special_characters:
            if c in cleaned_password:
                flag = True
                break

        if not flag:
            raise forms.ValidationError('InValid password!, Password must contain at least 1 special character.')

        return cleaned_password

    
    #   Custom Validation for whole form
    # def clean(self):
    #     cleaned_data = super().clean()

    #     name_value = cleaned_data.get('name')
    #     email_value = cleaned_data.get('email')

    #     if name_value is None:
    #         pass

    #     if ('gandu' in name_value) or ('gandu' in email_value):
    #         self.add_error('name', 'Bad words are included!')

    #     return cleaned_data

class LogIn(forms.Form):
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
    
    #   Custom validation for an individual form field
    def clean_password(self):
        cleaned_password = self.cleaned_data['password']

        special_characters = [
            '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',
            ':', ';', '<', '=', '>', '?', '@', '[', ']', '^', '_', '`', '{', '|', '}', '~'
        ]

        flag = False
        for c in special_characters:
            if c in cleaned_password:
                flag = True
                break

        if not flag:
            raise forms.ValidationError('InValid password!, Password must contain at least 1 special character.')

        return cleaned_password
        



class RegistrationFile(forms.Form):
    data_file = forms.FileField()

    def clean_data_file(self):
        cleaned_data_file = self.cleaned_data.get('data_file')
        print(cleaned_data_file)

        if not cleaned_data_file:
            print('Not a file')
            raise forms.ValidationError('Select a valid file!')

        extension = os.path.splitext(cleaned_data_file.name)[-1].lower()

        if extension != '.json':
            print('not json file')
            raise forms.ValidationError('Not a json file')
        
        return cleaned_data_file