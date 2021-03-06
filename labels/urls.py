from django.urls import path

from labels import views


urlpatterns = [
    path('', views.LabelListView.as_view(), name='labels_list'),
    path('create/', views.LabelCreateView.as_view(), name='label_creation'),
    path('<int:pk>/update/', views.LabelUpdateView.as_view(), name='label_update'),
    path('<int:pk>/delete/', views.LabelDeleteView.as_view(), name='label_delete'),
]
