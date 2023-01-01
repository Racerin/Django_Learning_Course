from django.urls import path

from . import views
from polls import views as original_views

app_name = "generic_polls"
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results', views.ResultsView.as_view(), name='results'),
    # path('<int:question_id>/vote', views.vote, name='vote'),
    path('<int:question_id>/vote', original_views.vote, name='vote'),
]