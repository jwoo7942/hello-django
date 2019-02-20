from django.shortcuts import render
from .models import Shop, Item


def index(request):
    # 전체 Shop 목록을 가져올 예정이다. (Lazy한 특성)
    qs = Shop.objects.all()
    return render(request, 'shop/shop_list.html', {
        'shop_list': qs,
    })


#def shop_detail(request, pk):
#    # 즉시 DB로부터 데이터를 가져옵니다.
#    shop = Shop.objects.get(pk=pk)
#    return render(request, 'shop/shop_detail.html', {
#        'shop': shop,
#    })

def shop_detail(request, pk):
    # 즉시 DB로부터 데이터를 가져옵니다.
    qs = Shop.objects.get(pk=pk)
    item = Item.objects.filter(shop_id=pk)
    return render(request, 'shop/shop_detail.html', {
        'item_list': item,
        'shop': qs,

    })