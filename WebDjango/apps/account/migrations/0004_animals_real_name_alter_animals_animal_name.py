# Generated by Django 4.2.6 on 2024-01-11 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_rename_role_id_userinfo_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='animals',
            name='real_name',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='animals',
            name='animal_name',
            field=models.CharField(max_length=3),
        ),
    ]
