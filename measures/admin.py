from django.contrib import admin

from .models import measure_names,measure_values

@admin.register(measure_values)
class measure_values_Admin(admin.ModelAdmin):
    list_display = ['author','measure_date', 'measure_1', 'measure_2', 'measure_3', 'measure_4', 'measure_5', 'measure_6']
    class Meta:
        model = measure_values


@admin.register(measure_names)
class measure_names_Admin(admin.ModelAdmin):
    list_display = [ "author",'measure_1_name', 'measure_2_name', 'measure_3_name', 'measure_4_name', 'measure_5_name', 'measure_6_name']
    class Meta:
        model = measure_names

