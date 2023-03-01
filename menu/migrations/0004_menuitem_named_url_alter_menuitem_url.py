# Generated by Django 4.1.7 on 2023-02-27 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_alter_menuitem_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='named_url',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='url',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
    ]
