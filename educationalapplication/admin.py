from django.contrib import admin
from educationalapplication.models import Registration, Contactreg

# Create a separate ModelAdmin class
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ['rname', 'rphone', 'remail', 'rstudentname', 'rmessage']

class ContactregAdmin(admin.ModelAdmin):
    list_display = ['cname', 'cphone', 'cemail', 'cmessage']

# Register the model with its admin class
admin.site.register(Registration, RegistrationAdmin)
admin.site.register(Contactreg, ContactregAdmin)
