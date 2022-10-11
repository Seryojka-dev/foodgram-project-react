import json
import logging

from django.core.management.base import BaseCommand
from recipes.models import Ingredient


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('data/ingredients.json', 'rb') as f:
            data = json.load(f)
            for i in data:
                ingredient = Ingredient()
                ingredient.name = i['name']
                ingredient.measurement_unit = i['measurement_unit']
                ingredient.save()
                logging.basicConfig(level=logging.INFO)
                logging.info(i['name'], i['measurement_unit'])
