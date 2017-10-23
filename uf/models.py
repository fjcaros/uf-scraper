# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Price(models.Model):
    value = models.FloatField(default=None)
    date = models.DateField(default=None)

    def __unicode__(self):
        return u'value: %s | date: %s' % (self.value, self.date)
