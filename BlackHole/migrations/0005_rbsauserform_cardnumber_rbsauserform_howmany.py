# Generated by Django 4.1.3 on 2022-11-24 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlackHole', '0004_simpleuserformone_alter_userformpy_user_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='rbsauserform',
            name='cardnumber',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='rbsauserform',
            name='howmany',
            field=models.CharField(default='', max_length=50),
        ),
    ]
