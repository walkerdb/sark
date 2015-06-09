from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import get_object_or_404

import sark.models as m

# Create your views here.
def home(request):
    selected = "index"
    t = get_template("index.html")
    html = t.render(Context({'selected': selected}))
    return HttpResponse(html)

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
    audio = show.audio.access_link

    with open("C:/Users/dev/PycharmProjects/sark_django/sark_django/static/sarkfiles/scripts/" + script, mode="r") as f:
        text = f.read()
    text = "<p>" + text + "</p>"
    text = text.replace("\n\n", "</p>\n<p>")

    t = get_template("program.html")
    html = t.render(Context({'selected': selected, 'host': host, 'date': date, 'script_text': text, 'audio': audio}))
    return HttpResponse(html)
