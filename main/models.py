from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=100)
    def __str__(self):
        return self.category_name
    

class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sub_category_name = models.CharField(max_length=100)
    def __str__(self):
        return self.sub_category_name
    

class Post(models.Model):
    # category = models.ForeignKey(Category, on_delete=models.CASCADE, default='category')
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, default='sub_category')
    image = models.ImageField(upload_to="images/",default="img")
    image_alt = models.CharField(max_length=255)
    title = models.CharField(max_length=100)
    description = models.TextField()
    content = models.CharField(max_length=255)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)
    

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})