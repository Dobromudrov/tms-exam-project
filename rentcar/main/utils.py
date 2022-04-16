from .models import *

menu = [{'title': 'Главная страница', 'url_name': 'index'},
    {'title': 'Прокат Авто', 'url_name': 'cars'},
    {'title': 'Условия Аренды', 'url_name': 'conditions'},
    {'title': 'Контакты', 'url_name': 'contacts'},
    {'title': 'Добавить машину', 'url_name': 'add_cars'},
]


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.all()

        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(4)

        context['menu'] = user_menu

        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context

