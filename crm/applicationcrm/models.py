from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


class MyAccountManager(BaseUserManager):
    def create_user(self, email, password):
        if not email:
            raise ValueError("Must email")
        user = self.model(
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name='email', max_length=60, unique=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = MyAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


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
    zip = models.IntegerField(max_length=20)  # Поштовий індекс
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
