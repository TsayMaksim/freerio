from django.db import models

# Create your models here.
class NewsCategory(models.Model):
    category_name = models.CharField(max_length=32)
    date_added = models.DateField()


    def __str__(self):
        return str(self.category_name)


class News(models.Model):
    news_title = models.CharField(max_length=128)
    news_text = models.TextField()
    news_category = models.ForeignKey(NewsCategory, on_delete=models.CASCADE)
    date_added = models.DateField()


    def __str__(self):
        return str(self.news_title)