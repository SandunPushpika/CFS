from django.urls import path
from app.feedbacks.views import (
    feedback_crud_api,
    list_feedbacks_api,
    feedback_stats_api,
    question_api,
    delete_question_api,
)

urlpatterns = [
    path("", feedback_crud_api, name="feedback-crud"),
    path("<int:feedback_id>/", feedback_crud_api, name="feedback-update-delete"),
    path("list/", list_feedbacks_api, name="feedback-list"),
    path("stats/", feedback_stats_api, name="feedback-stats"),
    path("questions/", question_api, name="questions"),
    path("questions/<int:question_id>/", delete_question_api, name="delete-question")
]