from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone
from django.core.validators import RegexValidator
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from .managers import CustomUserManager

class CustomUser(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(_("Email address"), max_length=254,unique=True)
    firstname = models.CharField(_("First Name"),max_length=60)
    lastname = models.CharField(_("Last Name"),max_length=60)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message=_("Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."))
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    # notice the absence of a "Password field", that is built in.

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] # Email & Password are required by default.

    def get_full_name(self):
        # The user is identified by their email address
        return "{} {}".format(self.firstname,self.lastname)

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
    
    objects = CustomUserManager()