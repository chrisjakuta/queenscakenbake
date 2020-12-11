from django.contrib import admin
from .models import (
    LandingPageModel,
    ProfilePageModel,
    LandingPageCollectDataModel,
)

admin.site.register(LandingPageModel)
admin.site.register(ProfilePageModel)
admin.site.register(LandingPageCollectDataModel)
