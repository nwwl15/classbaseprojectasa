from django.contrib import admin
from . models import userdetail,user_card_payment,KYC_verification,referral_logic,user_id

admin.site.register(userdetail)
admin.site.register(user_card_payment)
admin.site.register(referral_logic)
admin.site.register(user_id)
admin.site.register(KYC_verification)

