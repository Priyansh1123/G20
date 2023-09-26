from typing import Any, Dict
from django.shortcuts import render
from django.views import generic
from .models import Item,TOPIC_TYPE


class Topiclist(generic.ListView):
    queryset = Item.objects.order_by("-description")
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context =super().get_context_data(**kwargs)
        context['titles'] = TOPIC_TYPE
        return context




class TopicDetail(generic.DetailView):
    model = Item
    template_name = "detail.html"