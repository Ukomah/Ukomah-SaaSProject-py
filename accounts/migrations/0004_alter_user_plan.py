# Generated by Django 4.1.5 on 2023-04-03 13:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_user_plan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='plan',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='users', to='accounts.plan'),
        ),
    ]
