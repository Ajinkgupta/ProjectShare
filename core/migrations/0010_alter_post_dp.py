# Generated by Django 4.1.7 on 2023-04-01 07:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_alter_post_dp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='dp',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.profile'),
        ),
    ]