from django.urls import path
from django.views.generic import TemplateView

from .views import ItemTypeListView, ItemListView, ItemDetailView, add_review

app_name = "item"

urlpatterns = [
    path('item/<str:slug>',
         ItemDetailView.as_view(), name="item_detail"),
    path('about', TemplateView.as_view(template_name='about.html'), name="about"),
    path('contact', TemplateView.as_view(
        template_name='contact.html'), name="contact"),
    path('review/add/<str:slug>', add_review, name="add_review"),
    path('', ItemTypeListView.as_view(), name="home"),
    path('<str:item_type_slug>', ItemListView.as_view(), name="item_types"),
]
