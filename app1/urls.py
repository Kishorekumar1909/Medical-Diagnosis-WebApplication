from django.urls import path
from .views import *
from .app import *

urlpatterns =[
    path("home/",home),
    path("diabetes/",diabetesPage),
    path("cancer/",cancerPage),
    path("heart/",heartPage),
    path("liver/",liverPage),
    path("kidney/",kidneyPage),
    path("malaria/",malariaPage),
    path("pneumonia/",pneumoniaPage),
    path("malariapredict/",malariapredictPage),
    path("pneumoniapredict/",pneumoniapredictPage),
    path("malariapredict",malariapredictPage),
    path("pneumoniapredict",pneumoniapredictPage),
    path("predict/",predictPage),
    path("predict",predictPage),
    path("index/",index),
    path("about/",aboutpage),
    path("contact/",contactpage),
    path("icon/",iconpage),
    path("service/",servicepage),
]
