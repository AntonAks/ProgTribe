# Generated by Django 3.0.6 on 2020-06-05 04:37

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='banner_about_en',
            field=wagtail.core.fields.RichTextField(default='', null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='banner_about_uk',
            field=wagtail.core.fields.RichTextField(default='', null=True),
        ),
    ]
