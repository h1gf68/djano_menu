# Generated by Django 4.1.7 on 2023-02-27 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_remove_menuitem_css_class_menu_css_class_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='url',
            field=models.SlugField(blank=True, default='', null=True),
        ),
    ]