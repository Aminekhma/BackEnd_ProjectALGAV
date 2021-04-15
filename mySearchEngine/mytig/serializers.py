from rest_framework.serializers import ModelSerializer
from mytig.models import ProduitEnPromotion
from mytig.models import ProduitAvailable
from mytig.models import ProduitCoquillages
from mytig.models import Produit

class ProduitEnPromotionSerializer(ModelSerializer):
    class Meta:
        model = ProduitEnPromotion
        fields = ('id', 'tigID')

class ProduitAvailableSerializer(ModelSerializer):
    class Meta:
        model = ProduitAvailable
        fields = ('id', 'tigID')


class ProduitCoquillagesSerializer(ModelSerializer):
    class Meta:
        model = ProduitCoquillages
        fields = ('id', 'tigID')

class ProduitSerializer(ModelSerializer):
    class Meta:
        model = Produit
        fields = (
            'tigID', 
            'name',
            'price',
            'discount_price',
            'discount_percent',
            'quantity',
            'sales_number',
            'comments', 
        )