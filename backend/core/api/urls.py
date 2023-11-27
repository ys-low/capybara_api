from django.urls import path,include
from api.views import CapyList,CapyDetail
app_name="api"
urlpatterns = [
     path("capybara_list/",CapyList.as_view(),name='capybara_list'),
     path("capybara_detail/<int:pk>/",CapyDetail.as_view(),name='capybara_detail'),
     

]
