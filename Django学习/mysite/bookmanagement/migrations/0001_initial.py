# Generated by Django 4.0.2 on 2022-09-16 07:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='书籍名称')),
                ('author', models.CharField(max_length=64, verbose_name='作者')),
                ('price', models.FloatField(default=0.0, verbose_name='定价')),
                ('publish_date', models.DateField(blank=True, null=True, verbose_name='出版日期')),
                ('category', models.CharField(default='未分类', max_length=32, verbose_name='书籍分类')),
                ('create_datetime', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='图片名称')),
                ('description', models.TextField(default='', verbose_name='图片描述')),
                ('img', models.ImageField(upload_to='image/%Y/%m/%d/', verbose_name='图片')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookmanagement.book', verbose_name='所属书籍')),
            ],
        ),
    ]
