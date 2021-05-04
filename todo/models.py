from django.db import models

class todo(models.Model):
    author = models.ForeignKey("auth.User", on_delete = models.CASCADE, verbose_name= "Author")
    title = models.CharField(max_length = 50,verbose_name = "title")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="todo date")
    def __str__(self): 
        return '%s - %s' % (self.author, self.title)
    class Meta:
        ordering = ['-created_date']


