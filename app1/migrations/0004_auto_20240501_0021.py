# Generated by Django 3.2.25 on 2024-04-30 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_rename_products_patiance'),
    ]

    operations = [
        migrations.CreateModel(
            name='patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200, null=True)),
                ('DiseaseName', models.CharField(max_length=200, null=True)),
                ('Result', models.BooleanField()),
            ],
        ),
        migrations.DeleteModel(
            name='patiance',
        ),
    ]