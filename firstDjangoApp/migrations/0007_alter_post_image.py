# Generated by Django 4.1 on 2022-08-22 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstDjangoApp', '0006_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
