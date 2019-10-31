##### book/urls.py

# 이하 작성
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views 

router = DefaultRouter()
router.register('book', views.BookViewSet)
router.register('diary',views.DiaryViewSet)

urlpatterns = [ 
    path('', include(router.urls)),
]

#