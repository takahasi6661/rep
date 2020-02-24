from django.db import models
from django.db import models
from django.shortcuts import reverse

from django.utils.text import slugify
from time import time


#from django.shortcuts import reverse #функция, которая генерирует ссылку

# Create your models here.


def gen_slug(s):
    new_slug=slugify(s, allow_unicode=True)
    return new_slug+'-'+str(int(time()))


class Think (models.Model):
    title=models.CharField (max_length=150, db_index=True)
    opis=models.CharField (max_length=150, db_index=True)
    slug=models.SlugField(max_length=150, unique=True)
    body=models.TextField (blank=True, db_index=True)
    date_pub=models.DateTimeField(auto_now_add=True)

    def save(self,*args,**kwargs):
        if not self.id:
            self.slug=gen_slug(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('think_detail_url', kwargs={'slug':self.slug})

    def __str__(self):
        return self.title
    def get_update_url(self):
        return reverse('think_update_url', kwargs={'slug':self.slug})
    def get_delete_url(self):
        return reverse('think_delete_url', kwargs={'slug':self.slug})
    class Meta:
        ordering=['-date_pub']







