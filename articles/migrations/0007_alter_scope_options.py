# Generated by Django 5.0.6 on 2024-06-27 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_alter_scope_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='scope',
            options={'ordering': ['-is_main'], 'verbose_name': 'Раздел', 'verbose_name_plural': 'Разделы'},
        ),
    ]
