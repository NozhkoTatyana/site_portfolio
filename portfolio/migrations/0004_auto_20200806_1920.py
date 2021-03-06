# Generated by Django 3.0.7 on 2020-08-06 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_project_img'),
    ]

    operations = [
        migrations.RenameField(
            model_name='design',
            old_name='imgcdesign',
            new_name='imgd',
        ),
        migrations.AddField(
            model_name='certificate',
            name='imgc',
            field=models.ImageField(default='', upload_to='certificate_folder'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='design',
            name='imgdesign',
            field=models.ImageField(default=2, upload_to='design_folder'),
            preserve_default=False,
        ),
    ]
