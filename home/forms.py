from django import forms
from django.template.loader import render_to_string
from .email_thread import EmailThread
from .utils import cleaned_field

class ContactForm(forms.Form):

    name = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={
            'class': 'input-box',
            'placeholder': 'votre nom',
            'name': "name",
        }))
    email = forms.EmailField(max_length=60, widget=forms.EmailInput(
        attrs={
            'class': 'input-box',
            'placeholder': 'votre email',
            'name': 'email',
        }
    ))
    cellphone = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class': 'input-box',
        'placeholder': 'votre téléphone',
        'name': 'cellphone',
    }))
    content = forms.CharField(max_length=500, widget=forms.Textarea(
        attrs={
            'class': 'input-box',
            'placeholder': 'message',
            'name': 'content',
        }
    ))
    subject = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={

            'class': 'input-box',
            'placeholder': 'sujet ',
            'name': 'subject',
        }))

    def send_email(self):
        fields_value = cleaned_field(self)
        html = render_to_string('home/components/contact_form.html', {**fields_value})
        email_thread = EmailThread(fields_value.get('subject'), fields_value.get('content'), fields_value.get('email'), html, [
                                   'danidkm242@gmail.com'])
        email_thread.start()
        email_thread.join()
        return email_thread.status


class ApplyingForm(forms.Form): 
    civility = [
        ('Mrs', 'Mrs'),
        ('Mme', 'Mme'), 
        ]
        
     
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={
            'class': 'input-box',
            'placeholder': 'votre nom',
            'name': "name",
        }))
    email = forms.EmailField(max_length=60, widget=forms.EmailInput(
        attrs={
            'class': 'input-box',
            'placeholder': 'votre email',
            'name': 'email',
        }
    ))
    cellphone = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class': 'input-box',
        'placeholder': 'Tel (ex : 064649019) ',
        'name': 'cellphone',
    }))
    content = forms.CharField(max_length=500, widget=forms.Textarea(
        attrs={
            'class': 'input-box',
            'name': 'content',
            'placeholder': 'votre message',
        }
    ))
  
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={
            'class': 'input-box',
            'placeholder': 'votre prenom',
            'name': "name",
        }))
    
    cv  = forms.FileField();

  
    def send_email(self, file, offer_post):
        fields_value = cleaned_field(self)
        html = render_to_string('home/components/offer_applying.html', {**fields_value, 'post': offer_post})
        email_thread = EmailThread(fields_value.get('offer'), fields_value.get('content'), fields_value.get('email'), html, [
                                   'danidkm242@gmail.com'], (file.name , file.read(), file.content_type))
        email_thread.start()
        email_thread.join()
        return email_thread.status
