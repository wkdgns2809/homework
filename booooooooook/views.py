##### book/views.py

# 이하 작성
from rest_framework import viewsets
from .serializers import BookSerializer, DiarySerializer
from .models import Book,Diary
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser,FormParser
from rest_framework.pagination import PageNumberPagination
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class Custom_pagination(PageNumberPagination): # 페이지네이션 옵션 클래스
    page_size = 5 # 페이지를 나누는 기준 

class BookViewSet(viewsets.ModelViewSet): 
    queryset = Book.objects.all()
    serializer_class = BookSerializer  
    pagination_class = Custom_pagination # 생성한 페이지네이션 옵션 설정
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]
    permission_classes = [IsAuthenticated]

    def perform_create(self,serializer):
        serializer.save(user=self.request.user)


    filter_backends = [SearchFilter]
    search_fields = ('author','title') # 검색 기준이 되는 필드 설정
		
    def perform_create(self,serializer):
        serializer.save(user=self.request.user)
        
    
class DiaryViewSet(viewsets.ModelViewSet): 
    queryset = Diary.objects.all()
    serializer_class = DiarySerializer  

    filter_backends = [SearchFilter]
    search_fields = ('content','updated_at') # 검색 기준이 되는 필드 설정

    def perform_create(self,serializer):
        serializer.save(user=self.request.user)
		
		# 사용자가 작성한 글만 필터
    def get_queryset(self):
        qs = super().get_queryset()

        if self.request.user.is_authenticated:
            qs = qs.filter(user = self.request.user)
        else:
            qs = qs.none()
        return qs
        
        
        parser_classes = (MultiPartParser,FormParser)

    def post(self,request,*args,**kwargs):
        serializer = DiarySerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=HTTP_201_CREATED)
        else:
            return Response(serializer.error,status=HTTP_400_BAD_REQUEST)

class Custom_pagination(PageNumberPagination): # 페이지네이션 옵션 클래스
    page_size = 5 # 페이지를 나누는 기준 

