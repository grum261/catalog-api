# Generated by Django 3.1.4 on 2020-12-21 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_name', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('first_name', models.CharField(max_length=50, verbose_name='Имя')),
                ('middle_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Отчество')),
                ('birth_date', models.DateField(verbose_name='Дата рождения')),
                ('passport_series', models.IntegerField(verbose_name='Серия паспорта')),
                ('passport_number', models.IntegerField(verbose_name='Номер паспорта')),
                ('position', models.CharField(blank=True, max_length=100, null=True, verbose_name='Должность')),
                ('registration_address', models.CharField(blank=True, max_length=100, null=True, verbose_name='Адрес регистрации')),
                ('actual_address', models.CharField(blank=True, max_length=100, null=True, verbose_name='Фактический адрес')),
                ('questionnaire', models.FileField(blank=True, null=True, upload_to='', verbose_name='Анкета')),
                ('result', models.TextField(blank=True, max_length=2000, verbose_name='Результата проверки')),
                ('status', models.CharField(choices=[('Создана', 'Создана'), ('Обработана', 'Обработана'), ('Ошибка', 'Ошибка'), ('На согласование', 'На согласование'), ('Доп. запрос', 'Доп. запрос'), ('Уточнение данных', 'Уточнение данных'), ('Отклонена', 'Отклонена'), ('Согласована', 'Согласована')], default='Создана', max_length=20, verbose_name='Статус')),
            ],
        ),
    ]
