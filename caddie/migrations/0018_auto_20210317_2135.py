# Generated by Django 3.0.5 on 2021-03-17 21:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('caddie', '0017_gene_mutation_score'),
    ]

    operations = [
        migrations.CreateModel(
            name='MutationCancerType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=128)),
            ],
        ),
        migrations.RemoveField(
            model_name='gene',
            name='mutation_score',
        ),
        migrations.RemoveField(
            model_name='gene',
            name='n_mutations',
        ),
        migrations.CreateModel(
            name='MutationCounts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mutation_counts', models.FloatField()),
                ('mutation_score', models.FloatField()),
                ('cancer_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='caddie.MutationCancerType')),
                ('gene', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='caddie.Gene')),
            ],
            options={
                'unique_together': {('cancer_type', 'gene')},
            },
        ),
    ]
