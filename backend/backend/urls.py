
from django.contrib import admin
from django.urls import path, include
from reviews.views import ProductViewSet,  CommentViewSet
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static


router = DefaultRouter()
router.register(r'product', ProductViewSet, basename='Product')
# router.register(r'image', ImageViewSet, basename='Image')
router.register(r'comment', CommentViewSet, basename='Comment')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('auth.urls')),
    path('', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)