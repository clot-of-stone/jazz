from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True,
                              verbose_name='Изображение', )

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=50, verbose_name='Раздел')
    articles = models.ManyToManyField(Article, through='Scope',
                                      related_name='tags',
                                      verbose_name='Статьи')

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'
        ordering = ('name',)


class Scope(models.Model):
    is_main = models.BooleanField(default=False, verbose_name='Основной '
                                                              'раздел')
    article = models.ForeignKey(Article, on_delete=models.CASCADE,
                                verbose_name='Статья', related_name='scopes')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE,
                            verbose_name='Раздел', related_name='scopes')

    class Meta:
        verbose_name = 'Тематика статьи'
        verbose_name_plural = 'Тематики статьи'
        ordering = ('-is_main', 'tag')
        unique_together = (('article', 'tag'),)
