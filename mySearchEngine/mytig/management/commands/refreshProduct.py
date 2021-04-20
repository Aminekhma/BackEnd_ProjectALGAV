from django.core.management.base import BaseCommand, CommandError
from mytig.models import Produit
from mytig.config import baseUrl
import requests
import time

class Command(BaseCommand):
    help = 'Refresh the list of products which are on sale.'

    def handle(self, *args, **options):
        self.stdout.write('['+time.ctime()+'] Refreshing data...')
        response = requests.get(baseUrl+'products/')
        jsondata = response.json()
        Produit.objects.all().delete()
        for product in jsondata:
            p = Produit(
                tigID = product['id'],
                name = product['name'],
                price = product['price'],
                discount_price = product['discount'],
                comments = product['comments'],
                category = product['category']
            )
            p.save()
            self.stdout.write(self.style.SUCCESS('['+time.ctime()+'] Successfully added product id="%s"' % product['id']))
        self.stdout.write('['+time.ctime()+'] Data refresh terminated.')