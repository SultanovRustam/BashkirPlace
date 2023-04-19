from django.forms import ModelForm

from .models import Comment, Profile


class ProfileForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Profile
        labels = {'fio': 'ФИО', 'age': 'Возраст',
                  'nationality': 'Национальность',
                  'activity': 'Деятельность',
                  'family_status': 'Семейный статус',
                  'children': 'Дети', 'bio': 'О себе'}
        fields = ("image", 'fio', 'age', 'nationality',
                  'activity', 'family_status', 'children', 'bio')


class CommentForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["text"].widget.attrs[
            "placeholder"
        ] = "Введите какой нибудь текст комментария"

    class Meta:
        model = Comment
        fields = ("text",)
