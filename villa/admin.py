from django.contrib import admin
from villa.models import User, Owner, Villa, Rent


admin.site.register(Owner)
admin.site.register(Villa)
admin.site.register(Rent)
