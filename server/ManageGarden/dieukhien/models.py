from djongo import models
from ..manhdat.models import *

# Create your models here.
class DieuKhien(models.Model):
    manhdat = models.OneToOneField(ManhDat, models.SET_NULL, null=True)
    # each individual status
    TUOI_NUOC = 1
    BAT_DEN_SUOI = 2
    BAT_QUAT_LAM_MAT = 3
    MO_MAY_CHE = 4
    DONG_MAY_CHE = 5
    # set of possible order statuses
    ACTIONS = ((TUOI_NUOC, 'TUOI_NUOC'),
                      (BAT_DEN_SUOI, 'BAT_DEN_SUOI'),
                (BAT_QUAT_LAM_MAT, 'BAT_QUAT_LAM_MAT'),
                      (MO_MAY_CHE, 'MO_MAY_CHE'),
                (DONG_MAY_CHE, 'DONG_MAY_CHE'),)
