# Generated by Django 2.1.7 on 2019-05-01 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('realty', '0003_auto_20190425_0005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realtyphoto',
            name='realty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='realty.Realty'),
        ),
    ]