from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.upload, name='upload'),
    path('job/', views.job_list, name='job_list'),
    path('job/<int:job_posting_id>', views.predict, name = 'predict')
]