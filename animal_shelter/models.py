from django.db import models
from datetime import datetime


# Create your models here.
class Kind(models.Model):
    name = models.CharField(max_length=50, verbose_name="Вид", null=True, blank=True)

    def __str__(self):
        return self.name


class Pet(models.Model):
    name = models.CharField(max_length=13, verbose_name='Кличка')
    description = models.TextField(verbose_name='О питомце')
    receipt_date = models.DateField(auto_now=True, verbose_name="Поступил")
    face = models.ImageField(upload_to='pets_foto', blank=True, verbose_name="Фотография")
    birth_data = models.DateField(blank=True, null=True, verbose_name='Дата рождения')

    MALE = 'Мальчик'
    FEMALE = 'Девочка'
    GENDER = [(MALE, "Мальчик"), (FEMALE, "Девочка"), ]

    gender = models.CharField(max_length=10, choices=GENDER, verbose_name='Пол', null=True)

    kind = models.ForeignKey(Kind, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Вид")

    @property
    def age(self):
        age = int((datetime.now().date() - self.birth_data).days / 31)

        if age < 12:
            month = (2, 3, 4,)
            if age == 1:
                return f'{age} месяц'
            elif age in month:
                return f'{age} месяца'
            else:
                return f'{age} месяцев'
        elif age > 12:
            age = int(age / 12)
            last_simbol = str(age)[-1]
            year = ("1",)
            exception = (11, 12, 13, 14,)
            year2 = ("2", "3", "4",)
            if last_simbol in year and age not in exception:
                return f'{age} год'
            elif last_simbol in year2 and age not in exception:
                return f'{age} года'
            elif last_simbol not in year2 and age not in exception:
                return f'{age} лет'
            else:
                return age

    def __str__(self):
        return self.name
