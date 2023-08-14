from django.urls import path

from api.views import *
app_name = "api"

# urlpatterns = [
#     path("", index, name="index"),
#     path("<int:question_id>/", detail, name="detail"),
#     # ex: /polls/5/results/
#     path("<int:question_id>/results/", results, name="results"),
#     # ex: /polls/5/vote/
#     path("<int:question_id>/vote/", vote, name="vote"),
# ]


from django.urls import path

from . import views

app_name = "api"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]