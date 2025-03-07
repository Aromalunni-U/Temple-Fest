# Generated by Django 5.0.6 on 2024-06-14 16:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price_per_hour', models.DecimalField(decimal_places=2, max_digits=10)),
                ('address', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(default='static/service images/Festiconnect.png', upload_to='static/service images')),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
