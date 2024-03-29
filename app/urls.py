from django.urls import path

from app import views
from app.views import AnnouncementViewSet, CommentViewSet, ModuleViewSet, SessionViewSet, get_session_comments, students, technical_mentors

from rest_framework import permissions
from rest_framework.routers import DefaultRouter

from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Schedule API",
      default_version='v1',
      description="Test description",
    #   terms_of_service="https://www.google.com/policies/terms/",
    #   contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


router = DefaultRouter()

router.register(r'modules',ModuleViewSet,basename='module')
router.register(r'announcements',AnnouncementViewSet,basename='announcement')
router.register(r'sessions',SessionViewSet,basename='session')
router.register(r'comments',CommentViewSet,basename='comment')


urlpatterns = [
   path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
   path('api/',views.api,name='api'),
   
   # comments
   # announcements
   path('api/announcements/', views.all_announcements,name=''),
   
   path("api/like/comment/<int:comment_id>/",views.like_comment,name="likes"),
    # announcements comments likes
   path("api/like/announcement/comment/<int:announcomment_id>/",views.like_announ_comment,name="announ-likes"),


   # sessions
   path('api/sessions/detail/', views.get_session_details,name=''),
   path('api/sessions/search/<str:session_query>/', views.get_available_session,name=''),
   
   # Create user api
   path('api/user/create/',views.UserCreateAPIView.as_view(),name=''),
   path('api/user/login/',views.LoginAPIView.as_view(),name=''),
   path('api/user/logout/',views.LogoutAPIView.as_view(),name=''),


      # Get profile
   path("api/user/<int:user_id>/profile/" ,views.get_profile,name="user-profile"),
    # update student profile
   path("api/user/<int:pk>/update/profile/", views.ProfileUpdateAPIview.as_view(), name="update-profile"),
    



   # add student to module
   path("api/module/<int:module_id>/student/<int:student_id>/",views.add_student,name="add-student"),
   path("api/student/<int:student_id>/modules/",views.get_student_modules,name='student-modules'),


   path("api/module/<int:module_id>/sessions/",views.get_module_sessions,name='module-sessions'),
   path("api/technical-mentor/<int:tm_id>/modules/",views.get_tm_modules,name='tm-modules'),
   path("api/technical-mentors/",views.technical_mentors,name=''),
   path("api/students",views.students,name=''),

   # get session comments
   path("api/session/<int:session_id>/comments/",views.get_session_comments,name='')


] + router.urls
