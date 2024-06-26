from django.db import models

# Create your models here.
class Review(models.Model):
    stars = models.IntegerField()
    review_text = models.TextField()
    name = models.TextField()  
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Review by {self.name} on {self.datetime}'