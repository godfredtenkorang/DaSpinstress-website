# Generated by Django 4.1 on 2023-03-18 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('akuaa', '0010_alter_career_cover_letter_alter_career_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='career',
            name='cover_letter',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
