# Generated by Django 2.1.7 on 2019-04-24 21:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('realty', '0002_remove_realty_type'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='apartment',
            options={'base_manager_name': 'objects'},
        ),
        migrations.AlterModelOptions(
            name='building',
            options={'base_manager_name': 'objects'},
        ),
        migrations.AlterModelOptions(
            name='realty',
            options={'base_manager_name': 'objects'},
        ),
        migrations.AddField(
            model_name='realty',
            name='polymorphic_ctype',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_realty.realty_set+', to='contenttypes.ContentType'),
        ),
    ]