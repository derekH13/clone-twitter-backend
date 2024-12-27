
from django.contrib import admin
from django.urls import path, include
# para auth
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/', include('cadastro.urls'), name='user_urls'),
    path('feed/', include('feed.urls'), name='feed_urls'),
]
