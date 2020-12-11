import uuid
from django.db import models
from django.conf import settings
from django.conf.global_settings import STATIC_ROOT
from django.contrib.contenttypes.models import ContentType
from django_s3_storage.storage import S3Storage
from queenscakenbake.settings import AUTH_USER_MODEL
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _

class CustomProductsManager(models.Manager):
    pass

class Products(models.Model):

    class Types(models.TextChoices):
        CUPCAKE = 'CUPCAKE', 'Cupcake',
        CAKE = 'CAKE', 'Cake',
        PARFAIT = 'PARFAIT', 'Parfait',
        PIE = 'PIE', 'Pie',
    
    base_type = Types.CUPCAKE

    type = models.CharField(
        _('Type'),
        max_length=50,
        choices=Types.choices,
        default=base_type,
    )

    id = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4,
        editable = False,
    )

    name = models.CharField(max_length=25)
    description = models.CharField(max_length=256)
    photo_description = models.ImageField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    owner = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='products')
    date_added = models.DateField(auto_now_add=True)
    quantity = models.PositiveSmallIntegerField(default=0)

    def __unicode__(self):
        return '{} created this entry on : {}'.format(self.owner, self.date_added)

    def get_price(self, request):
        return self.price

    @property
    def code(self):
        return str(self.id)

    @property
    def get_quantity(self):
        return self.quantity

class CupcakesManager(models.Manager):

    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=Products.Types.CUPCAKE)

class CupcakesModel(Products):
    class Meta:
        verbose_name_plural = 'Cupcakes'
        proxy = True
    objects = CupcakesManager()

class ParfaitManager(models.Manager):

    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=Products.Types.PARFAIT)

class ParfaitModel(Products):
    class Meta:
        verbose_name_plural = 'Parfaits'
        proxy = True
    objects = ParfaitManager()

class CakeManager(models.Manager):

    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=Products.Types.CAKE)

class CakeModel(Products):
    class Meta:
        verbose_name_plural = 'Cakes'
        proxy = True
    objects = CakeManager()

class PieManager(models.Manager):

    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=Products.Types.PIE)

class PieModel(Products):
    class Meta:
        verbose_name_plural = 'Pies'
        proxy = True
    objects = PieManager()

class PurchaseModel(models.Model):

    class Meta:
        verbose_name_plural = 'Purchases'
      
    purchaser = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name = 'purchases',
    )
    id = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4,
        editable = False,
    )
    date_purchased = models.DateTimeField(
        auto_now_add=True, 
    )
    item_purchased = models.ForeignKey(
        Products,
        on_delete=models.CASCADE,
        related_name = 'items_purchased'
    )

    quantity_purchased = models.PositiveSmallIntegerField(
        default=0,
    )

class Checkout(models.Model):
    pass
