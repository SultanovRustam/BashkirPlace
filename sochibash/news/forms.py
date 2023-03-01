from django.forms import ModelForm

from .models import News


class NewsForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["title"].widget.attrs[
            "placeholder"
        ] = "Введите заголовок новости"
        self.fields["text"].widget.attrs[
            "placeholder"
        ] = "Введите  текст новости"
        self.fields["image"].widget.attrs[
            "class"
        ] = "button icon solid fa-download"

    class Meta:
        model = News
        labels = {"title": "Заголовок", "text": "Текст новости"}
        fields = ("title", "text", "image")
