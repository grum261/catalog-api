from django.contrib import admin
from .models import Applicant


# Register your models here.
@admin.register(Applicant)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created_at',
        'last_name',
        'first_name',
        'middle_name',
        'birth_date',
        'passport_series',
        'passport_number',
        'position',
        'status'
    )

    list_filter = ('id', 'created_at', 'status')