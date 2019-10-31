from django.db import models
from django.conf import settings

class Book(models.Model): # 책 정보 모델
    user = models.ForeignKey(settings.AUTH_USER_MODEL,default = 1,on_delete=models.CASCADE) # 작성 유저
    title = models.CharField(max_length=50,blank=True) # 책 제목
    author = models.CharField(max_length=50,blank=True) # 책 작가
    content = models.TextField(blank=True) # 책 줄거리
    cover = models.ImageField(upload_to='covers') # 책 표지


class Diary(models.Model): 
    user = models.ForeignKey(settings.AUTH_USER_MODEL,default = 1,on_delete=models.CASCADE)  
    content = models.TextField(blank=True) 
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    diary_file = models.FileField(upload_to='files',null=True) # 파일필드, upload_to => 파일 저장 경로