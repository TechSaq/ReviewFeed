from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView, DetailView, View

from .models import ItemType, Item, ItemSpecificationValue, Review
from account.models import ReviewUser

from .forms import AddReviewForm


class ItemTypeListView(ListView):
    model = ItemType
    context_object_name = "item_types"
    template_name = "homepage.html"


class ItemListView(ListView):
    model = Item
    context_object_name = "items"
    template_name = "item/items_list.html"

    def get_queryset(self):
        self.item_type = get_object_or_404(
            ItemType, slug=self.kwargs["item_type_slug"])

        return Item.objects.filter(item_type=self.item_type)


class ItemDetailView(DetailView):
    model = Item
    context_object_name = "item"
    template_name = "item/item_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        self.item = get_object_or_404(Item, slug=self.kwargs["slug"])

        context["specifications"] = ItemSpecificationValue.objects.filter(
            item=self.item)

        context["reviews"] = Review.objects.filter(item=self.item)

        form = AddReviewForm()
        form.user = self.request.user
        form.slug = self.kwargs["slug"]

        context["form"] = form

        print(form.slug)

        return context


def add_review(request, **kwargs):

    form = {}
    if request.method == "POST":
        form = AddReviewForm(request.POST)
        if form.is_valid():
            slug = kwargs.pop('slug')
            print("request.user")
            print(request.user)
            review_user = ReviewUser.objects.get(user=request.user)
            review = form.save(user=review_user, slug=slug)
            return redirect("item:item_detail", slug)
        else:
            pass
    else:
        form = AddReviewForm()
        form.user = request.user
        form.slug = kwargs.pop('slug')

    context = {"form": form}
    return render(request, "item/_add_review_form.html", context)
