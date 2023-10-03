# Generated by Django 4.2.5 on 2023-10-03 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='casestudysection',
            options={'ordering': ('number', '-create_at', '-update_at'), 'verbose_name': 'Case Study Section', 'verbose_name_plural': 'Case Study Sections'},
        ),
        migrations.AddField(
            model_name='casestudysection',
            name='layout',
            field=models.CharField(choices=[('img-full', 'Image Full Width'), ('img-left', 'Image ON Right'), ('img-right', 'Image ON Left'), ('card', 'Card'), ('quote', 'Quote'), ('text', 'Text only')], default='card', max_length=20, verbose_name='Section Layout'),
        ),
        migrations.AddField(
            model_name='casestudysection',
            name='number',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Number'),
        ),
        migrations.AlterField(
            model_name='casestudysection',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='sections/', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='casestudysection',
            name='sub_text',
            field=models.TextField(blank=True, null=True, verbose_name='Sub Text'),
        ),
    ]
