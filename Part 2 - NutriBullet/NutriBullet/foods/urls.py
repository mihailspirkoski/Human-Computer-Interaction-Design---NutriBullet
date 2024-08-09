from django.urls import path
from . import views


app_name='foods'

urlpatterns = [
    path('<slug:food_type>', views.foods_list, name="list"),
    path('<slug:food_type>/<slug:slug>', views.food_page, name="page")

]