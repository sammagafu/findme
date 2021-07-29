from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone
from django.core.validators import RegexValidator
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from .managers import CustomUserManager
# other models
from django.conf import settings
from dashboard.models import Category,Industry
from django.urls import reverse
# signals
from django.db.models.signals import post_save
from django.dispatch import receiver


class CustomUser(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(_("Email address"), max_length=254,unique=True)
    firstname = models.CharField(_("First Name"),max_length=60)
    lastname = models.CharField(_("Last Name"),max_length=60)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message=_("Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."))
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
    is_staff = models.BooleanField(default=False)
    is_freelance = models.BooleanField(default=False)
    is_business = models.BooleanField(default=False)
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


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    avatar = models.ImageField(_("Avatar"), upload_to='profile/', height_field=None, width_field=None, max_length=None,default="candidate-1.png")
    bio = models.TextField(max_length=500, blank=True)
    field = models.ManyToManyField(Category)
    linkedin = models.URLField(verbose_name="Linkedin Link", max_length=200,blank=True,null=True)
    facebook = models.URLField(verbose_name="Facebook Link", max_length=200,blank=True,null=True)
    twitter = models.URLField(verbose_name="Twitter Link", max_length=200,blank=True,null=True)
    instagram = models.URLField(verbose_name="Instagram Link", max_length=200,blank=True,null=True)
    behance = models.URLField(verbose_name="Behance Link", max_length=200,blank=True,null=True)

@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class CompanyProfile(models.Model):
    owner = models.OneToOneField(settings.AUTH_USER_MODEL, verbose_name=_("advister"), on_delete=models.CASCADE)
    company = models.CharField(_("Company name"), max_length=50)
    industry = models.ForeignKey(Industry, on_delete=models.CASCADE,null=True)
    about = models.TextField()
    city = models.CharField(_("City"), max_length=50)
    country = models.CharField(_("Country"), max_length=50)
    avatar = models.ImageField(_("Company Logo"), upload_to='company/logo/', height_field=None, width_field=None, max_length=None)
    website = models.URLField(verbose_name="Linkedin Link", max_length=200,blank=True,null=True)
    linkedin = models.URLField(verbose_name="Linkedin Link", max_length=200,blank=True,null=True)
    facebook = models.URLField(verbose_name="Linkedin Link", max_length=200,blank=True,null=True)
    twitter = models.URLField(verbose_name="Linkedin Link", max_length=200,blank=True,null=True)
    instagram = models.URLField(verbose_name="Linkedin Link", max_length=200,blank=True,null=True)
    office_email = models.EmailField(_("Company Email"), max_length=254,blank=True,null=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message=_("Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."))
    phone_number = models.CharField(_("Company Phone"),validators=[phone_regex], max_length=17, blank=True)

    class Meta:
        """Meta definition for CompanyProfile."""

        verbose_name = 'Company Profile'
        verbose_name_plural = 'Company Profiles'

    def __str__(self):
        return self.company

    def get_absolute_url(self):
        """Return absolute url for CompanyProfile."""
        return ('')
