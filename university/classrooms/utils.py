# utils.py
menu = [
    {'title': "О сайте", 'url_name': 'about'},
    {'title': "Аудитории", 'url_name': 'room_list'},
    {'title': "Войти", 'url_name': 'login'}
]

class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context['menu'] = menu
        return context
