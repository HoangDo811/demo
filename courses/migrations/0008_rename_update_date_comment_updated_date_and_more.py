# Generated by Django 4.1.7 on 2023-04-25 16:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_alter_rating_rate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='update_date',
            new_name='updated_date',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='update_date',
            new_name='updated_date',
        ),
        migrations.RenameField(
            model_name='lesson',
            old_name='update_date',
            new_name='updated_date',
        ),
        migrations.RenameField(
            model_name='like',
            old_name='update_date',
            new_name='updated_date',
        ),
        migrations.RenameField(
            model_name='rating',
            old_name='update_date',
            new_name='updated_date',
        ),
        migrations.RenameField(
            model_name='tag',
            old_name='update_date',
            new_name='updated_date',
        ),
    ]
