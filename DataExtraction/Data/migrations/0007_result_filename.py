# Generated by Django 3.0.6 on 2020-10-13 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Data', '0006_delete_card'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='filename',
            field=models.CharField(default=' ', max_length=100),
            preserve_default=False,
        ),
    ]