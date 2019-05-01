# Generated by Django 2.1.7 on 2019-05-01 06:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assessment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('files', models.BinaryField(blank=True, null=True)),
                ('weight', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'assessment',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('due_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'assignment',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('code', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('credit', models.SmallIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'course',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Courselearningobjective',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.CharField(blank=True, max_length=1000, null=True)),
            ],
            options={
                'db_table': 'courselearningobjective',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Courseoffering',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('letter_grades', models.BinaryField(blank=True, null=True)),
            ],
            options={
                'db_table': 'courseoffering',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Curriculum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'curriculum',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Examination',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('room', models.CharField(blank=True, max_length=10, null=True)),
                ('m_date', models.DateField(blank=True, null=True)),
                ('duration', models.SmallIntegerField(blank=True, null=True)),
                ('type', models.CharField(blank=True, max_length=7, null=True)),
            ],
            options={
                'db_table': 'examination',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('surname', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'instructor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Keylearningoutcome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.CharField(blank=True, max_length=1000, null=True)),
            ],
            options={
                'db_table': 'keylearningoutcome',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.CharField(blank=True, max_length=1000, null=True)),
                ('weight', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'question',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('duration', models.SmallIntegerField(blank=True, null=True)),
                ('q_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'quiz',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'section',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(blank=True, max_length=10, null=True)),
                ('year', models.CharField(blank=True, max_length=4, null=True)),
            ],
            options={
                'db_table': 'semester',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('code', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=25, null=True)),
            ],
            options={
                'db_table': 'department',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('surname', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'db_table': 'student',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='AssessmentStudent',
            fields=[
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='app.Student')),
                ('grade', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'assessment_student',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CurriculumCourse',
            fields=[
                ('curriculum', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='app.Curriculum')),
            ],
            options={
                'db_table': 'curriculum_course',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='QuestionCourselearningobjective',
            fields=[
                ('courselearningobjective', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='app.Courselearningobjective')),
                ('value', models.SmallIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'question_courselearningobjective',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='QuestionKeylearningoutcome',
            fields=[
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='app.Question')),
                ('value', models.SmallIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'question_keylearningoutcome',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SectionInstructor',
            fields=[
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='app.Section')),
            ],
            options={
                'db_table': 'section_instructor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SectionStudent',
            fields=[
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='app.Section')),
            ],
            options={
                'db_table': 'section_student',
                'managed': False,
            },
        ),
        migrations.AddField(
            model_name='student',
            name='dep_code',
            field=models.ForeignKey(blank=True, db_column='dep_code', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.Department'),
        ),
    ]