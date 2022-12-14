from django.db import models
from ckeditor.fields import RichTextField
from django.template.defaultfilters import slugify


# Create your models here.

class Offers(models.Model):
  contrat_type =  [
    ('CDI', 'CDI'),
    ('CDD', 'CDD'),
    ('Stage', 'Stage'),
]
  searching_for = models.CharField(max_length=255, verbose_name='post')
  slug = models.SlugField(null=True, blank=True)
  contract = models.CharField(max_length=10, choices=contrat_type, default=contrat_type[0], verbose_name='type_de_contact')
  post_number = models.PositiveIntegerField(default=1)
  description = RichTextField()
  looking_for = RichTextField()
  experience = models.CharField(max_length=255)
  region = models.CharField(max_length=255)
  
  
  
  def __str__(self): 
    return self.searching_for 
  
  def save(self , *args, **kwargs):
    self.slug = slugify(self.searching_for + '-' + self.region)
    return super().save(*args, **kwargs)
  
  class Meta: 
    verbose_name_plural = 'offers'
  