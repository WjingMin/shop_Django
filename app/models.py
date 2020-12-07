from django.db import models

class category(models.Model):
    cateid = models.AutoField(primary_key=True)
    catename = models.CharField(max_length=30,verbose_name='类别名称')
    catestatus = models.IntegerField(verbose_name='类别状态1-正常,2-已废弃',default=1)
    createtime = models.DateTimeField(auto_now_add=True,verbose_name='创建时间',null=True)
    updatetime = models.DateTimeField(auto_now=True,verbose_name='更新时间',null=True)

class product(models.Model):
    proid = models.AutoField(primary_key=True)
    cateid = models.IntegerField(verbose_name='类别Id')
    name = models.CharField(max_length=30,verbose_name='商品名称')
    mainimage = models.CharField(max_length=500,verbose_name='产品主图,url相对地址',null=True)
    detail = models.CharField(max_length=500,verbose_name='产品详细图,url相对地址',null=True)
    price = models.FloatField(verbose_name='价格')
    stock = models.IntegerField(verbose_name='库存数量')
    salenumber = models.IntegerField(verbose_name='销售数量',default=1)
    status = models.IntegerField(verbose_name='商品状态.1-在售 2-店长推荐 3-限时抢购',default=1)
    createtime = models.DateTimeField(auto_now_add=True,verbose_name='创建时间',null=True)
    updatetime = models.DateTimeField(auto_now=True,verbose_name='更新时间',null=True)
    cateid =  models.ForeignKey(category,on_delete=models.CASCADE) 

#用户信息
class WXuser(models.Model):
    WXuserid = models.AutoField(primary_key=True)
    WXname = models.CharField(max_length=30,verbose_name='用户名称')
    WXavatar = models.CharField(max_length=500,verbose_name='用户头像',null=True)
    phone = models.CharField(max_length=500,verbose_name='用户手机',null=True)
    WXpassword = models.CharField(max_length=300,verbose_name='密码')
    createtime = models.DateTimeField(auto_now_add=True,verbose_name='创建时间',null=True)
    updatetime = models.DateTimeField(auto_now=True,verbose_name='更新时间',null=True)

#购物车
class ShopCart(models.Model):
    cartid = models.AutoField(primary_key=True)
    WXuserid = models.IntegerField(verbose_name='用户id')
    proid = models.IntegerField(verbose_name='商品id')
    quantity = models.IntegerField(verbose_name='商品数量')
    checked = models.IntegerField(verbose_name='是否勾选',default=True)
    createtime = models.DateTimeField(auto_now_add=True,verbose_name='创建时间',null=True)
    updatetime = models.DateTimeField(auto_now=True,verbose_name='更新时间',null=True)
    proid =  models.ForeignKey(product,on_delete=models.CASCADE) 
    WXuserid =  models.ForeignKey(WXuser,on_delete=models.CASCADE) 









    

