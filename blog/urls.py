from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, BlogPostViewSet, CommentViewSet
from django.urls import path, include

router = DefaultRouter()
router.register('posts', BlogPostViewSet, basename='posts')
router.register('categories', CategoryViewSet)
router.register('comments', CommentViewSet)


urlpatterns = [
    path('', include(router.urls)),
]


