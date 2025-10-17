from django.urls import path
from .views import landing_page, project_list

urlpatterns = [
    path('', landing_page, name='landing_page'),           # Root URL: your landing page
    path('projects/', project_list, name='project_list'),  # Projects page at /projects/
]
from .views import landing_page, project_list, experience_list, education_list

urlpatterns = [
    path('', landing_page, name='landing_page'),
    path('projects/', project_list, name='project_list'),
    path('experience/', experience_list, name='experience_list'),
    path('education/', education_list, name='education_list'),
]
