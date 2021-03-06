# Generated by Django 3.0.7 on 2020-06-14 06:19

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('django_occupations', '0002_add_soc_codes'),
    ]

    operations = [
        migrations.CreateModel(
            name='ONetAlternateTitle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('alternate_title', models.CharField(max_length=250)),
                ('short_title', models.CharField(max_length=150, null=True)),
                ('title', models.CharField(max_length=150)),
                ('onet_soc_code', models.CharField(max_length=10, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ONetOccupation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('onet_soc_code', models.CharField(max_length=10, unique=True)),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='socbroadoccupation',
            name='soc_code',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='socdetailedoccupation',
            name='soc_code',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='socmajorgroup',
            name='soc_code',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='socminorgroup',
            name='soc_code',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.DeleteModel(
            name='Occupation',
        ),
        migrations.AddField(
            model_name='onetoccupation',
            name='soc_occupation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='django_occupations.SOCDetailedOccupation'),
        ),
        migrations.AddField(
            model_name='onetalternatetitle',
            name='onet_soc_occupation',
            field=models.ManyToManyField(to='django_occupations.ONetOccupation'),
        ),
        migrations.AddField(
            model_name='onetalternatetitle',
            name='soc_occupation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='django_occupations.SOCDetailedOccupation'),
        ),
    ]
