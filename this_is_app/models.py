from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class CategoryPost(models.Model):
    category_name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Post(models.Model):
    post_category = models.ForeignKey(CategoryPost, on_delete=models.CASCADE)
    post_name = models.CharField(max_length=50)
    post_descr = models.TextField(max_length=5000)
    post_photo = models.FileField(upload_to='post_photo',
                                  blank=True, null=True,
                                  default='urodlivaya_zalupa.webp')
    like_post = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post_name

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

class Commentary(models.Model):
    post_comment = models.ForeignKey(Post, on_delete=models.CASCADE)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    commentary_text = models.CharField(max_length=250)
    commentary_photo = models.FileField(upload_to='commentary_photo', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.commentary_text

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

class Likes(models.Model):
    like_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __int__(self):
        return self.username

    class Meta:
        verbose_name = 'Нравится'
        verbose_name_plural = 'Нравится'

class PredlojennieNovosti(models.Model):
    post_category_from_user = models.ForeignKey(CategoryPost, on_delete=models.CASCADE)
    post_name_from_user = models.CharField(max_length=250)
    post_descr_from_user = models.TextField(max_length=5000)
    post_photo_from_user = models.FileField(upload_to='post_photo',
                                            blank=True,
                                            null=True,
                                            default='urodlivaya_zalupa.webp'
                                        )
    post_from_user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post_name_from_user

    class Meta:
        verbose_name = 'Предложение новостя'
        verbose_name_plural = 'Предложенные новости'


