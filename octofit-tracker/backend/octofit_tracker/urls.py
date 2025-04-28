from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from octofit import views as octofit_views

router = DefaultRouter()
router.register(r'users', octofit_views.UserViewSet)
router.register(r'teams', octofit_views.TeamViewSet)
router.register(r'activities', octofit_views.ActivityViewSet)
router.register(r'leaderboards', octofit_views.LeaderboardViewSet)
router.register(r'workouts', octofit_views.WorkoutViewSet)

urlpatterns = [
    path('', octofit_views.api_root, name='api-root'),
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
]
