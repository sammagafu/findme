from django.db import models
from django.utils.translation import ugettext as _

# Create your models here.
class Portfolio(models.Model):
    cover = models.ImageField()
    title = models.CharField(max_length=130)

    

    class Meta:
        verbose_name = _("Portfolio")
        verbose_name_plural = _("Portfolios")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Portfolio_detail", kwargs={"pk": self.pk})
