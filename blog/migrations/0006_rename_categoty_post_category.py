# Generated by Django 5.0.6 on 2024-05-19 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_category_post_categoty'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='categoty',
            new_name='category',
        ),
    ]
