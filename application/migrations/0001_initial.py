# Generated by Django 3.2.18 on 2024-05-18 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('logo_image', models.ImageField(upload_to='services_logos/')),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('logo_image', models.ImageField(upload_to='sections_logos/')),
                ('application_service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.applicationservice')),
            ],
        ),
        migrations.CreateModel(
            name='SectionCenter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('qr', models.CharField(max_length=100, null=True)),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.section')),
            ],
        ),
        migrations.CreateModel(
            name='SectionClinic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dr_name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('specialist', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('qr', models.CharField(max_length=100, null=True)),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.section')),
            ],
        ),
        migrations.CreateModel(
            name='SectionHospital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('specialist', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('qr', models.CharField(max_length=100, null=True)),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.section')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('national_number', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='users/')),
                ('password', models.CharField(max_length=100)),
                ('bdate', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=10)),
                ('weight', models.IntegerField()),
                ('age', models.IntegerField()),
                ('blood', models.CharField(max_length=10)),
                ('qr', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserRecordsCenter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=100)),
                ('hour', models.CharField(max_length=100)),
                ('review_date', models.CharField(max_length=100)),
                ('section_center', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.sectioncenter')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.user')),
            ],
        ),
        migrations.CreateModel(
            name='UserRecordsClinic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=100)),
                ('hour', models.CharField(max_length=100)),
                ('review_date', models.CharField(max_length=100)),
                ('section_clinic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.sectionclinic')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.user')),
            ],
        ),
        migrations.CreateModel(
            name='UserRecordsHospital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=100)),
                ('hour', models.CharField(max_length=100)),
                ('review_date', models.CharField(max_length=100)),
                ('section_hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.sectionhospital')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.user')),
            ],
        ),
        migrations.CreateModel(
            name='UserRecordsHospitalImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='UserRecordsHospital/')),
                ('record', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.userrecordshospital')),
            ],
        ),
        migrations.CreateModel(
            name='UserRecordsClinicImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='UserRecordsClinic/')),
                ('record', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.userrecordsclinic')),
            ],
        ),
        migrations.CreateModel(
            name='UserRecordsCenterImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='UserRecordsCenter/')),
                ('record', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.userrecordscenter')),
            ],
        ),
        migrations.CreateModel(
            name='UserMedicalImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='UserMedicalImages/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.user')),
            ],
        ),
        migrations.CreateModel(
            name='UserMedicalAnalays',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('normal', models.IntegerField()),
                ('danger', models.IntegerField()),
                ('result', models.IntegerField()),
                ('analays_date', models.CharField(max_length=100)),
                ('src_name', models.CharField(max_length=100)),
                ('src_phone', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.user')),
            ],
        ),
        migrations.CreateModel(
            name='UserDoctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.sectionclinic')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.user')),
            ],
        ),
        migrations.CreateModel(
            name='SectionService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100)),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.section')),
            ],
        ),
        migrations.CreateModel(
            name='SectionHospitalBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=100)),
                ('month', models.CharField(max_length=100)),
                ('day', models.CharField(max_length=100)),
                ('hour', models.CharField(max_length=100)),
                ('commited', models.IntegerField()),
                ('section_hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.sectionhospital')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.user')),
            ],
        ),
        migrations.CreateModel(
            name='SectionClinicBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=100)),
                ('month', models.CharField(max_length=100)),
                ('day', models.CharField(max_length=100)),
                ('hour', models.CharField(max_length=100)),
                ('commited', models.IntegerField()),
                ('section_clinic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.sectionclinic')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.user')),
            ],
        ),
        migrations.CreateModel(
            name='SectionCenterBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=100)),
                ('month', models.CharField(max_length=100)),
                ('day', models.CharField(max_length=100)),
                ('hour', models.CharField(max_length=100)),
                ('commited', models.IntegerField()),
                ('section_center', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.sectioncenter')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.user')),
            ],
        ),
    ]
