# Generated by Django 5.0.6 on 2024-06-27 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_alter_scope_options_article_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='scope',
            name='is_main',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
