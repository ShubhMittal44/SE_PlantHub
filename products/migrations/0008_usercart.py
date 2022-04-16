# Generated by Django 3.2.5 on 2021-10-12 05:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0007_auto_20211010_1959'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.IntegerField()),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.itemmain')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]