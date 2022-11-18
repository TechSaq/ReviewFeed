# Generated by Django 4.1.1 on 2022-11-15 17:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0002_review_item_alter_media_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='item',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='review_item', to='item.item'),
            preserve_default=False,
        ),
    ]
