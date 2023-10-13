from django import forms
from .models import PropertyBook, PropertyReview


class PropertyBookForm(forms.ModelForm):
    date_from = forms.DateField(required=True, widget=forms.DateInput(attrs={'type': 'date'}))
    date_to = forms.DateField(required=True, widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = PropertyBook 
        fields = ("date_from", "date_to", "guest", "children")


class PropertyReviewForm(forms.ModelForm):
     class Meta:
        model = PropertyReview
        fields = ("rate","feedback")