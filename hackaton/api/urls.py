from django.urls import path
import api.views as views


urlpatterns = [
    path('organizations/', views.OrganizationView.as_view({'get': 'all'})),
    path('groups/<int:page>', views.GroupView.as_view({'get': 'all'})),
    path('events/<int:page>', views.EventView.as_view({'get': 'all'})),
    path('predict_groups', views.PredictGroupsView.as_view({'get': 'all'})),
]