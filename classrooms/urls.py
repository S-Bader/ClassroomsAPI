
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from classes import views
from api import views as api_views
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('classrooms/', views.classroom_list, name='classroom-list'),
    path('classrooms/<int:classroom_id>/', views.classroom_detail, name='classroom-detail'),

    path('classrooms/create', views.classroom_create, name='classroom-create'),
    path('classrooms/<int:classroom_id>/update/', views.classroom_update, name='classroom-update'),
    path('classrooms/<int:classroom_id>/delete/', views.classroom_delete, name='classroom-delete'),

    # API Views
    path('api/classrooms/', api_views.ClassroomListView.as_view()),
    path('api/classrooms/create/', api_views.ClassroomCreateView.as_view()),
    path('api/classrooms/<int:classroom_id>/', api_views.ClassroomUpdateView.as_view()),
    path('api/classrooms/<int:classroom_id>/update/', api_views.ClassroomDetailView.as_view()),
    path('api/classrooms/<int:classroom_id>/delete/', api_views.ClassroomDeleteView.as_view()),
    path('login/', TokenObtainPairView.as_view()),
]

if settings.DEBUG:
	urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
