from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify

class User(AbstractUser):
    pass


class Location(models.Model):
    name = models.CharField((""), max_length=50)
    # Put null and blank=True because what if the zoo do not specific location and constant moving
    # null for db blank for form
    longitude = models.DecimalField(max_digits=10,decimal_places=5,null=True, blank=True)
    latitude = models.DecimalField(max_digits=10,decimal_places=5,null=True, blank=True)
    

    def __str__(self):
        return self.name


class Capybara(models.Model):
    class AliveCapy(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(alive='True')
    name = models.CharField((""), max_length=50)
    gender_options = (("male", "Male"), ("female", "Female"))
    gender = models.CharField(max_length=7, choices=gender_options, null=False)
    birthday = models.DateTimeField(null=True)
    slug = models.SlugField(null=True, blank=True, unique=True)
    image_url = models.URLField(max_length=200, null=True)
    alive = models.BooleanField(default=True)
    location = models.ForeignKey(
        Location, on_delete=models.PROTECT, related_name="capybaras", null=False)
    parent = models.ManyToManyField(User, null=True, blank=True, related_name="children")
    summary = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(max_length=100, null=True, blank=True)
    objects=models.Manager()
    alive_objects=AliveCapy()

#overwrite save method in Capybara object so that everytime save slug refer to what I want
    def save(self,*args, **kwargs):
        self.slug=slugify(self.name+" "+self.location.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name +" - "+self.location.name
