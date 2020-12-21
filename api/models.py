from django.db import models

# Create your models here.
class Application(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    last_name = models.CharField('Фамилия', max_length=50)
    first_name = models.CharField('Имя', max_length=50)
    middle_name = models.CharField('Отчество', max_length=50, null=True, blank=True)
    birth_date = models.DateField('Дата рождения')
    passport_series = models.IntegerField('Серия паспорта')
    passport_number = models.IntegerField('Номер паспорта')
    position = models.CharField('Должность', max_length=100, null=True, blank=True)
    registration_address = models.CharField('Адрес регистрации', max_length=100, null=True, blank=True)
    actual_address = models.CharField('Фактический адрес', max_length=100, null=True, blank=True)
    questionnaire = models.FileField('Анкета', null=True, blank=True)
    result = models.TextField('Результата проверки', max_length=2000, blank=True)

    APPLICATION_STATUS = [
        ('Создана', 'Создана'),
        ('Обработана', 'Обработана'),
        ('Ошибка', 'Ошибка'),
        ('На согласование', 'На согласование'),
        ('Доп. запрос', 'Доп. запрос'),
        ('Уточнение данных', 'Уточнение данных'), 
        ('Отклонена', 'Отклонена'), 
        ('Согласована', 'Согласована')
    ]

    status = models.CharField('Статус', max_length=20, choices=APPLICATION_STATUS, default='Создана')

    def __str__(self):

        return f'{self.last_name} {self.first_name} {self.middle_name} {self.birth_date} {self.passport_series} {self.passport_number} {self.position}'