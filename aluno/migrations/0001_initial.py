# Generated by Django 4.1.3 on 2022-11-03 00:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('matricula', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('data_nascimento', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='AlunoDisciplina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aluno.aluno')),
            ],
        ),
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('turno', models.CharField(max_length=50)),
                ('aluno', models.ManyToManyField(through='aluno.AlunoDisciplina', to='aluno.aluno')),
            ],
        ),
        migrations.AddField(
            model_name='alunodisciplina',
            name='disciplina',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aluno.disciplina'),
        ),
    ]
