from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from main import views
from main.views import *

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', Login, name="login"),
                  path('signup/', SignUp, name="signup"),
                  path('logout/', Logout, name='logout'),
                  path('ForgetPassword/', ForgetPassword, name="forget-password"),
                  path('change_password/<token>/', ChangePassword, name='change_password'),
                  path('home/', home, name="home"),
                  path('search/', search, name="search"),
                  path('python01/', python01, name="python01"),
                  path('python_page/', python_page, name="python_page"),
                  path('python_meaning/', python_meaning_view, name='python_meaning'),
                  path('sql_details/', sql_details_view, name='sql_details'),

                  path('python_scraping/', python_scraping, name='python_scraping'),

                  # Testing -----------------------------------------------

                  path('pytest/', pytest, name='pytest'),

                  # Django ------------------------------------------------
                  path('django_app/', include('django_app.urls')),

                  # python module and libraries--------------------------
                  path('python_modules_libraries/', python_modules_libraries, name='python_modules_libraries'),
                  path('regex_module/', regex_module, name='regex_module'),
                  path('pandas_library/', pandas_library, name='pandas_library'),
                  path('python_other_important_libraries/', python_other_important_libraries,
                       name='python_other_important_libraries'),
                  # -----------------------------------------------------

                  path('interview_questions/', interview_questions_view, name="interview_questions"),
                  path('random_questions/', random_questions_view, name="random_questions"),
                  path('small_type_interview_questions/', small_type_interview_questions, name="small_questions"),
                  path('long_type_interview_questions/', long_type_interview_questions, name="long_questions"),
                  path('python_programming_questions/', python_programming_questions,
                       name="python_programming_questions"),
                  path('small_sql_questions/', small_sql_questions, name="small_sql_questions"),

                  path('payment_gateway/', payment_gateway, name="payment_gateway"),
                  # random -----------------------------------------------
                  path('error_handling/', error_handling_view, name="error_handling"),
                  path('status_code/', status_code, name="status code"),
                  path('aws/', AWS, name="aws"),
                  path('scrum/', scrum_detail, name="scrum"),
                  path('git/', git, name="git"),

                  # path('api/<id>', api_question, name="api_question"),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
