from django.shortcuts import render
from django.http import HttpResponse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
    'pizza': {
        'яйцо, шт.': 3,
        'майонез, ст.л.': 5,
        'мука, ст.л.': 5,
        'колбаса, г.': 30,
        'сыр, г.': 30,
        'помидор, г.': 25,
        'огурец маринованный, г.': 20,
        'кетчуп, ч.л.': 1
    },
}


# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
def cooking_helper(request, recipe_name):
    context = {
        'recipe': {}
    }
    servings = int(request.GET.get('servings', 1))
    content = DATA.get(recipe_name)
    if not content:
        return render(request, 'calculator/index.html', context)
    for ingredient, quantity in content.items():
        context['recipe'][ingredient] = quantity * servings
    return render(request, 'calculator/index.html', context)


def main_page(request):
    return HttpResponse(
        'Доступные рецепты: омлет (omlet), паста (pasta), '
        'бутерброд (buter), пицца (pizza)')
