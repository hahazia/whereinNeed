# Generated by Django 2.2.11 on 2020-03-26 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='charity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('mission', models.TextField()),
                ('webURL', models.URLField()),
                ('ein', models.IntegerField()),
                ('city', models.CharField(max_length=50)),
                ('zipCode', models.IntegerField(null=True)),
                ('addr', models.TextField(blank=True)),
                ('category', models.ManyToManyField(blank=True, to='myapp.Categ')),
            ],
        ),
    ]
