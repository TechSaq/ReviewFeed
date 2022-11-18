from django.db import models

from account.models import ReviewUser


class Category(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class ItemType(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="item_type")
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class ItemSpecification(models.Model):
    name = models.CharField(max_length=200)
    item = models.ForeignKey(ItemType, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Item(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField(max_length=2000, null=True, blank=True)
    item_type = models.ForeignKey(
        ItemType, related_name="item_type", on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, related_name="category")
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to="items", null=True, blank=True)

    def __str__(self):
        return self.title


class ItemSpecificationValue(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    specification = models.ForeignKey(
        ItemSpecification, on_delete=models.CASCADE)
    value = models.CharField(max_length=500)

    def __str__(self):
        return self.item.title + " - " + self.value


class Review(models.Model):
    RatingChoices = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    )

    title = models.CharField(max_length=200)
    description = models.TextField(max_length=2000, null=True, blank=True)
    rating = models.IntegerField(choices=RatingChoices)
    user = models.ForeignKey(
        ReviewUser, on_delete=models.CASCADE, null=True, blank=True)
    item = models.ForeignKey(Item, related_name="review_item",
                             on_delete=models.CASCADE)

    def __str__(self):
        return self.title
