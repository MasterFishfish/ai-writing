from django.contrib import admin

# Register your models here.
from loginPages.models import user, userInformation

admin.site.register(user)
admin.site.register(userInformation)