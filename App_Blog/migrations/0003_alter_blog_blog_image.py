# Generated by Django 4.2.7 on 2023-12-01 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Blog', '0002_alter_comment_blog_alter_likes_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blog_image',
            field=models.ImageField(upload_to='Uploaded/Blog_App/Blog_Posts_Image'),
        ),
    ]
