# Generated by Django 5.0.6 on 2024-06-14 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turismo', '0010_alter_alumno_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='imagenes'),
        ),
    ]
