from django.db import models

class measure_values(models.Model):
    author = models.ForeignKey("auth.User", on_delete = models.CASCADE, verbose_name= "author")
    measure_1 = models.IntegerField(verbose_name="measure 1")
    measure_2 = models.IntegerField(verbose_name="measure 2")
    measure_3 = models.IntegerField(verbose_name="measure 3")
    measure_4 = models.IntegerField(verbose_name="measure 4")
    measure_5 = models.IntegerField(verbose_name="measure 5")
    measure_6 = models.IntegerField(verbose_name="measure 6")
    measure_date = models.DateField(verbose_name="measure date")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="measure input date")
    def __str__(self): 
        return '%s - %s' % (self.author, self.measure_date)
    class Meta:
        ordering = ['-created_date']


class measure_names(models.Model):
    author = models.ForeignKey("auth.User", on_delete = models.CASCADE, verbose_name= "Author",primary_key=True)
    measure_1_name = models.CharField(max_length=20,verbose_name="measure 1", default=" ")
    measure_2_name = models.CharField(max_length=20,verbose_name="measure 2", default=" ")
    measure_3_name = models.CharField(max_length=20,verbose_name="measure 3", default=" ")
    measure_4_name = models.CharField(max_length=20,verbose_name="measure 4", default=" ")
    measure_5_name = models.CharField(max_length=20,verbose_name="measure 5", default=" ")
    measure_6_name = models.CharField(max_length=20,verbose_name="measure 6", default=" ")
    def __str__(self): 
        return '%s - measures' % (self.author)
    """class Meta:
        ordering = ['-created_date']"""

