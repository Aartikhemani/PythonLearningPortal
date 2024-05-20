from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    forget_password_token = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class Course(models.Model):
    course_name = models.CharField(max_length=100)

    def __str__(self):
        return self.course_name


class Practice(models.Model):
    practice_number = models.CharField(max_length=100)

    def __str__(self):
        return self.practice_number


class Questions(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    practice = models.ForeignKey(Practice, on_delete=models.CASCADE)
    question = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)
    option_one = models.CharField(max_length=255)
    option_two = models.CharField(max_length=255)
    option_three = models.CharField(max_length=255)
    option_four = models.CharField(max_length=255)

    def __str__(self):
        return self.question


class PythonMeaning(models.Model):
    title = models.CharField(max_length=255, blank=True)
    text = models.TextField()
    code_block = models.TextField(blank=True, null=True)
    img = models.ImageField(upload_to="productImages", blank=True)
    url = models.URLField(max_length=200, blank=True, null=True)
    pdf = models.FileField(upload_to='pdfs', blank=True)


class PythonOtherImportantLibraries(models.Model):
    title = models.CharField(max_length=225, blank=True)
    text = models.TextField()
    code_block = models.TextField(blank=True, null=True)
    img = models.ImageField(upload_to="productImages", blank=True)
    url = models.URLField(max_length=200, blank=True, null=True)
    pdf = models.FileField(upload_to='pdfs', blank=True)

    def __str__(self):
        return self.title


class Testing(models.Model):
    title = models.CharField(max_length=225, blank=True)
    text = models.TextField()
    code_block = models.TextField(blank=True, null=True)
    img = models.ImageField(upload_to="testingImages", blank=True)
    url = models.URLField(max_length=200, blank=True, null=True)
    pdf = models.FileField(upload_to='testing_pdfs', blank=True)


class InterviewQuestionType(models.Model):
    type = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.type


class InterviewQuestions(models.Model):
    interview_question_type = models.ForeignKey(InterviewQuestionType, on_delete=models.CASCADE)
    question = models.TextField(max_length=255, blank=True)
    img = models.ImageField(upload_to="productImages", blank=True)
    img2 = models.ImageField(upload_to="productImages", blank=True)
    answer1 = models.TextField(blank=True)
    code_block = models.TextField(blank=True, null=True)
    answer2 = models.TextField(blank=True, null=True)


class RandomQuestions(models.Model):
    question = models.TextField(max_length=255, blank=True)
    answer = models.TextField()
    img = models.ImageField(upload_to="productImages", blank=True)
    code_block = models.TextField(blank=True, null=True)
    url = models.URLField(max_length=200, blank=True, null=True)
    pdf = models.FileField(upload_to='testing_pdfs', blank=True)


class SQLquestions(models.Model):
    interview_question_type = models.ForeignKey(InterviewQuestionType, on_delete=models.CASCADE)
    question = models.TextField(max_length=255, blank=True)
    img = models.ImageField(upload_to="productImages", blank=True)
    answer = models.TextField(blank=True)
    code_block = models.TextField(blank=True, null=True)


class SQLdetails(models.Model):
    title = models.CharField(max_length=255, blank=True)
    text = models.TextField(blank=True)
    code_block = models.TextField(blank=True, null=True)
    img = models.ImageField(upload_to="productImages", blank=True)
    img2 = models.ImageField(upload_to="productImages", blank=True)
    img3 = models.ImageField(upload_to="productImages", blank=True)
    url = models.URLField(max_length=200, blank=True, null=True)
    pdf = models.FileField(upload_to='pdfs', blank=True)


# scrum------------------------
class Scrum(models.Model):
    title = models.CharField(max_length=355, blank=True)
    text = models.TextField(blank=True)
    question = models.TextField(max_length=255, blank=True)
    answer = models.TextField(blank=True)
    img = models.ImageField(upload_to="productImages/scrum", blank=True)
    img2 = models.ImageField(upload_to="productImages/scrum", blank=True)
    img3 = models.ImageField(upload_to="productImages/scrum", blank=True)
    url = models.URLField(max_length=200, blank=True, null=True)
    pdf = models.FileField(upload_to='pdfs/scrum', blank=True)


# git-----------------------------
class Git(models.Model):
    title = models.CharField(max_length=355, blank=True)
    text = models.TextField(blank=True)
    question = models.TextField(max_length=255, blank=True)
    answer = models.TextField(blank=True)
    code_block = models.TextField(blank=True, null=True)
    img = models.ImageField(upload_to="productImages/git", blank=True)
    img2 = models.ImageField(upload_to="productImages/git", blank=True)
    img3 = models.ImageField(upload_to="productImages/git", blank=True)
    url = models.URLField(max_length=200, blank=True, null=True)
    pdf = models.FileField(upload_to='pdfs/git', blank=True)


class DjangoRestFramework(models.Model):
    title = models.CharField(max_length=355, blank=True)
    text = models.TextField(blank=True)
    question = models.TextField(max_length=255, blank=True)
    code_block = models.TextField(blank=True, null=True)
    answer = models.TextField(blank=True)
    img = models.ImageField(upload_to="productImages/DRF", blank=True)
    img2 = models.ImageField(upload_to="productImages/DRF", blank=True)
    img3 = models.ImageField(upload_to="productImages/DRF", blank=True)
    url = models.URLField(max_length=200, blank=True, null=True)
    pdf = models.FileField(upload_to='pdfs/DRF', blank=True)


class DjangoRestFrameworkDetails(models.Model):
    title = models.CharField(max_length=355, blank=True)
    text = models.TextField(blank=True)
    code_block = models.TextField(blank=True, null=True)
    img = models.ImageField(upload_to="productImages/DRF", blank=True)
    img2 = models.ImageField(upload_to="productImages/DRF", blank=True)
    img3 = models.ImageField(upload_to="productImages/DRF", blank=True)
    url = models.URLField(max_length=200, blank=True, null=True)
    pdf = models.FileField(upload_to='pdfs/DRF', blank=True)


class DjangoLibrary(models.Model):
    title = models.CharField(max_length=355, blank=True)
    text = models.TextField(blank=True)
    question = models.TextField(max_length=255, blank=True)
    answer = models.TextField(blank=True)
    img = models.ImageField(upload_to="productImages/Django", blank=True)
    img2 = models.ImageField(upload_to="productImages/Django", blank=True)
    img3 = models.ImageField(upload_to="productImages/Django", blank=True)
    url = models.URLField(max_length=200, blank=True, null=True)
    pdf = models.FileField(upload_to='pdfs/Django', blank=True)
