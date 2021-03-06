from __future__ import absolute_import
import datetime

from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from haystack.views import FacetedSearchView

from ..sark import models as m


def home(request):
    return redirect("/demo")

class Demo(ListView):
    queryset = m.RadioShow.objects.order_by("date")
    # context_object_name = "radio_shows"

    def get_context_data(self, **kwargs):
        context = super(Demo, self).get_context_data(**kwargs)
        context['hosts'] = m.Agent.objects.filter(role_id=2).order_by("-dates_active").reverse()
        context['performers'] = m.Agent.objects.filter(role_id=1)
        context['locations'] = m.Location.objects.all()
        context['selected'] = "demo"
        return context

def about(request):
    selected = "about"
    t = get_template("about.html")
    html = t.render(Context({'selected': selected}))
    return HttpResponse(html)

def inventory(request):
    selected = "inventory"
    t = get_template("inventory.html")
    html = t.render(Context({'selected': selected}))
    return HttpResponse(html)

def broadcast(request, year, month, day):
    selected = "demo"

    show = get_object_or_404(m.RadioShow, date="{0}-{1}-{2}".format(year, month, day))
    performances = show.performances.all()
    photos = show.images.all()

    t = get_template("broadcast.html")
    html = t.render(Context({'selected': selected,
                             'show': show,
                             'performances': performances,
                             'photos': photos}))
    return HttpResponse(html)

def field_recording(request, unique_id):
    selected = "demo"

    recording = get_object_or_404(m.FieldRecording, unique_id=unique_id)
    performances = recording.performances.all().order_by('audio')
    images = recording.images.all()

    t = get_template("fieldrecording.html")
    html = t.render(Context({'selected': selected,
                             'recording': recording,
                             'performances': performances,
                             'images': images}))
    return HttpResponse(html)

def location(request, name, country):
    selected = "demo"
    location = get_object_or_404(m.Location, name=name, country=country)

    if name:
        people = m.Agent.objects.filter(primary_place_of_activity_id=location.pk).order_by('name')
        recordings = m.FieldRecording.objects.filter(location=location.pk).order_by('title')
    else:
        people = m.Agent.objects.filter(primary_place_of_activity__country=country).order_by('name')
        recordings = m.FieldRecording.objects.filter(location__country=country).order_by('title')

    if location.longitude and location.latitude:
        google_web_api_string = "https://www.google.com/maps/embed/v1/place?zoom={0}&center={1}%2C{2}&q={3}+{4}&key=AIzaSyDzDeB74FnjIvGAQhApW_8HVfrJSNq-nrE"
        google_web_api_string = google_web_api_string.format(location.zoom, location.latitude, location.longitude, location.name, location.country)
    else:
        google_web_api_string = "https://www.google.com/maps/embed/v1/place?zoom={0}&q={1}+{2}&key=AIzaSyDzDeB74FnjIvGAQhApW_8HVfrJSNq-nrE"
        google_web_api_string = google_web_api_string.format(location.zoom, location.name, location.country)

    t = get_template("location.html")

    html = t.render(Context({'selected': selected,
                             'google_maps_api_link': google_web_api_string,
                             'location': location,
                             'people': people,
                             'recordings': recordings}))
    return HttpResponse(html)

def agent(request, name):
    selected = "demo"
    agent = get_object_or_404(m.Agent, name=name)
    radio_shows = m.RadioShow.objects.filter(host_id=agent.pk).order_by("date")
    field_recordings = m.FieldRecording.objects.filter(performances__performers__id=agent.pk).distinct().order_by("date")
    recorded = m.FieldRecording.objects.filter(recording_engineer__id=agent.pk)
    recordings = list(radio_shows) + list(field_recordings) + list(recorded)
    members = agent.members.all()

    t = get_template("agent.html")
    html = t.render(Context({'agentdata': agent,
                             'recordings': recordings,
                             'selected': selected,
                             'members': members
                             }))

    return HttpResponse(html)

class SarkSearch(FacetedSearchView):

    def extra_context(self):
        extra = super(SarkSearch, self).extra_context()
        try:
            dates = extra['facets']['dates']['date']
            dates = sorted([[year[:4], count] for year, count in dates.items() if year.startswith("1") and count > 0], key=lambda x: -x[1])
            extra['facets']['dates']['date'] = dates
            # print(dates)
        except KeyError:
            dates = {"error", "No dates returned"}
            # extra['facets']['dates'] = dates

        try:
            for field in extra['facets']['fields']:
                if not any([int(count) > 0 for facet, count in extra['facets']['fields'][field]]):
                    extra['facets']['fields'][field] = ""
        except KeyError:
            pass

        return extra

    def get_results(self):
        if 'date_facet' in self.request.GET:
            year = int(self.request.GET['date_facet'])
            return self.form.search().filter(date__lte=datetime.date(year, 12, 31)).filter(date__gte=datetime.date(year, 1, 1))

        if 'sort' in self.request.GET:
            sort = self.request.GET['sort']
            if "date_asc" in sort:
                return self.form.search().order_by("date")
            elif "date_desc" in sort:
                return self.form.search().order_by("-date")

        return self.form.search()

def model_list(request, model):
    if "locations" in model:
        objects = m.Location.objects.all()
        headers = ["Country", "City / Area"]
        data = []
        for location in objects:
            try:
                url = reverse('sark_django.sark.views.location', kwargs={'country': location.country, 'name': location.name})
                cell_1_data = [url,  location.country]
                cell_2_data = [url, location.name]
                data.append([cell_1_data, cell_2_data])
            except:
                print("womp")

    elif "broadcasts" in model:
        objects = m.RadioShow.objects.all()
        headers = ["Show", "Host", "Date"]
        data = []
        for show in objects:
            try:
                year, day, month = str(show.date).split("-")
                broadcast_url = reverse('sark_django.sark.views.broadcast', kwargs={'year': year, 'month': month, 'day': day})
                host_url = reverse('sark_django.sark.views.agent', args=(show.host.name, ))

                cell_1_data = [broadcast_url,  show.title]
                cell_2_data = [host_url, show.host.name]
                cell_3_data = ["", str(show.date_text)]
                data.append([cell_1_data, cell_2_data, cell_3_data])
            except:
                print("womp")
    elif "fieldrecordings" in model:
        objects = m.FieldRecording.objects.all()
        headers = ["Title", "Location", "Date"]
        data = []
        for recording in objects:
            try:
                date = str(recording.date_text)
                recording_url = reverse('sark_django.sark.views.field_recording', args=(recording.unique_id, ))
                location_url = reverse('sark_django.sark.views.location', kwargs={'country': recording.location.country, 'name': recording.location.name})

                cell_1_data = [recording_url,  recording.title]
                cell_2_data = [location_url, recording.location]
                cell_3_data = ["", date]
                data.append([cell_1_data, cell_2_data, cell_3_data])
            except:
                print("womp")

    elif "performance" in model:
        pass
    elif "agent" in model:
        pass

    t = get_template('model_list.html')
    html = t.render(Context({
        'headers': headers,
        'data': data
    }))
    return HttpResponse(html)

def error404(request):
    return render(request, '404.html')
