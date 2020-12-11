from django.db import models
import uuid

class SendEmailModel(models.Model):

    '''
    A catch all email model that can be used for 
    sending introductory emails, or promo emails
    from the admin interface.
    '''

    class Meta:
        verbose_name_plural = 'Send Emails'

    class Types(models.TextChoices):
        SENDSIGNUPCONFIRMATIONEMAIL = 'SENDSIGNUPCONFIRMATIONEMAIL', 'SendSignUpConfirmationEmail',
        SENDEMAILTOONECUSTOMERMODEL = 'SENDEMAILTOONECUSTOMERMODEL', 'SendEmailToOneCustomerModel',
        SENDEMAILTOMULTIPLECUSTOMERSMODEL = 'SENDEMAILTOMULTIPLECUSTOMERSMODEL', 'SendEmailToMultipleCustomersModel',

    name = models.CharField(
        max_length=255,
    )
    message = models.CharField(
        max_length=255,
    )
    promo = models.BooleanField(
        default=False,
    )
    promo_id = models.UUIDField(
        default = uuid.uuid4,
        editable = False
    )
    promo_name = models.CharField(
        max_length = 255,
    )
    # * the url needed to reach the promotional sale
    url = models.URLField(
        max_length = 255,
    )

class SendSignUpConfirmationEmail(SendEmailModel):
    '''
    Proxy Model: Meant to be used for sign up confirmation and two factor auth
    '''

    class Meta:
        verbose_name_plural = 'Send Sign Up Emails'
        proxy = True

class SendEmailToOneCustomerModel(SendEmailModel):
    '''
    Proxy Model: Meant to be sent to individual customers for marketing purpose.
    '''
    
    class Meta:
        verbose_name_plural = 'Send To One Customer Emails'
        proxy = True

class SendEmailToMultipleCustomersModel(SendEmailModel):
    '''
    Proxy Model: Meant to be sent to multiple customers for marketing purpose.
    '''
    
    class Meta:
        verbose_name_plural = 'Send to Multiple Customers Emails'
        proxy = True
