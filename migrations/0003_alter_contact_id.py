# Generated by Django 3.2.8 on 2021-12-02 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
