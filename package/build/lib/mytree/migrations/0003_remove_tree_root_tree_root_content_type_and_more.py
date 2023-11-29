# Generated by Django 4.2.7 on 2023-11-27 12:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('mytree', '0002_tree'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tree',
            name='root',
        ),
        migrations.AddField(
            model_name='tree',
            name='root_content_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype'),
        ),
        migrations.AddField(
            model_name='tree',
            name='root_object_id',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]