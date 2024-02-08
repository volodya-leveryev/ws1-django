from django.db import models


class Student(models.Model):
    last_name = models.CharField('фамилия', max_length=50)
    first_name = models.CharField('имя', max_length=50)
    second_name = models.CharField('отчество', max_length=50, blank=True,
                                   default='')
    group = models.ForeignKey('EduGroup', verbose_name='группа', null=True,
                              on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'студент'
        verbose_name_plural = 'студенты'

    def __str__(self):
        result = f'{self.last_name} {self.first_name[0]}.'
        if self.second_name:
            result += f'{self.second_name[0]}.'
        return result


class EduGroup(models.Model):
    name = models.CharField('название', max_length=50)

    class Meta:
        verbose_name = 'группа'
        verbose_name_plural = 'группы'

    def __str__(self):
        return self.name
