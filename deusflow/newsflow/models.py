from django.db import models

# Create your models here.
class Articles(models.Model):
    title = models.CharField('Name', max_length=50)
    anons = models.CharField('Anons',max_length =250)
    full_text = models.TextField('Articles')
    date = models.DateTimeField('Date')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/newsflow/{self.id}'

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
