from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LAU',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=15, unique=True)),
                ('name', models.CharField(max_length=250)),
                ('local_name', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name': 'LAU',
                'verbose_name_plural': 'LAU',
                'ordering': ('code',),
            },
        ),
        migrations.CreateModel(
            name='NUTS',
            fields=[
                ('code', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250)),
                ('level', models.PositiveSmallIntegerField()),
            ],
            options={
                'verbose_name': 'NUTS',
                'verbose_name_plural': 'NUTS',
                'ordering': ('code',),
            },
        ),
        migrations.AddField(
            model_name='lau',
            name='nuts',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='django_nuts.NUTS'),
        ),
    ]
