# Generated by Django 4.1.3 on 2022-11-09 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team_member_add', '0003_alter_teammember_phonenumber_alter_teammember_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teammember',
            name='phoneNumber',
            field=models.PositiveBigIntegerField(max_length=10),
        ),
    ]
