import os
import random

from django.views.generic.base import TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self):
        random.seed()
        context = {
            'my_pid': os.getpid(),
            'a_random': random.random(),
        }
        return context
