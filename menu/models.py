from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=50)
    visible = models.BooleanField(default=True)
    css_class = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=50)
    position = models.PositiveIntegerField(default=1)
    visible = models.BooleanField(default=True)
    named_url = models.CharField(max_length=50, blank=True, null=True, default='')
    url = models.CharField(max_length=50, blank=True, null=True, default='')

    class Meta:
        ordering = ('position', )

    def __str__(self):
        return self.name


