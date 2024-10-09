# Generated by Django 5.1.1 on 2024-10-07 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='duration',
            field=models.FloatField(null=True, verbose_name='Продолжительность'),
        ),
        migrations.AddField(
            model_name='movie',
            name='genres',
            field=models.CharField(default=1, help_text='Максимум 50 символов', max_length=50, verbose_name='Жанр'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='movie',
            name='video',
            field=models.URLField(verbose_name='Фильм'),
        ),
    ]
