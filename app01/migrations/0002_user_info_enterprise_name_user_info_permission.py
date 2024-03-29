# Generated by Django 5.0.3 on 2024-03-07 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_info',
            name='enterprise_name',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='企业名'),
        ),
        migrations.AddField(
            model_name='user_info',
            name='permission',
            field=models.CharField(choices=[('A', 'Admin'), ('C', 'Client'), ('E', 'Enterprise')], default='C', max_length=1),
        ),
    ]
