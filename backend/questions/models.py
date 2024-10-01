from django.db import models

class Categories(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Название")
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name="Ссылка")
    
    class Meta:
        db_table = "category"
        verbose_name = "Категорию"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name

class Questions(models.Model):
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE, verbose_name="Автор")
    category = models.ForeignKey(to=Categories, on_delete=models.CASCADE, verbose_name="Категория")
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name="Ссылка")
    text = models.TextField(verbose_name="Текст")
    rating = models.IntegerField(default=0, verbose_name="Рейтинг")
    
    
    class Meta:
        db_table = "question"
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"

    def __str__(self):
        return self.title