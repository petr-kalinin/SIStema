from django.core import urlresolvers
from django.db import models


class School(models.Model):
    name = models.CharField(max_length=50, help_text='Например, «ЛКШ 2015»')

    full_name = models.TextField(help_text='Полное название, не аббревиатура. По умолчанию совпадает с обычным названием. Например, «Летняя компьютерная школа 2015»')

    short_name = models.CharField(max_length=20, help_text='Используется в адресах. Например, 2015',
                                  unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.full_name:
            self.full_name = self.name
        super(School, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return urlresolvers.reverse('school:index', kwargs={'school_name': self.short_name})


class Session(models.Model):
    school = models.ForeignKey(School)

    name = models.CharField(max_length=50, help_text='Например, Август')
    short_name = models.CharField(max_length=20, help_text='Используется в адресах. Например, august')

    class Meta:
        unique_together = ['school', 'short_name']

    def __str__(self):
        return '%s.%s' % (self.school.name, self.name)