from django.contrib import admin
# from .models import related models


# Register your models here.

# CarModelInline class

# CarModelAdmin class

# CarMakeAdmin class with CarModelInline

# Register models here
from django.contrib import admin


from django.contrib import admin
from .models import CarMake, CarModel


# Register your models here.
admin.site.register(CarMake)

admin.site.register(CarModel)


# CarModelInline class

class CarModelInline:
    pass


# CarModelAdmin class

# CarMakeAdmin class with CarModelInline

# Register models here
