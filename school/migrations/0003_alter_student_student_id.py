# Generated by Django 3.2.9 on 2021-11-24 07:18

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_auto_20211124_1007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='Student_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
