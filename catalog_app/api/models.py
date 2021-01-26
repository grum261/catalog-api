from django.db import models
from django.conf import settings

class AbstractApplication(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    APPLICATION_STATUS = [
        ('Создана', 'Создана'),
        ('Обработана', 'Обработана'),
        ('Ошибка', 'Ошибка'),
        ('На согласование', 'На согласование'),
        ('Доп. запрос', 'Доп. запрос'),
        ('Уточнение данных', 'Уточнение данных'), 
        ('Отклонена', 'Отклонена'), 
        ('Согласована', 'Согласована'),
    ]

    status = models.CharField('Статус', max_length=20, choices=APPLICATION_STATUS, default='Создана')

    class Meta:
        abstract = True

class Applicant(AbstractApplication):
    last_name = models.CharField('Фамилия', max_length=50, null=False)
    first_name = models.CharField('Имя', max_length=50, null=False)
    middle_name = models.CharField('Отчество', max_length=50, null=True, blank=True)
    birth_date = models.DateField('Дата рождения')
    passport_series = models.IntegerField('Серия паспорта')
    passport_number = models.IntegerField('Номер паспорта')
    position = models.CharField('Должность', max_length=100, null=True, blank=True)
    registration_address = models.CharField('Адрес регистрации', max_length=100, null=True, blank=True)
    actual_address = models.CharField('Фактический адрес', max_length=100, null=True, blank=True)
    questionnaire = models.FileField('Анкета', null=True, blank=True)
    result = models.TextField('Результата проверки', max_length=2000, blank=True)

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.middle_name} {self.birth_date} {self.passport_series} {self.passport_number} {self.position}'
