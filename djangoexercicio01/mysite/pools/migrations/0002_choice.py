# Generated by Django 2.1.3 on 2019-05-27 23:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pools', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=50)),
                ('votes', models.IntegerField()),
                ('question', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='pools.Question')),
            ],
        ),
    ]