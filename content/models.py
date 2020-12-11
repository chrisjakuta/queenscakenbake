from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid
from django.utils import timezone

class PageModel(models.Model):

    class Meta:
        verbose_name_plural = 'Pages'
    
    class Types(models.TextChoices):
        LANDINGPAGE = 'LANDINGPAGE', 'LandingPage',
        PROFILEPAGE = 'PROFILEPAGE', 'ProfilePage',
        LOGINPAGE = 'LOGINPAGE', 'LoginPage',

    base_type = Types.LANDINGPAGE
    
    type = models.CharField(
        _('Type'),
        max_length=50,
        choices=Types.choices,
        default=base_type,
    )

    name = models.CharField(
        max_length=255,
        help_text='Should be used to identify each model, in case you decide to have additional models.'
    )
    header_text = models.CharField(
        max_length=255,
        verbose_name='header_text',
        help_text='The text that will display prominantly on the page.',
    )
    image = models.ImageField(
        verbose_name='image',
        name='image',
        width_field=None,
        height_field=None,
    )
    landing_page_text = models.CharField(
        verbose_name='secondary_text',
        max_length=255,
        help_text='Text for display on the page, underneath the header text',
    )
    product_section_header_text = models.CharField(
        verbose_name='product_section_header_text',
        max_length=255,
        help_text='The header text for the product section.'
    )
    product_section_text = models.CharField(
        verbose_name='product_section_text',
        max_length=255,
        help_text='The text that will display underneath the product section header text.'
    )

class LandingPageManager(models.Manager):

    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=PageModel.Types.LANDINGPAGE)

class LandingPageModel(PageModel):

    class Meta:
        proxy = True
        verbose_name_plural = 'Landing Pages'
    objects = LandingPageManager()

class ProfilePageManager(models.Manager):

    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=PageModel.Types.PROFILEPAGE)

class ProfilePageModel(PageModel):

    class Meta:
        proxy = True
        verbose_name_plural = 'Profile Pages'
    objects = ProfilePageManager()

# default = 'work-with-us %s' % timezone.now()

class LandingPageCollectDataModel(models.Model):

    id = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4,
        editable = False,
    )

    name = models.CharField(
        verbose_name='work-with-us',
        max_length=50,
        default='work-with-us %s' % timezone.now(),
    )
    full_name = models.CharField(
        verbose_name='Full Name',
        max_length=50,
    )
    email = models.EmailField(
        max_length=254,
    )
    user_message = models.CharField(
        verbose_name='message',
        max_length=255,
    )
    date_created = models.DateTimeField(
        auto_now_add=True,
    )
