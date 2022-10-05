from django.contrib.auth.models import User
from django.db import models


class Section(models.Model):
    trener = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="тренер")
    section_name = models.CharField(max_length=300, verbose_name="секция")
    device_id = models.CharField(max_length=150, verbose_name="номер устройства")

    def __str__(self):
        return f"{self.trener.first_name} {self.trener.last_name}"

    class Meta:
        verbose_name = "занятия"
        verbose_name_plural = "занятия"
