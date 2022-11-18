from django import forms

from .models import Review, Item


class AddReviewForm(forms.Form):
    RatingChoices = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    )

    title = forms.CharField(label="Title", max_length=200, required=False)
    review = forms.CharField(
        label="Your Review", max_length=200, required=False, widget=forms.Textarea)
    rating = forms.IntegerField(
        label="Your Rating", required=False)

    def save(self, **kwargs):

        title = self.cleaned_data["title"]
        review = self.cleaned_data["review"]
        rating = self.cleaned_data["rating"]

        print(kwargs)

        user = kwargs.pop('user')

        slug = kwargs.pop('slug')
        item = Item.objects.get(slug=slug)

        review = Review.objects.create(
            title=title,
            description=review,
            rating=rating,
            user=user,
            item=item
        )

        review.save()

        return review
