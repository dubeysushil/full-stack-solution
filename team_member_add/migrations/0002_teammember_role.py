# Generated by Django 4.1.3 on 2022-11-09 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team_member_add', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teammember',
            name='role',
            field=models.CharField(choices=[('0', "Regular - Can't delete members"), ('1', 'Admin - Can delete members')], default='Admin', max_length=50),
            preserve_default=False,
        ),
    ]
