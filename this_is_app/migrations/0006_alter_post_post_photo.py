# Generated by Django 5.1.4 on 2024-12-28 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('this_is_app', '0005_alter_post_post_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_photo',
            field=models.FileField(blank=True, default='media/urodlivaya_zalupa.webp', null=True, upload_to='post_photo'),
        ),
    ]