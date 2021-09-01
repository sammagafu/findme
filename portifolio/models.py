from django.db import models
from django.utils.translation import ugettext as _
from django_quill.fields import QuillField
from django.utils.text import slugify
from django.conf import settings
from django.urls import reverse
from django.utils import timezone




# Create your models here.
class Portfolio(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("owner"), on_delete=models.CASCADE,blank=True,null=True)
    title = models.CharField(max_length=130)
    cover = models.ImageField(upload_to="covers",help_text="image should be squared")
    slug = models.SlugField(editable=False,unique=True)
    content = QuillField()
    created_at = models.DateTimeField(default=timezone.now)
    views = models.IntegerField(editable=False,default=0)

    class Meta:
        verbose_name = _("Portfolio")
        verbose_name_plural = _("Portfolios")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("portifolio:detail", kwargs={"slug": self.slug})

    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Portfolio,self).save(*args, **kwargs)
