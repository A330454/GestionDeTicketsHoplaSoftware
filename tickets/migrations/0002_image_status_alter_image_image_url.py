# Generated by Django 5.0.6 on 2024-05-30 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('completed', 'Completed')], default='pending', max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='image',
            name='image_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
