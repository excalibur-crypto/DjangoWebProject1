﻿from django.db import models
from django.contrib import admin
from datetime import datetime
from django.urls import reverse
from django.contrib.auth.models import User

class Blog(models.Model):

    title = models.CharField(max_length=100, unique_for_date="posted", verbose_name="Заголовок")

    description = models.TextField(verbose_name="Краткое содержание")

    content = models.TextField(verbose_name="Полное содержание")

    posted = models.DateTimeField(default=datetime.now(), db_index=True, verbose_name="Опубликована")

    image = models.FileField(default='temp.jpg', verbose_name="Путь к картинке")

    def get_absolute_url(self):

        return reverse("blogpost", args=[str(self.id)])
    
    def __str__(self):

        return self.title
    class Meta:

        db_table="Posts"

        ordering =["-posted"]

        verbose_name ="статья блога"

        verbose_name_plural="статьи блога"

admin.site.register(Blog)

class Comment(models.Model):

    text = models.TextField(verbose_name = "Текст комментария")

    date = models.DateTimeField(default = datetime.now(), db_index = True, verbose_name="Дата комментария")

    author = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name = "Автор комментария")

    post = models.ForeignKey(Blog, on_delete = models.CASCADE, verbose_name = "Статья комментария")

    def __str__(self):
        
        return f"{self.author.username}: {self.content[:20]}"
        # return 'Комментарий %d' % (self.id, self.author.username, self.post)

    class Meta:

        db_table = "Comment"

        ordering = ["-date"]

        verbose_name = "Комметарий к статье блога"

        verbose_name_plural = "Комментарий к статьям блога"

admin.site.register(Comment)

class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.FileField(default = 'temp.jpg', verbose_name="Путь к картинке.")  # Изменено на FileField
    
    def __str__(self):
        return self.title

   


