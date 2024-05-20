from django.shortcuts import render
from main.models import DjangoLibrary, InterviewQuestions, PythonMeaning, DjangoRestFramework, DjangoRestFrameworkDetails
from django.core.paginator import Paginator


# Create your views here.
def django_library(request):
    meaning = DjangoLibrary.objects.all()
    return render(request, 'django_app/django-library.html', {"meaning": meaning})


def django_testing(request):
    meaning = InterviewQuestions.objects.filter(interview_question_type__type__icontains="django testing")
    return render(request, 'django_app/django_testing.html', {"meaning": meaning})


def django_interview_questions(request):
    meaning = InterviewQuestions.objects.filter(
        interview_question_type__type__icontains="django interview questions")
    return render(request, 'django_app/django_interview_questions.html', {"meaning": meaning})


def django_orm(request):
    meaning = PythonMeaning.objects.filter(title__contains="ORM")
    return render(request, 'django_app/django_orm.html', {"meaning": meaning})


def django_rest_framework(request):
    # Fetch specific fields from the DjangoRestFramework model
    queryset = DjangoRestFramework.objects.all()
    # Set the number of items per page
    items_per_page = 5
    # Create a Paginator object with the queryset and the number of items per page
    paginator = Paginator(queryset, items_per_page)
    # Get the current page number from the request
    page_number = request.GET.get('page')
    # Get the Page object for the current page
    page_obj = paginator.get_page(page_number)
    # Render the template with the Page object as context
    return render(request, 'django_app/DRF-Questions.html', {"page_obj": page_obj})


def django_rest_framework_details(request):
    queryset = DjangoRestFrameworkDetails.objects.all()
    return render(request, 'django_app/DRF-Details.html', {"queryset": queryset})

