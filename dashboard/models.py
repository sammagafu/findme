from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
class Category(models.Model):
    category = models.CharField(_("Category Name"), max_length=100)
    icon = models.ImageField(_("Avatar"), upload_to="category/", height_field=None, width_field=None, max_length=None)
    description = models.TextField()

    def __str__(self):
        return self.category


class Industry(models.Model):
    industry = models.CharField(_("Industry Name"), max_length=100)
    icon = models.ImageField(_("Avatar"), upload_to="Industry/", height_field=None, width_field=None, max_length=None)
    description = models.TextField()

    def __str__(self):
        return self.industry

