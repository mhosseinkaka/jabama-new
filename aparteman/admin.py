from django.contrib import admin
from aparteman.models import Owner, User, Place, Rent

# Register your models here.
admin.site.register(Owner)
admin.site.register(User)
admin.site.register(Place)
admin.site.register(Rent)