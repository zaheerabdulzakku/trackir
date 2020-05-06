from django.urls import path
from appone import views

app_name='appone'

urlpatterns = [
    path('',views.index.as_view(),name='index'),
    path('<int:pk>/',views.detaillist.as_view(),name='detail'),
    path('create/',views.createir.as_view(),name='create'),
    path('update/<int:pk>/',views.irUpdateView.as_view(),name='update'),
    path('delete/<int:pk>/',views.irDeleteView.as_view(),name='delete'),
]
