from django.db import models

# Create your models here.

class ProgramType(models.Model):
    program_id = models.AutoField(primary_key=True)  # Унікальний айді програми
    name = models.CharField(max_length=50)  # Назва програми
    info = models.CharField(max_length=1000)  # Опис програми
    date_start = models.DateTimeField()  # Дата початку
    date_stop = models.DateTimeField()  # Кінцева дата
    date_created = models.DateTimeField(auto_now_add=True)  # Дата створення
    date_updated = models.DateTimeField(auto_now=True)  # Дата обновлення

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Програма',
        verbose_name_plural = 'Програми'

class Program3(models.Model):
    region = models.CharField(max_length=50)  # Область
    zip = models.IntegerField(max_length=20) # Поштовий індекс
    job_description = models.CharField(max_length=1000, null=True)  # Опис діяльності
    postmail_place = models.CharField(max_length=50)  # Фізична адреса листування
    email = models.EmailField(max_length=100)  # Електронна пошта
    project_name = models.CharField(max_length=50, null=True)  # Назва проєкту
    project_callnumber = models.IntegerField(max_length=13, null=True)  # Контактний номер менеджера проекту
    projectowner_first_name = models.CharField(max_length=50, null=True)  # Імя менеджера
    projectowner_last_name = models.CharField(max_length=50, null=True)  # Прізвище менеджера
    projectowner_fathers_name = models.CharField(max_length=50, null=True)  # По батькові менеджера
    project_sum = models.IntegerField(max_length=20, null=True)  # Сума проекту
    date_created = models.DateTimeField(auto_now_add=True)  # Дата створення
    date_updated = models.DateTimeField(auto_now=True)  # Дата обновлення
    def __str__(self):
        return self.zip

    class Meta:
        verbose_name = 'Користуавч',
        verbose_name_plural = 'Користувачі'