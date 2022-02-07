from django.shortcuts import render, redirect, reverse
from . import forms
from movies.models import Movie
from books.models import Book
from django.views.generic import FormView
from django.contrib import messages



def create_review(request, pk):
  if request.method == "POST":
      form = forms.Review_Form(request.POST)
      movie = Movie.objects.get_or_none(pk=pk)
      book = Book.objects.get_or_none(pk=pk)
      if not movie or book:
        return redirect(reverse("core:home"))
      if book:
        if form.is_valid():
          review = form.save()
          review.book = book
          review.created_by = request.use
          review.save()
          messages.success(request, "Book reviewed")
          return redirect(reverse("book:detail", kwargs={"pk": pk }))
      if movie:
        if form.is_valid():
          review = form.save()
          review.movie = movie
          review.created_by = request.use
          review.save()
          messages.success(request, "Movie reviewed")
          return redirect(reverse("movie:detail", kwargs={"pk": pk}))





class Reivew_View(FormView):
  template_name = "review.html"
  form_class=forms.Review_Form