# Generated by Django 4.1 on 2023-03-18 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('akuaa', '0008_remove_career_choice1_remove_career_choice2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='career',
            name='choice1',
            field=models.CharField(choices=[('YES', 'Yes'), ('No', 'No')], default='YES', max_length=3),
        ),
        migrations.AddField(
            model_name='career',
            name='choice2',
            field=models.CharField(choices=[('YES', 'Yes'), ('No', 'No')], default='YES', max_length=3),
        ),
    ]
