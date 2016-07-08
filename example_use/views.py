import json
import requests as req
from django.shortcuts import render
from django.views.generic import TemplateView, View, FormView
from django.shortcuts import render_to_response, redirect
from django.conf import settings
from django.http import HttpResponse
from django import forms


class SearchForm(forms.Form):
    city = forms.CharField(max_length=255, required=True)


class FormSearch(FormView):
    template_name = "form_search.html"
    form_class = SearchForm

    def post(self, request, *args, **kwargs):
        form = SearchForm(request.POST)
        error = None
        if form.is_valid():
            resp = req.get('{0}browseroutes/v1.0/{1}/{2}/{3}/{4}/{5}/{6}/{7}?apiKey={8}'.format(
                settings.LINK,
                settings.COUNTRY,
                settings.CURRENCY,
                settings.LOCALE,
                form.cleaned_data['city'],
                'anywhere',
                'anytime',
                'anytime',
                settings.API_KEY))

            if resp:
                data = resp.json()
                return render_to_response('list.html', {'routes': data['Routes'],
                                                        'carriers': data['Carriers'],
                                                        })

            else:
                error = 'error input'

        form = SearchForm()
        return render(request, 'form_search.html', {
                'form': form,
                'error': error
        })
