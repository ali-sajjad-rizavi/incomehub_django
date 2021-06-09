# Generated by Django 3.2.3 on 2021-06-07 08:25

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
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(default='job-picture.jpg', upload_to='job-images')),
                ('description', models.TextField()),
                ('company_name', models.CharField(max_length=100)),
                ('company_description', models.TextField()),
                ('salary', models.IntegerField()),
                ('category', models.CharField(choices=[('other', 'Other'), ('it', 'IT and Software'), ('data_entry', 'Data Entry'), ('graphic_design', 'Graphic Design'), ('teaching', 'Teaching'), ('home_tuiton', 'Home Tuition')], max_length=50)),
                ('location', models.CharField(choices=[('lahore', 'Lahore'), ('karachi', 'Karachi'), ('islamabad', 'Islamabad')], max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
