from django.db import models

from questions.models import Questions
from users.models import User

class OtvetQuerySet(models.QuerySet):
    
    def rating_plus(self):
        return self.update(rating=f'rating'+1)
    def rating_minus(self):
        return self.update(rating=f'rating'-1)
 

class Otvets(models.Model):

    id = models.AutoField(primary_key=True, verbose_name="ID")
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name="Пользователь")
    question = models.ForeignKey(to=Questions, on_delete=models.CASCADE, verbose_name="Вопрос")
    discription = models.TextField(verbose_name="Ответ")
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Создан")
    rating = models.IntegerField(default=0, verbose_name="Рейтинг")

    class Meta:
        db_table = "otvet"
        verbose_name = "Ответ"
        verbose_name_plural = "Ответы"

    objects = OtvetQuerySet().as_manager()

    def __str__(self):
        return f'Пользователь {self.user}, вопрос {self.question}, ответ {self.discription}'