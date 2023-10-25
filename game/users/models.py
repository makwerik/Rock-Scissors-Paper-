from django.db import models


class UserInfo(models.Model):
    name = models.CharField('Имя', max_length=50)
    score_user = models.IntegerField('Очки игрока', null=True)
    score_pc = models.IntegerField('Очки Компьютера', null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Результат'
        verbose_name_plural = 'Результаты'

