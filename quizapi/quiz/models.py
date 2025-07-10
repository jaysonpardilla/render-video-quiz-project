from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category_images/', default='default_category.png')

    def __str__(self):
        return self.name

class Video(models.Model):
    name = models.CharField(max_length=255)
    video_file = models.FileField(upload_to='videos/')
    category = models.ForeignKey(Category, related_name='videos', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name
