from django.forms import ModelForm

from .models import Profile


class ProfileForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Profile
        labels = {'fio': 'ФИО', 'age': 'Возраст',
                  'nationality': 'Национальность',
                  'activity': 'Деятельность',
                  'family_status': 'Семейный статус', 'children': 'Дети'}
        fields = ("image", 'fio', 'age', 'nationality',
                  'activity', 'family_status', 'children')
