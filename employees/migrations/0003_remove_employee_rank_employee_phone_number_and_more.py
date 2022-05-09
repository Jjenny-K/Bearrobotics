from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0002_rename_restaurant_restaurant_name'),
        ('employees', '0002_alter_employee_rank'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='rank',
        ),
        migrations.AddField(
            model_name='employee',
            name='phone_number',
            field=models.CharField(blank=True, default='', max_length=31),
        ),
        migrations.AddField(
            model_name='employee',
            name='rank_type',
            field=models.CharField(choices=[('SUPER', 'Super'), ('CONFIRM', 'Confirm'), ('NORMAL', 'Normal')], default='NORMAL', max_length=15),
        ),
        migrations.AlterField(
            model_name='employee',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='restaurants.group'),
        ),
    ]
