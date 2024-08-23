from index.models import Contact
from django.forms import ModelForm
from captcha.fields import CaptchaField



class ContactForm(ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Contact
        fields  = '__all__'