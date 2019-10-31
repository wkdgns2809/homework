from rest_framework import serializers
from .models import Book,Diary

class BookSerializer(serializers.ModelSerializer):
		
		# user 필드를 읽기 전용으로 설정
    user_name = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Book
        fields = ('pk','user_name','title','author','content','cover')


class DiarySerializer(serializers.ModelSerializer):
    user_name = serializers.ReadOnlyField(source='user.username')

    class Meta: 
        model = Diary
        fields = ('pk','user_name','content','created_at','updated_at','diary_file')
  