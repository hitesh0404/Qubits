# Generated by Django 5.1.3 on 2024-12-03 13:05

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_uuid',
            field=models.UUIDField(auto_created=True, default=uuid.UUID('c88e024f-fb2f-419f-b457-83bd826208ad'), primary_key=True, serialize=False),
        ),
    ]
