from django.contrib import admin
from .models import (
    SendEmailModel,
    SendEmailToMultipleCustomersModel,
    SendEmailToOneCustomerModel,
    SendSignUpConfirmationEmail,
)

admin.site.register(SendEmailModel)
admin.site.register(SendEmailToMultipleCustomersModel)
admin.site.register(SendEmailToOneCustomerModel)
admin.site.register(SendSignUpConfirmationEmail)
