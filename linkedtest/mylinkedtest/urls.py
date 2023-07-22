from django.urls import path
from .views import *


urlpatterns = [
    path('', Questions.as_view(), name='my_q'),
    path('<int:pk>', Qu_detail.as_view(), name='my_q_det'),

]
