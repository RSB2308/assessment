from .models import Question

def view_questions(request):
    questions = Question.objects.all()
    return render(request, 'view_questions.html', {'questions': questions})

def answer_question(request, question_id):
    question = Question.objects.get(pk=question_id)
    if request.method == 'POST':
        # Handle the answer submission
        pass
    return render(request, 'answer_question.html', {'question': question})