from django.db import models

# Create your models here.
# Blog - title, photo, description, published_date, author

class Blog(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='Blog/image')
    description = models.TextField()
    
    published_date = models.DateTimeField(auto_now=True)

    author = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.title}  by {self.author}"
