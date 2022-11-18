from .models import ItemType


def get_item_types(request):

    item_types = ItemType.objects.all()

    return {"item_types": item_types}
