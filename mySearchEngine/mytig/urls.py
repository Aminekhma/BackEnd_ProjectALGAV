from mytig import views
from django.views.generic.base import RedirectView
from django.urls import path, re_path, register_converter, include
from mytig.utils import converters

# Contents mytig/utils/converters.py

register_converter(converters.RomanNumeralConverter, 'roman')
register_converter(converters.FloatConverter, 'float')

urlpatterns = [
    path('products/', views.ListeDeProduits.as_view()),
    path('availableproducts/', views.Availablelist.as_view()),
    path('coquillages/', views.Coquillageslist.as_view()),
    path('onsaleproducts/', views.PromoList.as_view()),
    path('product/<int:pk>/', views.DetailProduit.as_view()),
    path('onsaleproduct/<int:pk>/', views.PromoDetail.as_view()),
    path('decrementStock/<int:id>/<int:number>/',views.decrementStock.as_view()),
    path('incrementStock/<int:id>/<int:number>/',views.incrementStock.as_view()),
    path('changePercent/<int:id>/<float:percentage>/',views.changePercent.as_view()),
    path('invendu/<int:id>/<int:number>/',views.invendu.as_view()),

    path('transactions/',views.ListeDeTransactions.as_view()),
]
