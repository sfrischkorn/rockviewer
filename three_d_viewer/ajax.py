from django.utils import simplejson
from dajaxice.decorators import dajaxice_register

from three_d_viewer.models import Question

@dajaxice_register
def dajaxice_example(request):
    test = check_answer(request, 3, 1)
    print test
    return simplejson.dumps({'message':'Hello from Python!'})

@dajaxice_register    
def check_answer(request, answerid, questionid):
    question = Question.objects.get(id=int(questionid))
    
    result = False
    for answer in question.correct_answers():
        print type(answer.id)
        if answer.id == int(answerid):
            result = True
    print simplejson.dumps({'result': result})
    return simplejson.dumps({'result': result})
    