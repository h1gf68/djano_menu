# Generated by Django 4.1.7 on 2023-02-27 17:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menuitem',
            name='css_class',
        ),
        migrations.AddField(
            model_name='menu',
            name='css_class',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='menu.menuitem'),
        ),
    ]
