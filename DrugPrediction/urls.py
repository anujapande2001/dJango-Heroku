
from django.urls import path
from DrugPrediction import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('',views.drugPred),
    path('drugpred/', views.drugPred),
    path('fps/', views.fpsPred),
    path('fpspred/', views.fpsPred),
    path('medcost/', views.medcostPred),
    path('medcostpred/', views.medcostPred),
    path('custclass/', views.custclassPred),
    path('custclassPred/', views.custclassPred),
]