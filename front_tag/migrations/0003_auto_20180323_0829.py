# Generated by Django 2.0.3 on 2018-03-23 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front_tag', '0002_auto_20180323_0814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='norma',
            name='norm_text',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='norma',
            name='norm_url',
            field=models.CharField(max_length=10000),
        ),
    ]