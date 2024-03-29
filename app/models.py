from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField("Название", max_length=30, unique=True, null=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Категории"
        verbose_name = "Категория"


