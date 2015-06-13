from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import get_object_or_404

import sark_django.sark.models as m

# Create your views here.
def home(request):
    return redirect("/demo")
    # selected = "index"
    # t = get_template("index.html")
    # html = t.render(Context({'selected': selected}))
    # return HttpResponse(html)

def demo(request):
    selected = "demo"
    t = get_template("demo.html")
    html = t.render(Context({'selected': selected}))
    return HttpResponse(html)

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
    host = show.host.name
    date = show.date
    script = show.script.plaintext_link
    print(script)
    audio = show.audio.access_link

    with open("C:/Users/dev/PycharmProjects/sark_django/sark_django/static/sarkfiles/scripts/" + script, mode="r") as f:
        text = f.read()
    text = "<p>" + text + "</p>"
    text = text.replace("\n", "</p>\n<p>")

    t = get_template("program.html")
    html = t.render(Context({'selected': selected, 'host': host, 'date': date, 'script_text': text, 'audio': audio}))
    return HttpResponse(html)

def location(request, name, country):
    selected = "demo"
    location = get_object_or_404(m.Location, name=name, country=country)

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
                             'location_name': name_string}))
    return HttpResponse(html)
