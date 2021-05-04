from django.contrib import admin
from .models import todo

@admin.register(todo)
class todo_Admin(admin.ModelAdmin):
    list_display = ['author','title','created_date']
    class Meta:
        model = todo


