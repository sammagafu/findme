from dashboard.models import Industry
from django.db import models
from django.utils.translation import gettext as _
from dashboard.models import Industry,Category
from django.urls import reverse
from django.utils.text import slugify
from django.conf import settings
from django.utils import timezone

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
    is_active = models.BooleanField(_("Active / ready"),default=True)
    is_saved = models.BooleanField(_("archived"),default=False,editable=False)
    

    class Meta:
        verbose_name = 'Opportunity'
        verbose_name_plural = 'Opportunities'

    def __str__(self):
        return self.title

    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Opportunity, self).save(*args, **kwargs)

    def job_is_active(self):
        return self.is_active

    def get_absolute_url(self):
        return reverse('opportunity:detail', kwargs={'slug': self.slug})


class AppliedJob(models.Model):
    job = models.ForeignKey(Opportunity, verbose_name=_("Opportunity"), on_delete=models.CASCADE)
    applying = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("Person Applying"), on_delete=models.CASCADE)
    applied = models.BooleanField(verbose_name="Applied",default=True)
    applied_date = models.DateField(_("Start Date"),default=timezone.now())

    class Meta:
        """Meta definition for MODELNAME."""

        verbose_name = 'Applied Job'
        verbose_name_plural = 'Applied Jobs'

class SavedJob(models.Model):
    job = models.ForeignKey(Opportunity, verbose_name=_("Opportunity"), on_delete=models.CASCADE)
    saving = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("Person Applying"), on_delete=models.CASCADE)
    is_saved = models.BooleanField(verbose_name="Applied",default=True)
    saved_date = models.DateField(_("Start Date"),default=timezone.now())

