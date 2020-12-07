from django.shortcuts import render
from app.models import category,product,ShopCart,WXuser
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
import datetime
from decimal import Decimal
# Create your views here.
        

class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')

        elif isinstance(obj, datetime.date):
            return obj.strftime("%Y-%m-%d")

        else:
            return json.JSONEncoder.default(self, obj)
#添加类别
@csrf_exempt
def  addcategory(request):
    catename = request.POST.get('catename')
    print(catename)
    obj=category(catename = catename)
    obj.save()
    data = {"code": 200, "msg": "商品类别添加成功"}
    return HttpResponse(json.dumps(data, cls=DateEncoder), content_type="application/json")
#删除类别
@csrf_exempt
def  DelCategory(request):
    print(request)
    cateid = request.POST.get('cateid')
    print(cateid)
    category.objects.filter(cateid = cateid).delete()
    data = {"code": 200, "msg": "商品类别删除成功"}
    return HttpResponse(json.dumps(data, cls=DateEncoder), content_type="application/json")

#修改类别名称
@csrf_exempt
def  EditCategoryName(request):
    cateid = request.POST.get('cateid')
    catename = request.POST.get('catename')
    category.objects.filter(cateid = cateid).update(catename = catename)
    data = {"code": 200, "msg": "商品类别编辑成功"}
    return HttpResponse(json.dumps(data, cls=DateEncoder), content_type="application/json")

#查询商品类别
@csrf_exempt
def  SearchCategoryName(request):
    categoryList = category.objects.values()
    data = list(categoryList)
    data = {"code": 200, "msg": "成功","data":data}
    return HttpResponse(json.dumps(data, cls=DateEncoder), content_type="application/json")

#添加商品
@csrf_exempt
def addproduct(request):
    id = request.POST.get('cateid')
    cateid = category.objects.get(cateid = id)
    name = request.POST.get('name')
    mainimage = request.POST.get('mainimage')
    detail = request.POST.get('detail')
    price = request.POST.get('price')
    stock = request.POST.get('stock')
    status = request.POST.get('status')
    obj=product(cateid=cateid,name=name,mainimage=mainimage,detail=detail,
    price=price,stock=stock,status = status)
    obj.save()
    data = {"code": 200, "msg": "商品添加成功"}
    return HttpResponse(json.dumps(data, cls=DateEncoder), content_type="application/json")

#根据类别查询商品
@csrf_exempt
def productList(request):
    cateid = request.POST.get('cateid')
    obj = product.objects.filter(cateid = cateid).values()
    data = list(obj)
    data = {"code": 200, "msg": "商品获取成功","data":data}
    return HttpResponse(json.dumps(data, cls=DateEncoder), content_type="application/json")

#查询店长推荐/限时抢购商品（1:在售2:店长推荐3:限时抢购)
@csrf_exempt
def SearchStatutList(request):
    status = request.POST.get('status')
    # status = json.loads(request.body).get('status')
    # print(request.body)
    obj = product.objects.filter(status = status).values()
    data = list(obj)
    data = {"code": 200, "msg": "商品获取成功","data":data}
    return HttpResponse(json.dumps(data, cls=DateEncoder), content_type="application/json")

#根据商品id查询商品的详情
@csrf_exempt
def SearchProudById(request):
    proid = request.POST.get('proid')
    # status = json.loads(request.body).get('status')
    obj = product.objects.filter(proid = proid).values()
    if obj.count() == 0:
        data = {"code": 200, "msg": "商品不存在"}
        return HttpResponse(json.dumps(data, cls=DateEncoder), content_type="application/json")
    else:
        data = list(obj)
        data = {"code": 200, "msg": "商品获取成功","data":data}
        return HttpResponse(json.dumps(data, cls=DateEncoder), content_type="application/json")


#用户登陆//创建
def WXuserLogin(request):
    WXname = request.POST.get('WXname')
    WXavatar = request.POST.get('WXavatar')
    WXpassword = request.POST.get('WXpassword')
    data = {"code": 200, "msg": "用户登陆/创建成功"}
    return HttpResponse(json.dumps(data, cls=DateEncoder), content_type="application/json")


#根据商品名称查找商品
@csrf_exempt
def SearchProudByName(request):
    name = request.POST.get('name')
    print(name)
    if(name == ''):
        print('为空不操作')
    else:
        obj = product.objects.filter(name__contains= name).values()
        if obj.count() == 0:
            data = {"code": 200, "msg": "商品不存在"}
            return HttpResponse(json.dumps(data, cls=DateEncoder), content_type="application/json")
        else:
            data = list(obj)
            data = {"code": 200, "msg": "商品获取成功","data":data}
            return HttpResponse(json.dumps(data, cls=DateEncoder), content_type="application/json")
    data = {"code": 200, "msg": "商品获取成功","data":''}
    return HttpResponse(json.dumps(data, cls=DateEncoder), content_type="application/json")


