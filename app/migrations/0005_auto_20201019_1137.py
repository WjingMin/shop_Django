# Generated by Django 3.0.4 on 2020-10-19 11:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20200913_1822'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='salenumber',
            field=models.IntegerField(default=1, verbose_name='销售数量'),
        ),
        migrations.CreateModel(
            name='WXuser',
            fields=[
                ('WXuserid', models.AutoField(primary_key=True, serialize=False)),
                ('WXname', models.CharField(max_length=30, verbose_name='用户名称')),
                ('WXavatar', models.CharField(max_length=500, null=True, verbose_name='用户头像')),
                ('WXpassword', models.CharField(max_length=300, verbose_name='用户名称')),
                ('createtime', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('updatetime', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
                ('cateid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.category')),
            ],
        ),
        migrations.CreateModel(
            name='ShopCart',
            fields=[
                ('cartid', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField(verbose_name='商品数量')),
                ('checked', models.IntegerField(verbose_name='是否勾选')),
                ('createtime', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('updatetime', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
                ('WXuserid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.WXuser')),
                ('proid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product')),
            ],
        ),
    ]
