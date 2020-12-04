# Generated by Django 3.1.3 on 2020-12-04 18:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=30)),
                ('version', models.CharField(max_length=30)),
                ('extension', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'language',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('path', models.CharField(max_length=100)),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='code_editor.language')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.userprofile')),
            ],
            options={
                'db_table': 'project',
            },
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('path', models.CharField(max_length=150)),
                ('creation_date', models.DateField()),
                ('is_main', models.BooleanField(default=False)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='code_editor.project')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.userprofile')),
            ],
            options={
                'db_table': 'file',
            },
        ),
    ]