# Generated by Django 3.2.7 on 2021-09-09 04:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_article_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='image_thumb',
        ),
    ]