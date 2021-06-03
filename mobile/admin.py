from django.contrib import admin
from mobile.models import Brand,Product


# Register your models here.
admin.site.register(Brand)
admin.site.register(Product)

#create superuser
# python manage.py create superuser
