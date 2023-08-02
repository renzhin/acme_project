from django.contrib import admin


# Из модуля models импортируем модель Birthday...
from .models import Birthday, Tag


# ...и регистрируем её в админке:
admin.site.register(Tag)
admin.site.register(Birthday)
