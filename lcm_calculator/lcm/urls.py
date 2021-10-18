from django.urls import path
from . import views

urlpatterns = [
    path('', views.lcm, name='lcm' ),
    # path('lcm-of-<int:num1>-and-<int:num2>/', views.lcm_fun, name='lcm_fun'),
    path('lcm-calculator/', views.calculator, name='calculator' ),
]
