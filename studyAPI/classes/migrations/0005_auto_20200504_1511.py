# Generated by Django 2.2 on 2020-05-04 13:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0004_classmodel_todo'),
    ]

    operations = [
        migrations.CreateModel(
            name='ToDoList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='classmodel',
            name='toDo',
            field=models.ForeignKey(default=12312313, on_delete=django.db.models.deletion.CASCADE, to='classes.ToDoList'),
            preserve_default=False,
        ),
    ]
