# Generated by Django 5.2 on 2025-05-06 10:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dosyalar', '0015_ailebilgisi'),
    ]

    operations = [
        migrations.CreateModel(
            name='ManuelMaddiYardimKayit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad_soyad', models.CharField(max_length=100)),
                ('tc_kimlik', models.CharField(max_length=11)),
                ('telefon', models.CharField(max_length=20)),
                ('adres', models.TextField()),
                ('tutar', models.DecimalField(decimal_places=2, max_digits=10)),
                ('aciklama', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('maddi_yardim', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='manuel_kayitlar', to='dosyalar.maddiyardim')),
            ],
            options={
                'verbose_name': 'Manuel Maddi Yardım Kaydı',
                'verbose_name_plural': 'Manuel Maddi Yardım Kayıtları',
                'db_table': 'manuel_maddi_yardim_kayitlar',
            },
        ),
    ]
