import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from mytig.config import baseUrl
from mytig.models import Produit
from mytig.models import Transaction
from mytig.serializers import ProduitSerializer
from mytig.serializers import TransactionSerializer

# Create your views here.
class ListeDeProduitss(APIView):
    def get(self, request, format=None):
        res = []
        queryset = Produit.objects.all()
        for p in queryset:
            res.append(ProduitSerializer(p).data)
        return Response(res)
#    def post(self, request, format=None):
#        NO DEFITION of post --> server will return "405 NOT ALLOWED"

class ListTransaction(APIView):
    def get(self, request, format=None):
        res = []
        queryset = Transaction.objects.all()
        for p in queryset:
            res.append(TransactionSerializer(p).data)
        return Response(res)

class ListeDeProduits(APIView):
    def get(self, request, format=None):
        res = []
        queryset = Produit.objects.all()
        for p in queryset:
            res.append(ProduitSerializer(p).data)
        return Response(res)

class DetailProduit(APIView):
    def get_object(self, pk):
        try:
            queryset = Produit.objects.get(tigID = pk)
            response = ProduitSerializer(queryset).data
            return response
        except:
            raise Http404
    def get(self, request, pk, format=None):
        response = self.get_object(pk)
        return Response(response)
    def patch(self, request, pk, format=None):
        response = self.get_object(pk)
        return Response(response)

class decrementStock(APIView):
    def get_object(self, id):
        try:
            queryset = Produit.objects.get(tigID = id)
            return queryset
        except Produit.DoesNotExist:
            raise Http404
    def get(self, request, id, number,format=None):

        prod = self.get_object(id)
        if(prod.quantity<= 0):
            return Response(ProduitSerializer(prod).data)
        else:
            prod.quantity = prod.quantity - number
            prod.save()
            response = ProduitSerializer(prod).data
            return Response(response)

class incrementStock(APIView):
    def get_object(self, id):
        try:
            queryset = Produit.objects.get(tigID = id)
            return queryset
        except Produit.DoesNotExist:
            raise Http404
    def get(self, request,format=None):
        prod = self.get_object(id)
        prod.quantity = prod.quantity + number
        prod.save()
        response = ProduitSerializer(prod).data

        return Response(response)


class changePercent(APIView):
    def get_object(self, id):
        try:
            queryset = Produit.objects.get(tigID = id)
            return queryset
        except Produit.DoesNotExist:
            raise Http404
    def get(self, request, id, percentage,format=None):
        if percentage > 100.0 or percentage < 0.0:
            return Response({ "error_message" : "Incorrect Value"})
        else:
            prod = self.get_object(id)
            prod.discount_percent = percentage
            newprice = prod.price - (1.0 - (percentage/100.0))
            prod.discount_price = round(newprice,2)
            prod.save()
            response = ProduitSerializer(prod).data
            return Response(response)



from mytig.models import ProduitAvailable
from mytig.serializers import ProduitAvailableSerializer
from mytig.models import ProduitCoquillages
from mytig.serializers import ProduitCoquillagesSerializer
from mytig.models import ProduitEnPromotion
from mytig.serializers import ProduitEnPromotionSerializer
from django.http import Http404
from django.http import JsonResponse

class Availablelist(APIView):
    def get(self, request, format=None):
        res=[]
        for prod in Produit.objects.all():
            serializer = ProduitAvailableSerializer(prod)
            response = requests.get(baseUrl+'product/'+str(serializer.data['tigID'])+'/')
            jsondata = response.json()
            res.append(jsondata)
        return JsonResponse(res, safe=False)
#    def post(self, request, format=None):
#        NO DEFITION of post --> server will return "405 NOT ALLOWED"

class Coquillageslist(APIView):
    def get(self, request, format=None):
        res=[]
        for prod in ProduitCoquillages.objects.all():
            serializer = ProduitCoquillagesSerializer(prod)
            response = requests.get(baseUrl+'product/'+str(serializer.data['tigID'])+'/')
            jsondata = response.json()
            res.append(jsondata)
        return JsonResponse(res, safe=False)
#    def post(self, request, format=None):
#        NO DEFITION of post --> server will return "405 NOT ALLOWED"

class PromoList(APIView):
    def get(self, request, format=None):
        res=[]
        for prod in ProduitEnPromotion.objects.all():
            serializer = ProduitEnPromotionSerializer(prod)
            response = requests.get(baseUrl+'product/'+str(serializer.data['tigID'])+'/')
            jsondata = response.json()
            res.append(jsondata)
        return JsonResponse(res, safe=False)
#    def post(self, request, format=None):
#        NO DEFITION of post --> server will return "405 NOT ALLOWED"

class PromoDetail(APIView):
    def get_object(self, pk):
        try:
            return ProduitEnPromotion.objects.get(pk=pk)
        except ProduitEnPromotion.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        prod = self.get_object(pk)
        serializer = ProduitEnPromotionSerializer(prod)
        response = requests.get(baseUrl+'product/'+str(serializer.data['tigID'])+'/')
        jsondata = response.json()
        return Response(jsondata)
#    def put(self, request, pk, format=None):
#        NO DEFITION of put --> server will return "405 NOT ALLOWED"
#    def delete(self, request, pk, format=None):
#        NO DEFITION of delete --> server will return "405 NOT ALLOWED"

  