from django.urls import path
import api.views as views


urlpatterns = [
    path('organizations/', views.OrganizationView.as_view({'get': 'all'})),
    path('groups/<int:page>', views.GroupView.as_view({'get': 'all'})),
]