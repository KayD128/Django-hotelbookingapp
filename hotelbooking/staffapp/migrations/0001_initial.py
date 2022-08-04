# Generated by Django 4.0.5 on 2022-06-29 21:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=100, null=True)),
                ('address', models.CharField(max_length=100, null=True)),
                ('phone', models.CharField(max_length=11, null=True)),
                ('nationality', models.CharField(choices=[('Nigeria', 'Nigeria'), ('United States of America', 'USA'), ('Ghana', 'Ghana'), ('Niger', 'Niger'), ('Germany', 'Germany'), ('United Arab Emirates', 'UAE')], max_length=100, null=True)),
                ('state', models.CharField(choices=[('Oyo', 'Oyo'), ('Abuja', 'Abuja')], max_length=20, null=True)),
                ('means_of_identity', models.ImageField(null=True, upload_to='pictures/')),
                ('particulars', models.FileField(null=True, upload_to='documents/')),
                ('profile_passport', models.ImageField(null=True, upload_to='staffs/')),
                ('position', models.CharField(choices=[('General Manager', 'GM'), ('Assistant General Manager', 'AGM'), ('Front Office Manager', 'FOM'), ('Concierge', 'Concierge'), ('Guest Service Agent', 'GSA'), ('Night Auditor', 'Night Auditor'), ('Security', 'Security'), ('Bellman', 'Bellman'), ('Director of Sales', 'DOS'), ('Sales Manager', 'SM'), ('Sales Coordinator', 'SC'), ('Catering Assistant', 'Catering Assistant'), ('Executive Housekeeper', 'Executive Housekeeper'), ('Assistant Executive Housekeeper', 'Assistant Executive Housekeeper'), ('Continental Breakfast Attendant', 'Continental Breakfast Attendant'), ('Houseperson', 'Houseperson'), ('Room Attendant', 'Room Attendant'), ('Chief Maintenance Engineer', 'Chief Maintenance Engineer'), ('Assistant Maintenance', 'Assistant Maintenance')], max_length=100, null=True)),
                ('marital_status', models.CharField(choices=[('Single', 'Single'), ('Married', 'Married'), ('Divorced', 'Divorced'), ('Complicated', 'Complicated')], max_length=20, null=True)),
                ('staff', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]