"""
Defines the models that that Django application uses
"""

from django.db import models


class CommonInfo(models.Model):
    """
    Common base class for models that need a name and active field. It is
    intended to be an abstract class.
    """
    name = models.CharField(max_length=100)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name

    class Meta:
        """
        Declare the class as abstract
        """
        abstract = True


class Category(CommonInfo):
    """
    Contains the details for a category of samples. Categories have a parent
    category field to another category which creates a tree structure.
    """
    parent = models.ForeignKey('self', blank=True, null=True,
                               on_delete=models.SET_NULL,
                               related_name='children')


class Sample(CommonInfo):
    """
    The definition of a model itself. The model_filename is the path relative
    to the models directory.
    """
    model_filename = models.CharField(max_length=1000)
    description = models.CharField(max_length=2000, default='', blank=True,
                                   null=True)
    parent = models.ForeignKey(Category, blank=True, null=True,
                               on_delete=models.SET_NULL)


class Question(models.Model):
    """
    The definition of a multiple choice question, associated with a Sample
    """
    text = models.CharField(max_length=2000)
    sample = models.ForeignKey(Sample, related_name='questions')

    def correct_answers(self):
        """
        Return a list of correct answers to the question
        """
        return self.answers.filter(correct=True)

    def check_answer(self, answerid):
        """
        Check if answerid is correct. Returns True if correct, else False
        """
        for answer in self.correct_answers():
            if answer.id == int(answerid):
                return True

        return False

    def __unicode__(self):
        return self.text


class Answer(models.Model):
    """
    The definition of an answer to a Question
    """
    text = models.CharField(max_length=2000)
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, related_name='answers')

    def __unicode__(self):
        return self.text
