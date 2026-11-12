from django.db import models
from django.contrib.auth.models import User

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)

class ServiceRequest(models.Model):
    PRIORITY_CHOICES = [
        ('hight', 'Высокий приоритет'),
        ('middle', 'Средний приоритет'),
        ('low', 'Низкий приоритет'),
    ]
    STATUS = [
        ('in_progress', 'В работе'),
        ('completed', 'Завершено'),
        ('cancelled', 'Отменено'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Пользователь')
    theme = models.CharField(max_length=100, verbose_name='Тема заявки')
    description = models.TextField(verbose_name='Описание заявки')
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, verbose_name='Приоритет')
    feedback_method = models.CharField(max_length=100, verbose_name='Способ обратной связи')
    status = models.CharField(max_length=30, choices=STATUS, verbose_name='Статус заявки', default='in_progress')

    def __str__(self):
        return f"Заявка от {self.user.username if self.user else 'Аноним'}"