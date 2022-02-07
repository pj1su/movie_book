from django.urls import path
from . import views

app_name="review"

urlpatterns=[
  path("<int:pk>",views.Reivew_View.as_view(),name="add_review"),
  path("<int:pk>",views.create_review,name="review"),
]
