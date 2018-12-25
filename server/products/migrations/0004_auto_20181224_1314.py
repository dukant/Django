# Generated by Django 2.1.4 on 2018-12-24 10:14
import json
from django.db import migrations

def create_categories(apps, schema_editor):
    model_class = apps.get_model('products.category')
    with open('products\Fixtures\categories.json', 'r') as file:
        for data in json.load(file):
            model_class.objects.create(
                name=data.get('name')
            )


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_category'),
    ]

    operations = [
        migrations.RunPython(
            create_categories,
            lambda x,y:(x,y)
        )
    ]
