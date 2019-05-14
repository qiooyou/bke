# Generated by Django 2.0.9 on 2019-03-15 01:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': '文章', 'verbose_name_plural': '文章'},
        ),
        migrations.AlterModelOptions(
            name='articletags',
            options={'verbose_name': '文章标签', 'verbose_name_plural': '文章标签'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': '标签', 'verbose_name_plural': '标签'},
        ),
        migrations.AddField(
            model_name='article',
            name='abstract',
            field=models.TextField(blank=True, default=None, null=True, verbose_name='摘要'),
        ),
        migrations.AddField(
            model_name='tag',
            name='articles',
            field=models.ManyToManyField(through='pages.ArticleTags', to='pages.Article'),
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.TextField(blank=True, default=None, null=True, verbose_name='内容'),
        ),
        migrations.AlterField(
            model_name='article',
            name='create_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(through='pages.ArticleTags', to='pages.Tag'),
        ),
        migrations.AlterField(
            model_name='article',
            name='upate_time',
            field=models.DateTimeField(auto_now=True, verbose_name='最后修改时间'),
        ),
    ]
