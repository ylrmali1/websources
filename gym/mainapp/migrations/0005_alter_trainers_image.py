# Generated by Django 4.1 on 2022-10-30 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_alter_trainers_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainers',
            name='image',
            field=models.ImageField(null=True, upload_to='trainers'),
        ),
    ]
