import random
from datetime import datetime

from django.shortcuts import render
from django.views import View


class IndexView(View):

    def get(self, request):
        ctx = {"actual_date": datetime.now()}
        return render(request, "test.html", ctx)



class CarouselView(View):

    def get(self, request):
        recipes = Recipe.objects.all()
        random_recipes = []
        for random_count in range(3):
            recipe = random.choice(recipes)
            random_recipes.append(recipe)
        return render(request, 'carousel.html', {'recipes': random_recipes})
