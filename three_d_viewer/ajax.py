"""
Handle asynchronous calls from the web pages
"""

from django.utils import simplejson
from dajaxice.decorators import dajaxice_register

from models import Question


@dajaxice_register
def check_answer(request, answerid, questionid):
    """
    Check whether answerid is the correct answer for questionid.
    Returns a boolean in 'result'
    """

    question = Question.objects.get(id=int(questionid))

    result = False
    for answer in question.correct_answers():
        print type(answer.id)
        if answer.id == int(answerid):
            result = True

    return simplejson.dumps({'result': result})
