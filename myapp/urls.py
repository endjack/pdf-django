from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.index, name='index'),

    path('pdf_pdfkit/<str:type>', pdf_from_template, name='pdfkit'), 

]