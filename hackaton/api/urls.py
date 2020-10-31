from django.urls import path
import api.views as views


urlpatterns = [
    path('organizations/', views.OrganizationView.as_view({'get': 'all'})),

]