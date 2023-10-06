from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=30, null=False, unique=True)

    def __str__(self):
        return self.name
    
class Tag(models.Model):
    tags = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.tags

class Quote(models.Model):
    quote = models.TextField(null=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.quote
