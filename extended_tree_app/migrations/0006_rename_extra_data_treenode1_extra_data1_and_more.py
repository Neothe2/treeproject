# Generated by Django 4.2.7 on 2023-11-27 13:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('extended_tree_app', '0005_rename_additional_info_tree1_additional_info1_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='treenode1',
            old_name='extra_data',
            new_name='extra_data1',
        ),
        migrations.RenameField(
            model_name='treenode2',
            old_name='description',
            new_name='extra_data2',
        ),
    ]
