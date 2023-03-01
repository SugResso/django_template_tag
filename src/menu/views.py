from django.shortcuts import render
from menu.models import Menu


# Create your views here.
def get_chapters(request):
    menus = [menu.title for menu in Menu.objects.all()]
    return render(request, 'menu/chapter.html', context={'menus': menus})


def get_sub_chapters(request, name_menu):
    name_menu = name_menu
    return render(request, 'menu/sub_chapter.html', context={'name_menu': name_menu})
