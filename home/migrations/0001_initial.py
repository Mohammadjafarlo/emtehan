# Generated by Django 5.0.1 on 2024-03-02 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='madahyha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('matn', models.TextField()),
                ('Music', models.FileField(upload_to='<django.db.models.fields.CharField>/')),
            ],
        ),
    ]