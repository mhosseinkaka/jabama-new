from django.contrib import admin
from aparteman.models import Owner, Place, Rent

# Register your models here.
admin.site.register(Owner)
admin.site.register(Place)
admin.site.register(Rent)