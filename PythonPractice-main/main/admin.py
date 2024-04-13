from django.contrib import admin

from .models import *

admin.site.register(Questions)
admin.site.register(Profile)
admin.site.register(PythonMeaning)
admin.site.register(SQLdetails)
admin.site.register(InterviewQuestionType)
admin.site.register(RandomQuestions)
admin.site.register(SQLquestions)
admin.site.register(PythonOtherImportantLibraries)
admin.site.register(Testing)
admin.site.register(Scrum)
# admin.site.register(Git)


# Register your models here.
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ["course_name"]


@admin.register(Practice)
class PracticeAdmin(admin.ModelAdmin):
    list_display = ["practice_number"]


@admin.register(InterviewQuestions)
class InterviewQuestionAdmin(admin.ModelAdmin):
    list_display = ["interview_question_type", "question"]


@admin.register(Git)
class GitAdmin(admin.ModelAdmin):
    list_display = ["question", "title"]