# Generated by Django 4.0.5 on 2022-06-30 21:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0003_review_critic_alter_review_recomendation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='start',
            new_name='stars',
        ),
    ]
