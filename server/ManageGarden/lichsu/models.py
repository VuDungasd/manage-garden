from djongo import models
from ..manhdat.models import *

# Create your models here.
class LichSu(models.Model):
    manhdat = models.ForeignKey(ManhDat, models.SET_NULL, null=True)
    nhiet_do = models.IntegerField(default=0)
    do_am = models.IntegerField(default=0)
    anh_sang = models.IntegerField(default=0)
    status_maiche = models.BooleanField(default=False)
    status_quatmat = models.BooleanField(default=False)
    status_maytuoinuoc = models.BooleanField(default=False)
    status_densuoi = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.manhdat
