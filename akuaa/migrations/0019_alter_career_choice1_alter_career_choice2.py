# Generated by Django 4.1 on 2023-03-19 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('akuaa', '0018_latestnews'),
    ]

    operations = [
        migrations.AlterField(
            model_name='career',
            name='choice1',
            field=models.CharField(choices=[('YES', 'Yes')], default='YES', max_length=3),
        ),
        migrations.AlterField(
            model_name='career',
            name='choice2',
            field=models.CharField(choices=[('YES', 'Yes')], default='YES', max_length=3),
        ),
    ]
