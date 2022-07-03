from tabnanny import verbose
from django.db import models

# Create your models here.

class Image(models.Model):
    name = models.CharField(max_length=100)
    img_file = models.ImageField(upload_to='images')

    class Meta:
        verbose_name = "Image"
        verbose_name_plural = "Images"

    def __str__(self):
        return self.name if self.name else "Picture without name"

class Category(models.Model): 

    name = models.CharField(max_length=100)

    parent = models.ForeignKey(
        "self",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    ) 
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
       return self.name



class Articles(models.Model):
    title = models.CharField('Name', max_length=50)
    announcement = models.CharField('Announcement', max_length=100)
    full_text = models.TextField('Full Text')

    img_file = models.ForeignKey(
        Image,
        on_delete=models.CASCADE,
        blank=True,
    ) 

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        blank=True,    
    ) 

    date = models.DateTimeField('Date of publication')


    def __str__(self):
        return f"{self.title} | {self.img_file} | {self.category}"

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"




