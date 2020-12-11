from django.contrib import admin
from .models import (ParfaitModel, CupcakesModel, CakeModel, PieModel, PurchaseModel)

admin.site.register(ParfaitModel)
admin.site.register(CupcakesModel)
admin.site.register(PieModel)
admin.site.register(CakeModel)
admin.site.register(PurchaseModel)

