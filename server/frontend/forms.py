from django import forms
from django.forms import ModelForm, Textarea, TextInput, EmailInput
from .models import Contact


class ContactForm(ModelForm):

    class Meta:
        model = Contact
        fields = ['first_name', 'email_address', 'city', 'phone', 'category', 'message', 'file']


        widgets = {
            'first_name': TextInput(attrs={'class': 'contact-field',
                                           'autocomplete': 'off',
                                           'style': 'height: 35px',
                                           'required': True}),

            'email_address': EmailInput(attrs={'class': 'contact-field',
                                               'autocomplete': 'on',
                                               'style': 'height: 35px',
                                               'required': True}),

            'city': TextInput(attrs={'class': 'contact-field',
                                     'autocomplete': 'off',
                                     'style': 'height: 35px',
                                      'required': True}),

            'phone': TextInput(attrs={'class': 'contact-field',
                                      'type': 'tel',
                                      'pattern': '^[\\d() +-]+$',
                                      'minlength': '6',
                                      'title': 'Пример: 79501234567',
                                      'autocomplete': 'off',
                                      'style': 'height: 35px',
                                      'required': False}),


            'message': Textarea(attrs={'class': 'contact-field textarea',
                                       'autocomplete': 'off',
                                       'style': 'height: 150px',
                                       'required': False}),

            'category': forms.RadioSelect()

        }


        file = forms.FileField(
            label='Select a file',
            help_text='max. 42 megabytes'
        )