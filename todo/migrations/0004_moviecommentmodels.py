# Generated by Django 5.1.1 on 2024-10-10 16:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_movie_director_alter_movie_duration'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovieCommentModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('rating', models.CharField(choices=[('*', '*'), ('**', '**'), ('***', '***'), ('****', '****'), ('*****', '*****')], max_length=55)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('movie_choice_comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='todo.movie')),
            ],
        ),
    ]
