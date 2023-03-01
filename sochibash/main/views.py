from django.views.generic.base import TemplateView


class MainView(TemplateView):
    template_name = 'main/index.html'


class ContactView(TemplateView):
    template_name = 'main/contact.html'


class ElementsView(TemplateView):
    template_name = 'main/elements.html'


class GenericView(TemplateView):
    template_name = 'main/generic.html'
