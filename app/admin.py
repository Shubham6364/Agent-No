from django.contrib import admin
from . models import Test
from .models import Salepost
from . models import Rentpost


# Register your models here.

admin.site.register(Test)
admin.site.register(Salepost)
admin.site.register(Rentpost)


