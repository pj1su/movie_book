from django import forms
from . import models

class Review_Form(forms.ModelForm):
  class Meta:
    model = models.Review
    fields =  ("text",)

    def save(self):
        review = super().save(commit=False)
        return review