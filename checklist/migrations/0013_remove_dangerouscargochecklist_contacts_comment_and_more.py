# Generated by Django 5.1.2 on 2024-12-15 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checklist', '0012_dangerouscargochecklist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dangerouscargochecklist',
            name='contacts_comment',
        ),
        migrations.RemoveField(
            model_name='dangerouscargochecklist',
            name='contacts_mark',
        ),
        migrations.RemoveField(
            model_name='dangerouscargochecklist',
            name='danger_signs_comment',
        ),
        migrations.RemoveField(
            model_name='dangerouscargochecklist',
            name='danger_signs_mark',
        ),
        migrations.RemoveField(
            model_name='dangerouscargochecklist',
            name='danger_waybill_comment',
        ),
        migrations.RemoveField(
            model_name='dangerouscargochecklist',
            name='danger_waybill_mark',
        ),
        migrations.RemoveField(
            model_name='dangerouscargochecklist',
            name='driver_approval_comment',
        ),
        migrations.RemoveField(
            model_name='dangerouscargochecklist',
            name='driver_approval_mark',
        ),
        migrations.RemoveField(
            model_name='dangerouscargochecklist',
            name='driver_instruction_comment',
        ),
        migrations.RemoveField(
            model_name='dangerouscargochecklist',
            name='driver_instruction_mark',
        ),
        migrations.RemoveField(
            model_name='dangerouscargochecklist',
            name='emergency_plan_comment',
        ),
        migrations.RemoveField(
            model_name='dangerouscargochecklist',
            name='emergency_plan_mark',
        ),
        migrations.RemoveField(
            model_name='dangerouscargochecklist',
            name='license_card_comment',
        ),
        migrations.RemoveField(
            model_name='dangerouscargochecklist',
            name='license_card_mark',
        ),
        migrations.RemoveField(
            model_name='dangerouscargochecklist',
            name='no_entry_sign_comment',
        ),
        migrations.RemoveField(
            model_name='dangerouscargochecklist',
            name='no_entry_sign_mark',
        ),
        migrations.RemoveField(
            model_name='dangerouscargochecklist',
            name='signal_tape_comment',
        ),
        migrations.RemoveField(
            model_name='dangerouscargochecklist',
            name='signal_tape_mark',
        ),
        migrations.RemoveField(
            model_name='dangerouscargochecklist',
            name='transportation_form_comment',
        ),
        migrations.RemoveField(
            model_name='dangerouscargochecklist',
            name='transportation_form_mark',
        ),
        migrations.RemoveField(
            model_name='dangerouscargochecklist',
            name='waybill_comment',
        ),
        migrations.RemoveField(
            model_name='dangerouscargochecklist',
            name='waybill_mark',
        ),
    ]
