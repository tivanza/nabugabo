# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class signUp(models.Model):
    email = models.EmailField()
    full_name = models.CharField(max_length=120,blank=True,null=True)
    timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated = models.DateTimeField(auto_now_add=False,auto_now=True)

    def _unicode_(self):
        return self.email