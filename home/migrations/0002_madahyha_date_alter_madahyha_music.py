# Generated by Django 5.0.1 on 2024-03-02 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='madahyha',
            name='date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='madahyha',
            name='Music',
            field=models.FileField(upload_to='%Y/%m/%d/'),
        ),
    ]