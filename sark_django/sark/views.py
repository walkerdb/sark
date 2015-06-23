from __future__ import absolute_import
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, UpdateView
import os

from ..settings import BASE_DIR
from ..sark import models as m

# Create your views here.
def home(request):
    return redirect("/demo")
    # selected = "index"
    # t = get_template("index.html")
    # html = t.render(Context({'selected': selected}))
    # return HttpResponse(html)

class Demo(ListView):
    queryset = m.RadioShow.objects.order_by("-date").reverse()
    # context_object_name = "radio_shows"

    def get_context_data(self, **kwargs):
        context = super(Demo, self).get_context_data(**kwargs)
        context['hosts'] = m.Person.objects.filter(role_id=2).order_by("-dates_active").reverse()
        context['performers'] = m.Person.objects.filter(role_id=1)
        context['locations'] = m.Location.objects.all()
        return context

def aboutus(request):
    selected = "aboutus"
    t = get_template("aboutus.html")
    html = t.render(Context({'selected': selected}))
    return HttpResponse(html)

def aboutmtia(request):
    selected = "aboutmtia"
    t = get_template("aboutmtia.html")
    html = t.render(Context({'selected': selected}))
    return HttpResponse(html)

def inventory(request):
    selected = "inventory"
    t = get_template("inventory.html")
    html = t.render(Context({'selected': selected}))
    return HttpResponse(html)

def program(request, year, month, day):
    selected = "demo"

    show = get_object_or_404(m.RadioShow, date="{0}-{1}-{2}".format(year, month, day))
    script = show.script.plaintext_link
    performances = show.performances.all()
    photos = show.photos.all()

    with open(os.path.join(BASE_DIR, "sark_django/static/sarkfiles/scripts/") + script, mode="r") as f:
        text = f.read()

    if "<p>" not in text:
        text = "<p>" + text + "</p>"
        text = text.replace("\n", "</p>\n<p>")

    t = get_template("program.html")
    html = t.render(Context({'selected': selected,
                             'show': show,
                             'script_text': text,
                             'performances': performances,
                             'photos': photos}))
    return HttpResponse(html)

def location(request, name, country):
    selected = "demo"
    location = get_object_or_404(m.Location, name=name, country=country)
    people = m.Person.objects.filter(birthplace_id=location.pk)
    print(people)

    if location.longitude and location.latitude:
        google_web_api_string = "https://www.google.com/maps/embed/v1/place?zoom={0}&center={1}%2C{2}&q={3}+{4}&key=AIzaSyDzDeB74FnjIvGAQhApW_8HVfrJSNq-nrE"
        google_web_api_string = google_web_api_string.format(location.zoom, location.latitude, location.longitude, location.name, location.country)
    else:
        google_web_api_string = "https://www.google.com/maps/embed/v1/place?zoom={0}&q={1}+{2}&key=AIzaSyDzDeB74FnjIvGAQhApW_8HVfrJSNq-nrE"
        google_web_api_string = google_web_api_string.format(location.zoom, location.name, location.country)

    name_string = location.name + ", " + location.country
    t = get_template("location.html")

    html = t.render(Context({'selected': selected,
                             'google_maps_api_link': google_web_api_string,
                             'location_name': name_string,
                             'people': people}))
    return HttpResponse(html)

def person(request, name):
    selected = "demo"
    sark_person = get_object_or_404(m.Person, name=name)
    shows = m.RadioShow.objects.filter(host_id=sark_person.pk).order_by("-date").reverse()

    t = get_template("person.html")
    html = t.render(Context({'persondata': sark_person,
                             'shows': shows,
                             'selected': selected
                             }))

    return HttpResponse(html)
