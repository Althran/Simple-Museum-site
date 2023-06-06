from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:id>/', views.post_detail, name='detail'),
    path('stands/', views.StandsTemplateView.as_view(), name='stands'),
    path('eksponaty/', views.item_list, name='item_list'),
    path('contacts/', views.ContactTemplateView.as_view(), name='contacts'),
]
