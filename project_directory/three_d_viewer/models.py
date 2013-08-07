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
    description = models.CharField(max_length=2000, default='', blank=True, null=True)
    parent = models.ForeignKey(Category, blank=True, null=True,
                               on_delete=models.SET_NULL)


class Question(models.Model):
    text = models.CharField(max_length=2000)
    sample = models.ForeignKey(Sample, related_name='questions')

    def correct_answers(self):
        return self.answers.filter(correct = True)
    
    def __unicode__(self):
        return self.text
    
class Answer(models.Model):
    text = models.CharField(max_length=2000)
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, related_name='answers')
    
    def __unicode__(self):
        return self.text
