# Generated by Django 5.2 on 2025-05-02 10:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dosyalar', '0006_remove_maddiyardim_dosya_maddiyardim_dosyalar_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DosyaTutari',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tutar', models.DecimalField(decimal_places=2, max_digits=10)),
                ('dosya', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='yardim_tutarlari', to='dosyalar.dosya')),
                ('maddi_yardim', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dosya_tutarlari', to='dosyalar.maddiyardim')),
            ],
            options={
                'verbose_name': 'Dosya Tutarı',
                'verbose_name_plural': 'Dosya Tutarları',
                'unique_together': {('maddi_yardim', 'dosya')},
            },
        ),
    ]
