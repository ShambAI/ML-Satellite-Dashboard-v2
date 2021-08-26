# Generated by Django 3.2.5 on 2021-08-13 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_auto_20210803_2100'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nursery',
            name='arrondissement',
        ),
        migrations.RemoveField(
            model_name='nursery',
            name='certified',
        ),
        migrations.RemoveField(
            model_name='nursery',
            name='certified_by',
        ),
        migrations.RemoveField(
            model_name='nursery',
            name='certified_date',
        ),
        migrations.RemoveField(
            model_name='nursery',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='nursery',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='nursery',
            name='department',
        ),
        migrations.RemoveField(
            model_name='nursery',
            name='first_login',
        ),
        migrations.RemoveField(
            model_name='nursery',
            name='owner_address',
        ),
        migrations.RemoveField(
            model_name='nursery',
            name='owner_date_of_birth',
        ),
        migrations.RemoveField(
            model_name='nursery',
            name='owner_gender',
        ),
        migrations.RemoveField(
            model_name='nursery',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='nursery',
            name='updated_by',
        ),
        migrations.RemoveField(
            model_name='nursery',
            name='village',
        ),
        migrations.RemoveField(
            model_name='nursery',
            name='website',
        ),
        migrations.AddField(
            model_name='nursery',
            name='number_of_plants',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='mothertree',
            name='created_by',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='mothertree',
            name='created_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='mothertree',
            name='updated_by',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='mothertree',
            name='updated_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='nursery',
            name='latitude',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='nursery',
            name='status',
            field=models.IntegerField(choices=[(1, 'Active'), (0, 'Inactive')], default=1),
        ),
        migrations.AlterField(
            model_name='plantation',
            name='created_by',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='plantation',
            name='created_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='plantation',
            name='updated_by',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='plantation',
            name='updated_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='remuser',
            name='created_by',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='remuser',
            name='updated_by',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='yieldhistory',
            name='created_by',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='yieldhistory',
            name='created_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='yieldhistory',
            name='updated_by',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='yieldhistory',
            name='updated_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]