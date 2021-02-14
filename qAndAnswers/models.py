from django.db import models
from datetime import datetime
from django.template.defaultfilters import slugify
# Create your models here.

class Categories(models.TextChoices):
    PROFESSIONAL = 'professional'
    SKILLS= 'skills'
    FOUNDATION = 'foundation'
    ATSWA1 = 'atswa1'
    ATSWA2 = 'atswa2'
    ATSWA3 = 'atswa3'
    
   

class QAndAnswers(models.Model):
    title = models.CharField(max_length=255,unique = True)
    question = models.TextField()
    answer = models.TextField()
    category = models.CharField(max_length=50, choices=Categories.choices, default=Categories.PROFESSIONAL)
    slug = models.SlugField()
    month = models.CharField(max_length=3)
    date_created = models.DateTimeField(default=datetime.now, blank=True)
    
    def save(self, *args, **kwargs):
        original_slug = slugify(self.title)
        queryset = QAndAnswers.objects.all().filter(slug__iexact=original_slug).count()

        count = 1
        slug = original_slug
        while(queryset):
            slug = original_slug + '-' + str(count)
            count += 1
            queryset = QAndAnswers.objects.all().filter(slug__iexact=slug).count()

        self.slug = slug

        
        
        super(QAndAnswers, self).save(*args, **kwargs)

    def __str__(self):
        return self.title