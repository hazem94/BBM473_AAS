# Generated by Django 2.1.7 on 2019-05-01 07:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='assessment',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='assessmentstudent',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='assignment',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='course',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='courselearningobjective',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='courseoffering',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='curriculum',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='curriculumcourse',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='examination',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='instructor',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='keylearningoutcome',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='questioncourselearningobjective',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='questionkeylearningoutcome',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='quiz',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='section',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='sectioninstructor',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='sectionstudent',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='semester',
            options={'managed': True},
        ),
    ]