#加入购物车
@csrf_exempt
def addtoCart(request):
    getuserid = request.POST.get('WXuserid')
    getproid = request.POST.get('proid')
    print(ShopCart.objects.filter(WXuserid = getuserid).values().count() == 0)
    if(WXuser.objects.filter(WXuserid = getuserid).values().count() == 0):
        data = {"code": 500, "msg": "还未注册"}
        return HttpResponse(json.dumps(data, cls=DateEncoder), content_type="application/json")
    else:
        print('已经注册')
        if(ShopCart.objects.filter(WXuserid = getuserid).values().count() == 0):
            print('该用户还没添加购物车')
            haisproid = product.objects.get(proid = getproid)
            haswxuser = WXuser.objects.get(WXuserid = getuserid)
            obj = ShopCart(WXuserid=haswxuser,proid=haisproid,quantity=1)
            obj.save()
            data = {"code": 200, "msg": "购物车添加成功"}
            return HttpResponse(json.dumps(data, cls=DateEncoder), content_type="application/json")
        else:
            print('该用户已经有购物车了')
            if(ShopCart.objects.filter(WXuserid = getuserid ,proid = getproid ).values().count() == 0):
                haisproid = product.objects.get(proid = getproid)
                haswxuser = WXuser.objects.get(WXuserid = getuserid)
                obj = ShopCart(WXuserid=haswxuser,proid=haisproid,quantity=1)
                obj.save()
                data = {"code": 200, "msg": "购物车添加成功"}
                return HttpResponse(json.dumps(data, cls=DateEncoder), content_type="application/json")
            else:
                print('购物车有该商品')
                haisproid = product.objects.get(proid = getproid)
                haswxuser = WXuser.objects.get(WXuserid = getuserid)
                number = ShopCart.objects.get(proid = haisproid ,WXuserid=haswxuser).quantity
                ShopCart.objects.filter(WXuserid=haswxuser ,proid = haisproid).update(quantity = number + 1)
                data = {"code": 200, "msg": "购物车添加成功"}
                return HttpResponse(json.dumps(data, cls=DateEncoder), content_type="application/json")
    data = {"code": 500, "msg": "llll"}
    return HttpResponse(json.dumps(data, cls=DateEncoder), content_type="application/json")


#查询购物车内容（通过userid）
@csrf_exempt
def searchCart(request):
    WXuserid = request.POST.get('WXuserid')
    haswxuser = WXuser.objects.get(WXuserid = WXuserid)
    cartList = ShopCart.objects.filter(WXuserid = haswxuser).values()
    countprice = 0
    for i,j in enumerate(cartList):
        searchList = product.objects.filter(proid = j['proid_id']).values()
        list(cartList)[i]['name'] = list(searchList)[0]['name']
        list(cartList)[i]['price'] = list(searchList)[0]['price']
        list(cartList)[i]['mainimage'] = list(searchList)[0]['mainimage']
        list(cartList)[i]['stock'] = list(searchList)[0]['stock']
        leftprice = str(list(searchList)[0]['price'])
        countprice = str(countprice)
        countprice = Decimal(leftprice) * list(cartList)[i]['quantity'] + Decimal(countprice)
    print(countprice)
    number = str(countprice)
    data = {"code": 200, "msg": "查询成功","data":list(cartList),"countprice":number}
    return HttpResponse(json.dumps(data, cls=DateEncoder), content_type="application/json")

#减少购物车中的商品
@csrf_exempt
def reduce(request):
    proid = request.POST.get('proid')
    WXuserid = request.POST.get('WXuserid')
    reducetype = request.POST.get('reducetype')
    haswxuser = WXuser.objects.get(WXuserid = WXuserid)
    hasproid = product.objects.get(proid = proid)
    if(reducetype == 1):
        obj=ShopCart.objects.get(proid=hasproid,WXuserid = haswxuser)
        obj.delete()
    else:
        number = ShopCart.objects.get(proid = hasproid ,WXuserid=haswxuser).quantity
        if(number == 1):
            print('不能再少啦！')
            data = {"code": 200, "msg": "不能再少啦！"}
            return HttpResponse(json.dumps(data, cls=DateEncoder), content_type="application/json")
        else:
            ShopCart.objects.filter(WXuserid=haswxuser ,proid = hasproid).update(quantity = number - 1)
    data = {"code": 200, "msg": "减少成功"}
    return HttpResponse(json.dumps(data, cls=DateEncoder), content_type="application/json")

#删除购物车中的商品
@csrf_exempt
def delShopcartGood(request):
    proid = request.POST.get('proid')
    WXuserid = request.POST.get('WXuserid')
    haswxuser = WXuser.objects.get(WXuserid = WXuserid)
    hasproid = product.objects.get(proid = proid)
    obj=ShopCart.objects.get(WXuserid = haswxuser ,proid = hasproid)
    obj.delete()
    data = {"code": 200, "msg": "删除成功"}
    return HttpResponse(json.dumps(data, cls=DateEncoder), content_type="application/json")
    




    