# Generated by Django 5.1.2 on 2024-11-04 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checklist', '0005_alter_checklist_brake_fluid_comment_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='checklist',
            name='headlights_comment',
            field=models.CharField(blank=True, max_length=40, verbose_name='Headlights comment'),
        ),
        migrations.AddField(
            model_name='checklist',
            name='headlights_flag',
            field=models.IntegerField(choices=[(1, 'Critical'), (2, 'Need correction'), (3, 'OK')], default=3, verbose_name='Headlights status'),
        ),
        migrations.AddField(
            model_name='checklist',
            name='headlights_mark',
            field=models.IntegerField(choices=[(0, 'NO'), (1, 'YES'), (2, 'N/A')], default=1, verbose_name='Headlights mark'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='checklist',
            name='reversing_lights_comment',
            field=models.CharField(blank=True, max_length=40, verbose_name='Reversing lights comment'),
        ),
        migrations.AddField(
            model_name='checklist',
            name='reversing_lights_flag',
            field=models.IntegerField(choices=[(1, 'Critical'), (2, 'Need correction'), (3, 'OK')], default=3, verbose_name='Reversing lights status'),
        ),
        migrations.AddField(
            model_name='checklist',
            name='reversing_lights_mark',
            field=models.IntegerField(choices=[(0, 'NO'), (1, 'YES'), (2, 'N/A')], default=1, verbose_name='Reversing lights mark'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='checklist',
            name='turn_and_stop_lights_comment',
            field=models.CharField(blank=True, max_length=40, verbose_name='Turn and stop lights comment'),
        ),
        migrations.AddField(
            model_name='checklist',
            name='turn_and_stop_lights_flag',
            field=models.IntegerField(choices=[(1, 'Critical'), (2, 'Need correction'), (3, 'OK')], default=3, verbose_name='Turn and stop lights status'),
        ),
        migrations.AddField(
            model_name='checklist',
            name='turn_and_stop_lights_mark',
            field=models.IntegerField(choices=[(0, 'NO'), (1, 'YES'), (2, 'N/A')], default=1, verbose_name='Turn and stop lights mark'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='checklist',
            name='brake_fluid_flag',
            field=models.IntegerField(choices=[(1, 'Critical'), (2, 'Need correction'), (3, 'OK')], default=3, verbose_name='Brake fluid status'),
        ),
        migrations.AlterField(
            model_name='checklist',
            name='brake_fluid_mark',
            field=models.IntegerField(choices=[(0, 'NO'), (1, 'YES'), (2, 'N/A')], verbose_name='Brake fluid mark'),
        ),
        migrations.AlterField(
            model_name='checklist',
            name='cooling_fluid_flag',
            field=models.IntegerField(choices=[(1, 'Critical'), (2, 'Need correction'), (3, 'OK')], default=3, verbose_name='Cooling fluid status'),
        ),
        migrations.AlterField(
            model_name='checklist',
            name='cooling_fluid_mark',
            field=models.IntegerField(choices=[(0, 'NO'), (1, 'YES'), (2, 'N/A')], verbose_name='Cooling fluid mark'),
        ),
        migrations.AlterField(
            model_name='checklist',
            name='fuel_flag',
            field=models.IntegerField(choices=[(1, 'Critical'), (2, 'Need correction'), (3, 'OK')], default=3, verbose_name='Fuel status'),
        ),
        migrations.AlterField(
            model_name='checklist',
            name='fuel_mark',
            field=models.IntegerField(choices=[(0, 'NO'), (1, 'YES'), (2, 'N/A')], verbose_name='Fuel mark'),
        ),
        migrations.AlterField(
            model_name='checklist',
            name='oil_flag',
            field=models.IntegerField(choices=[(1, 'Critical'), (2, 'Need correction'), (3, 'OK')], default=3, verbose_name='Oil status'),
        ),
        migrations.AlterField(
            model_name='checklist',
            name='oil_mark',
            field=models.IntegerField(choices=[(0, 'NO'), (1, 'YES'), (2, 'N/A')], verbose_name='Oil mark'),
        ),
        migrations.AlterField(
            model_name='checklist',
            name='windshield_fluid_flag',
            field=models.IntegerField(choices=[(1, 'Critical'), (2, 'Need correction'), (3, 'OK')], default=3, verbose_name='Windshield fluid status'),
        ),
        migrations.AlterField(
            model_name='checklist',
            name='windshield_fluid_mark',
            field=models.IntegerField(choices=[(0, 'NO'), (1, 'YES'), (2, 'N/A')], verbose_name='Windshield fluid mark'),
        ),
    ]