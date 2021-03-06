"""
Defines the models that that Django application uses
"""

from django.db import models
from model_utils.managers import InheritanceManager


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

    objects = InheritanceManager()

    @property
    def active_children(self):
        return self.children.filter(active=True).order_by('name')

    @property
    def active_samples(self):
        return self.samples.select_subclasses(Sample, Mineral).filter(active=True).order_by('name')
        
    @property
    def active_101_samples(self):
        return self.samples.select_subclasses(Sample, Mineral).filter(active=True).filter(erb101_sample=True).order_by('name')

    class Meta:
	    verbose_name_plural = "Categories"


class Sample(CommonInfo):
    """
    The definition of a model itself. The model_filename is the path relative
    to the models directory.
    """
    model_filename = models.CharField(max_length=1000)
    description = models.CharField(max_length=2000, default='', blank=True,
                                   null=True)
    parent = models.ForeignKey(Category, blank=True, null=True,
                               on_delete=models.SET_NULL,
                               related_name="samples")
    viewed_count = models.IntegerField(default=0)
    erb101_sample = models.BooleanField(default=False)

    #Use the inheritance manager for handling subclasses
    objects = InheritanceManager()

    def GetTopParent(self, current_parent):
        if current_parent.parent is None:
            return current_parent
        else:
            return self.GetTopParent(current_parent.parent)

    @property
    def url(self):
        cat = self.GetTopParent(self.parent)

        self.viewed_count += 1

        if cat.name == 'Fossils':
            return 'fossil_detail'
        elif cat.name == 'Rocks':
            return 'rock_detail'
        else:
            return 'sample_detail'


class Mineral(Sample):
    """
    Extending the Sample class to add details specific to minerals
    """
    chemical_formula = models.CharField(max_length=100, blank=True)
    hardness = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    specific_gravity = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    cleavage_fracture = models.CharField(max_length=100, blank=True)
    lustre = models.CharField(max_length=100, blank=True)
    colour = models.CharField(max_length=100, blank=True)
    streak = models.CharField(max_length=100, blank=True)
    habit = models.CharField(max_length=1000, blank=True)
    crystallography = models.CharField(max_length=100, blank=True)
    identifying_features = models.CharField(max_length=1000, blank=True)
    occurance = models.CharField(max_length=1000, blank=True)

    @property
    def url(self):
        self.viewed_count += 1
        return 'mineral_detail'


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

class GlossaryEntry(models.Model):
	"""
	A glossary entry
	"""
	name = models.CharField(max_length=200)
	definition = models.CharField(max_length=2000)
	
	def __unicode__(self):
		return self.name
	
	class Meta:
	    verbose_name_plural = "Glossary Entries"
