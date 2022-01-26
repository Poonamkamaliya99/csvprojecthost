from django.urls import path
from app import views

urlpatterns = [
    
    path("upload",views.upload , name="upload"),
    path("read_csv",views.read_csv , name="read_csv"),


    path('filecrt/', views.FileCreateAPIView.as_view(), name='filecrt'),

    path('csvlist/', views.CsvList, name='csvlist'),

    path('slist/', views.StudentList, name='slist'),

]

