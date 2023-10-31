def like_answer(request, answer_id):
    answer = Answer.objects.get(pk=answer_id)
    user = request.user
    if user not in answer.likes.all():
        answer.likes.add(user)
    else:
        answer.likes.remove(user)
    return redirect('view_questions')