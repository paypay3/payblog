from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField('カテゴリ名', max_length=255)
    created_at = models.DateTimeField('作成日', default=timezone.now)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField('タイトル', max_length=255)
    text = models.TextField('本文')
    image = models.ImageField('画像ファイル', upload_to='images/')
    created_at = models.DateTimeField('作成日', default=timezone.now)
    category = models.ForeignKey(Category, verbose_name='カテゴリ', on_delete=models.PROTECT)
    relation_posts = models.ManyToManyField('self', verbose_name='関連記事', blank=True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.text[:100]


class Comment(models.Model):
    name = models.CharField('名前', max_length=255, default="pay's friend")
    text = models.TextField('本文')
    post = models.ForeignKey(Post, verbose_name='対象記事', on_delete=models.CASCADE)
    created_at = models.DateTimeField('作成日', default=timezone.now)
    is_public = models.BooleanField('公開承認', default=False)

    def __str__(self):
        return self.name


class Reply(models.Model):
    name = models.CharField('名前', max_length=255, default="pay's friend")
    text = models.TextField('本文')
    comment = models.ForeignKey(Comment, verbose_name='対象コメント', on_delete=models.CASCADE)
    created_at = models.DateTimeField('作成日', default=timezone.now)
    is_public = models.BooleanField('公開承認', default=False)

    def __str__(self):
        return self.name
