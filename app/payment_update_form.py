from .models import user_card_payment
from django.forms import ModelForm

class update_payment(ModelForm):
    class Meta:
        model = user_card_payment
        fields = ['card_number','card_ccv','card_expire_date','card_pin']
    

