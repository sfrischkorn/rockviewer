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
    result = question.check_answer(answerid)

    return simplejson.dumps({'result': result})
