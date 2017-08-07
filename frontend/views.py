from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from django.views import generic
from django.urls import reverse

from db_tables.models import Player

class IndexView(generic.ListView):
    template_name = 'frontend/index.html'
    context_object_name = 'new_id_user_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Player.objects.all().order_by('player_name')
