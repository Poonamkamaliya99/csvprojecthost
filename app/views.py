from django.shortcuts import render,HttpResponse
from .models import Csv,Student
from django.contrib import messages

import csv
import os



def upload(request):
    if request.method=="POST":
              
        file_name=request.POST.get('file_name')
        myfile=request.FILES.get('myfile')
        
        file =Csv(file_name=file_name,myfile=myfile)
        try:
            file.save()
        except Exception :
            print(file)
        messages.success(request, 'Your message has been sent')
        
        read_csv(request)
   
    return render(request,'upload.html')






def read_csv(request):
    read_file=os.listdir('media/csv/')
    print(read_file)
    
    file=read_file[0]
    
    with open('media/csv/'+file, 'r') as f:
        print(f)
        reader=csv.reader(f)
        data=[]
        count=0
        primary_counter=0
        secondary_counter=0
        for row in reader:
            if count==0 or count==1:
                count=count+1
                pass
            else:
                data.append(row)
     
        
        for i in data:
            print(i)
        
        
        
        
        for i in range(len(data)):
            if primary_counter>len(data):
                break
               
            student=Student.objects.create( fname=data[primary_counter][secondary_counter], lname=data[primary_counter][secondary_counter+1], city=data[primary_counter][secondary_counter+2])
            primary_counter = primary_counter+1
            # secondary_counter = secondary_counter+1
            
    
    os.remove('media/csv/'+file)           
    return HttpResponse('upload' )


from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import FileSerializer,StudentSerializer
from rest_framework.generics import CreateAPIView
from .models import Csv,Student


class FileCreateAPIView(CreateAPIView):
    queryset=Csv.objects.all()
    serializer_class=FileSerializer
    



@api_view(['GET'])
def CsvList(request):
    csv=Csv.objects.all()
    serializer=FileSerializer(csv, many=True)
    return Response(serializer.data)







@api_view(['GET'])
def StudentList(request):
    s=Student.objects.all()
    serializer=StudentSerializer(s, many=True)
    return Response(serializer.data)

