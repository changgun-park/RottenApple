# Generated by Django 3.2.3 on 2021-11-22 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0003_alter_article_like_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='rate',
            field=models.IntegerField(default=0),
        ),
    ]