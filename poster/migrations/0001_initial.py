# Generated by Django 3.2.9 on 2023-01-03 18:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cinema',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=50)),
                ('district', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('numbers', models.PositiveSmallIntegerField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=50)),
                ('year', models.PositiveSmallIntegerField(max_length=4)),
                ('photo', models.ImageField(upload_to='photo/')),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='FilmGenre',
            fields=[
                ('genre', models.CharField(db_index=True, max_length=50, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='FilmProduction',
            fields=[
                ('production', models.CharField(db_index=True, max_length=50, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Hall',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('cinema_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='poster.cinema')),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=100)),
                ('photo', models.ImageField(upload_to='')),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SeatCategory',
            fields=[
                ('category', models.CharField(db_index=True, max_length=50, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_time', models.DateTimeField()),
                ('film_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='poster.film')),
                ('hall_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='poster.hall')),
            ],
        ),
        migrations.CreateModel(
            name='SeatRow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('row', models.PositiveSmallIntegerField(max_length=2)),
                ('place', models.PositiveSmallIntegerField(max_length=4)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='poster.seatcategory')),
                ('hall_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='poster.hall')),
            ],
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='poster.seatcategory')),
                ('session_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='poster.session')),
            ],
        ),
        migrations.AddField(
            model_name='film',
            name='genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='poster.filmgenre'),
        ),
        migrations.AddField(
            model_name='film',
            name='production',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='poster.filmproduction'),
        ),
    ]
