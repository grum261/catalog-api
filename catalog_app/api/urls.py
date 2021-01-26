from rest_framework.routers import DefaultRouter
from .views import ApplicantViewSet


router = DefaultRouter()

router.register(r'applicant', ApplicantViewSet, basename='applicant')

urlpatterns = router.urls