# Generated by Django 2.2 on 2020-05-04 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0005_auto_20200504_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classmodel',
            name='toDo',
            field=models.CharField(max_length=200),
        ),
        migrations.DeleteModel(
            name='ToDoList',
        ),
    ]
