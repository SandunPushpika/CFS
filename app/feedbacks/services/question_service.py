from app.feedbacks.models.question_model import Question

def get_all_questions():
    return Question.objects.all()

def create_question(text):
    new_question = Question(text=text)
    new_question.save()
    return new_question

def delete_question(question_id):
    question = Question.objects.filter(id=question_id).first()
    if not question:
        raise ValueError("Question not found")
    
    question.delete()
    return True