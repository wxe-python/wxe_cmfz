# Generated by Django 2.0.6 on 2020-04-14 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20200414_2322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='cover',
            field=models.ImageField(upload_to='pics/pics'),
        ),
        migrations.AlterField(
            model_name='chapter',
            name='url',
            field=models.CharField(max_length=255),
        ),
    ]