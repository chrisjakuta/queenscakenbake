'''
Custom User model and Custom User Manager for the User model.
'''

# TODO: Remember to set the user permissions
# TODO: based on the boolean @property
# TODO: methods. For example, give access
# TODO: to blogs based on the is_blogger
# TODO: method of the User model.

from django.contrib import auth
from django.contrib.auth.models import AbstractUser, AnonymousUser, UserManager
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import PermissionDenied
from django.core.mail import send_mail
from django.db import models
from django.utils import timezone
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _
from django_s3_storage.storage import S3Storage

class CustomUserManager(UserManager):
    '''
    Creates a new User instance w/
    the given fields, provided they are
    valid.
    '''

    def create_user(self, username, email=None, password=None, user_photo=None, **extra_fields):
        if not username:
            raise ValueError('Users must have a username!')
        if not email:
            raise ValueError('Users must have an email!')

        user = self.model(
            username=username,
            email=self.normalize_email(email),
            user_photo=user_photo
        )

        user.set_password(password)
        user.save(using=self._db)
        return user


class CustomUser(AbstractUser):

    class Types(models.TextChoices):
        CONSUMER = 'CONSUMER', 'Consumer',
        CREATOR = 'CREATOR', 'Creator',

    base_type = Types.CONSUMER

    type = models.CharField(
        _('Type'),
        max_length=50,
        choices=Types.choices,
        default=base_type,
    )

    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_(
            'Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    email = models.EmailField(max_length=254)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    user_photo = models.ImageField()
    is_blogger = models.BooleanField(default=False)
    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    # will cause the models.E006 error, deprecated.
    # when used with the proceeding values, USERNAME_FIELD
    # and REQUIRED_FIELDS respectively.
    # EMAIL_FIELD = email

    def __unicode__(self):
        return self.username

    def __str__(self):
        return self.username

    def __repr__(self):
        return 'CustomUser(username= , email= , password= )'

    @property
    def active(self):
        return self.active

    @property
    def staff(self):
        return self.is_staff

    @property
    def admin(self):
        return self.is_admin

    @admin.setter
    def admin(self, value: bool):
        self.admin = value if value is bool else None

    @property
    def superuser(self):
        return self.is_superuser
    
    @superuser.setter
    def superuser(self, value: bool):
        self.superuser = value if value is bool else None

    @property
    def blogger(self):
        return self.is_blogger

    @blogger.setter
    def blogger(self, value: bool):
        self.is_blogger = value if value is bool else None

    @property
    def staff(self):
        return self.is_staff
    
    @staff.setter
    def staff(self, value : bool):
        self.is_staff = value if value is bool else None
        
class ConsumerManager(CustomUserManager):

    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=CustomUser.Types.CONSUMER)

class Consumer(CustomUser):

    base_type = CustomUser.Types.CONSUMER
    objects = ConsumerManager()

    class Meta:
        proxy = True

class CreatorManager(CustomUserManager):

    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=CustomUser.Types.CREATOR)

    def create_user(self, username, email=None, password=None, user_photo=None, **extra_fields):
        if not username:
            raise ValueError('Users must have a username!')
        if not email:
            raise ValueError('Users must have an email!')

        user = self.model(
            username=username,
            email=self.normalize_email(email),
            user_photo=user_photo
        )

        user.set_password(password)
        user.blogger(True)
        user.admin(True)
        user.save(using=self._db)
        return user

class Creator(CustomUser):

    base_type = CustomUser.Types.CREATOR
    objects = CreatorManager()

    class Meta:
        proxy = True
