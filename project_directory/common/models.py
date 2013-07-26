from django.db import models


class CommonInfo(models.Model):
    name = models.CharField(max_length=100)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name

    class Meta:
        abstract = True


class Category(CommonInfo):
    parent = models.ForeignKey('self', blank=True, null=True,
                               on_delete=models.SET_NULL,
                               related_name='children')


class Sample(CommonInfo):
    model_filename = models.CharField(max_length=1000)
    parent = models.ForeignKey(Category, blank=True, null=True,
                               on_delete=models.SET_NULL)
