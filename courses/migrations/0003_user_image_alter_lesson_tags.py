# Generated by Django 4.1.7 on 2023-04-21 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_tag_lesson'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(null=True, upload_to='users/%Y/%m'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='tags',
            field=models.ManyToManyField(related_name='lessons', to='courses.tag'),
        ),
    ]
