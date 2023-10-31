from .forms import QuestionForm

def post_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.save()
    else:
        form = QuestionForm()
    return render(request, 'post_question.html', {'form': form})