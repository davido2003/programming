# Generated by Django 3.2.7 on 2021-10-16 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new', '0003_alter_programmingnewsapi_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='programmingnewsapi',
            name='description',
            field=models.CharField(default=2, max_length=3000),
            preserve_default=False,
        ),
    ]
