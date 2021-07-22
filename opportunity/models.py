from dashboard.models import Industry
from django.db import models
from django.utils.translation import gettext as _
from dashboard.models import Industry,Category
from django.urls import reverse
from django.utils.text import slugify
from django.conf import settings

# models import


# Create your models here.

class Opportunity(models.Model):
    advertiser = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("advister"), on_delete=models.CASCADE)
    title = models.CharField(_("title"), max_length=50)
    slug = models.SlugField(_("slug"),editable=False)
    description = models.TextField()
    created_date  = models.DateTimeField(auto_now_add=True)
    start_date = models.DateField(_("Start Date"), auto_now=False, auto_now_add=False)
    end_date = models.DateField(_("End Date"), auto_now=False, auto_now_add=False)
    category = models.ManyToManyField(Category,null=True,blank=True)
    industry = models.ManyToManyField(Industry,null=True,blank=True)
    budjet = models.FloatField(default=100000)
    is_negotiatable = models.BooleanField(default=False,verbose_name=_("Open for Negotiations"))
    is_active = models.BooleanField(_("Is_active"),default=True)
    

    class Meta:
        verbose_name = 'Opportunity'
        verbose_name_plural = 'Opportunities'

    def __str__(self):
        return self.title

    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Opportunity, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('job:detail', kwargs={'slug': self.slug})