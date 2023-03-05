from django.forms import ModelForm

from .models import Class


class ClassForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["title"].widget.attrs[
            "placeholder"
        ] = "Введите название занятия"
        self.fields["description"].widget.attrs[
            "placeholder"
        ] = "Введите  описание занятия"
        self.fields["event_date"].widget.attrs[
            "placeholder"
        ] = "Введите дату занятия"
        self.fields["image"].widget.attrs[
            "class"
        ] = "button icon solid fa-download"

    class Meta:
        model = Class
        labels = {"title": "Название", "description": "Описание",
                  "event_date": "Дата занятия"}
        fields = ("title", "description", "event_date", "image")
