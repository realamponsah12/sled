from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = image = models.ImageField(upload_to='media', blank=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    comment=models.TextField(null=True, blank=True)
    email=models.EmailField(max_length=255)
    created_at =  models.DateTimeField(auto_now=True)


class BlogAdmin(models.Model):
    admin_blog=models.CharField(max_length=250) 
    passion = models.CharField(max_length = 250)
    created_at =  models.DateTimeField(auto_now=True)


    from django.db import models 

class Newsletter(models.Model):
    email = models.EmailField()

    def __str__(self) -> str:
        return self.email