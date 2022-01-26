from rest_framework import serializers
from .models import Csv,Student

class FileSerializer(serializers.ModelSerializer):
  class Meta():
    model = Csv
    fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
  class Meta():
    model = Student
    fields = '__all__'