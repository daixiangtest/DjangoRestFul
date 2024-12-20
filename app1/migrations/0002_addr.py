# Generated by Django 4.2.13 on 2024-06-06 12:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Addr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=18, verbose_name='手机号')),
                ('city', models.CharField(max_length=10, verbose_name='城市')),
                ('info', models.CharField(max_length=200, verbose_name='地址详情')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.userinfo', verbose_name='所属用户')),
            ],
            options={
                'verbose_name': '邮件地址表',
                'db_table': 'addr',
            },
        ),
    ]
