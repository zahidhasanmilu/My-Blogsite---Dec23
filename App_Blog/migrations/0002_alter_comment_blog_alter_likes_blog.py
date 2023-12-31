# Generated by Django 4.2.7 on 2023-11-26 10:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App_Blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='blog',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_comment', to='App_Blog.blog'),
        ),
        migrations.AlterField(
            model_name='likes',
            name='blog',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_like', to='App_Blog.blog'),
        ),
    ]
