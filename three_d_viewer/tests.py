"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from three_d_viewer.models import Category, Question, Answer


class ModelsTest(TestCase):
    #def setUp(self):
      #CommonInfo.objects.create(name="test", active=True)
      #  Animal.objects.create(name="cat", sound="meow")

    def test_common_unicode(self):
        """
        Tests the unicode method for categories
        """
        testcat = Category(name='test', active=True)
        self.assertEqual("test", testcat.__unicode__())

    def test_question_unicode(self):
        """
        Tests the unicode method for questions
        """

        testquestion = Question(text="Test")
        self.assertEqual("Test", testquestion.__unicode__())

    def test_answer_unicode(self):
        """
        Tests the unicode method for answers
        """

        testanswer = Answer(text="Test")
        self.assertEqual("Test", testanswer.__unicode__())

    def test_no_correct_answers(self):
        testquestion = Question(text="Test", id=1)

        answer = Answer(text="Test", correct=False, question=testquestion)
        answer2 = Answer(text="Test2", correct=False, question=testquestion)

        testquestion.answers = [answer, answer2, ]

        self.assertEqual(len(testquestion.correct_answers()), 0)

    def test_correct_answers(self):
        testquestion = Question(text="Test", id=1)

        answer = Answer(text="Test", correct=True, question=testquestion)
        answer2 = Answer(text="Test2", correct=False, question=testquestion)
        testquestion.answers = [answer, answer2]

        self.assertEqual(len(testquestion.correct_answers()), 1)

    def test_multiple_correct_answers(self):
        testquestion = Question(text="Test", id=1)

        answer = Answer(text="Test", correct=True, question=testquestion)
        answer2 = Answer(text="Test2", correct=False, question=testquestion)
        answer3 = Answer(text="Test3", correct=True, question=testquestion)
        testquestion.answers = [answer, answer2, answer3, ]

        self.assertEqual(len(testquestion.correct_answers()), 2)
