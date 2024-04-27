from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import provider,Register,Hotel,Services,Places,ProvPlaces,Provservices
# Register your models here.

admin.site.register(provider)
admin.site.register(Register)
admin.site.register(Hotel)
admin.site.register(Services)
admin.site.register(Places)
admin.site.register(ProvPlaces)
admin.site.register(Provservices)


