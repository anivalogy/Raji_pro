from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Choice, Question

from django.utils import timezone

# class IndexView(generic.ListView):
#     template_name = "api/index.html"
#     context_object_name = "latest_question_list"

#     def get_queryset(self):
#         """Return the last five published questions."""
#         return Question.objects.order_by("-pub_date")[:5]

class IndexView(generic.ListView):
    template_name = "api/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by("-pub_date")[:5]

def get_queryset(self):
    """
    Return the last five published questions (not including those set to be
    published in the future).
    """
    return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[
        :5
    ]

class DetailView(generic.DetailView):
    model = Question
    template_name = "api/detail.html"
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = "api/result.html"


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "api/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("api:results", args=(question.id,)))
























# from django.shortcuts import render,get_object_or_404,HttpResponseRedirect
# # Create your views here.
# from django.http import HttpResponse
# from django.http import Http404
# from .models import Question,Choice
# from django.urls import reverse



# def index(request):
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     context = {"latest_question_list": latest_question_list}
#     return render(request, "api/index.html", context)

# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "api/detail.html", {"question": question})

#     # try:
#     #     question = Question.objects.get(pk=question_id)
#     # except Question.DoesNotExist:
#     #     raise Http404("Question does not exist")
#     # return render(request, "api/detail.html", {"question": question})


# # def detail(request, question_id):
# #     return HttpResponse("You're looking at question %s." % question_id)
















# # #mapping with temp
# # def index(request):
# #     latest_question_list = Question.objects.order_by("-pub_date")[:5]
# #     template = loader.get_template("api/index.html")
# #     context = {
# #         "latest_question_list": latest_question_list,
# #     }
# #     return HttpResponse(template.render(context, request))




# # def index(request):
# #     latest_question_list = Question.objects.order_by("-pub_date")[:5]
# #     output = "++ ".join([q.question_text for q in latest_question_list])
# #     return HttpResponse(output)


# # Leave the rest of the views (detail, results, vote) unchanged

# # def index(request):
# #     return HttpResponse("Hello, world. You're at the api index.")


# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "api/result.html", {"question": question})


# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST["choice"])
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(
#             request,
#             "api/detail.html",
#             {
#                 "question": question,
#                 "error_message": "You didn't select a choice.",
#             },
#         )
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse("api:results", args=(question.id,)))