# Generated by Django 3.1.14 on 2022-06-13 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('projects', '0017_auto_20220613_1731'),
    ]

    operations = [
        migrations.CreateModel(
            name='AsyncMigrationStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meta', models.JSONField(default=dict, help_text='Meta is for any params for migrations.E.g. project, filter or error message.', null=True, verbose_name='meta')),
                ('name', models.TextField(help_text='Migration name', verbose_name='migration_name')),
                ('status', models.CharField(choices=[('STARTED', 'Migration is started or queued.'), ('IN PROGRESS', 'Migration is in progress. Check meta for job_id or status.'), ('FINISHED', 'Migration completed successfully.'), ('ERROR', 'Migration completed with errors. Check meta for more info.')], default=None, max_length=100, null=True)),
                ('project', models.ForeignKey(help_text='Project ID for this migration', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='asyncmigrationstatus', to='projects.project')),
            ],
        ),
    ]
