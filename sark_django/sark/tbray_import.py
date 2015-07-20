import csv
import os
import datetime


def get_date_info(date_text):
    date = ""
    date_approximation = ""
    if len(date_text) == 4:
        date = date_text + "-01-01"
        year, month, day = [int(item) for item in date.split("-")]
        date = datetime.date(year, month, day)
        date_approximation = m.DateApproximationLevel.objects.get(approximation="Year approximate")
    elif len(date_text) == 7:
        date = date_text + "-01"
        year, month, day = [int(item) for item in date.split("-")]
        date = datetime.date(year, month, day)
        date_approximation = m.DateApproximationLevel.objects.get(approximation="Month approximate")
    elif len(date_text) == 10:
        date = date_text
        year, month, day = [int(item) for item in date.split("-")]
        date = datetime.date(year, month, day)
        date_approximation = m.DateApproximationLevel.objects.get(approximation="Exact date")

    return date, date_approximation

def import_performances(reel_data):
    audio_location = r"H:\Sark output\audio"
    audio_files = os.listdir(audio_location)
    image_location = r"H:\Sark output\img"
    image_files = [img for img in os.listdir(image_location) if not img.endswith("thumb.jpg")]

    for reel_id, content in reel_data.items():
        try:
            x = m.FieldRecording.objects.get(unique_id=reel_id)
        except:
            title = content['reel_title']
            locations = content['locations']
            date_text = content['date']
            reel_audio_files = sorted([mp3 for mp3 in audio_files if mp3.startswith(reel_id)])
            reel_image_files = [img for img in image_files if img.startswith((reel_id))]
            num_of_audio_files = len(reel_audio_files)
            num_of_tracks = len(content['tracks'])

            r = m.FieldRecording.objects.create(title=title, unique_id=reel_id)

            if date_text:
                date, date_approximation = get_date_info(date_text)
                if date_approximation:
                    r.date_text = date_text
                    r.date = date
                    r.date_accuracy = date_approximation

            performer_1 = ""
            performer_2 = ""
            performers = content['performers']
            if len(performers) == 1:
                performer_1 = performers.pop()
            elif len(performers) == 2:
                performer_1 = performers.pop()
                performer_2 = performers.pop()

            added_tracks = []

            if num_of_tracks != num_of_audio_files:
                for i, track in enumerate(reel_audio_files):
                    p = m.Performance.objects.create(title="Track {}".format(i+1), audio="audio/{0}".format(reel_audio_files[i]))

                    if len(locations) == 1:
                        location = locations.pop()
                        if "," in location:
                            city, country = location.split(", ")
                        else:
                            city = ""
                            country = location
                    else:
                        country = ""
                        city = ""

                    if country:
                        try:
                            location = m.Location.objects.get(name=city, country=country)
                            p.location = location
                        except:
                            print("Failed country lookup - {0}, {1}".format(city, country))

                    performer_1 = ""
                    performer_2 = ""
                    if performer_1:
                        performer_1 = m.Agent.objects.get(name=performer_1)
                        p.performers.add(performer_1)
                    if performer_2:
                        performer_2 = m.Agent.objects.get(name=performer_2)
                        p.performers.add(performer_2)
                    if not performer_1 and not performer_2:
                        performer_1 = m.Agent.objects.get(name="Unknown performer(s)")
                        p.performers.add(performer_1)

                    if date_text:
                        date, date_approximation = get_date_info(date_text)
                        if date:
                            p.date = date
                            p.date_text = date_text
                            p.date_accuracy = date_approximation

                    p.save()
                    added_tracks.append(p)
                    # print(p.title)

            else:
                tracks = content['tracks']
                for i, track in enumerate(tracks):
                    track_number, track_title, duration, performer_1, performer_2, city, country, date_text = track
                    if not track_title:
                        track_title = "Track {0}".format(i + 1)
                    p = m.Performance.objects.create(title=track_title, audio="audio/{0}".format(reel_audio_files[i]))

                    if performer_1:
                        performer_1 = m.Agent.objects.get(name=performer_1)
                        p.performers.add(performer_1)
                    if performer_2:
                        performer_2 = m.Agent.objects.get(name=performer_2)
                        p.performers.add(performer_2)
                    if not performer_1 and not performer_2:
                        performer_1 = m.Agent.objects.get(name="Unknown performer(s)")
                        p.performers.add(performer_1)

                    if country:
                        try:
                            location = m.Location.objects.get(name=city, country=country)
                            p.location = location
                        except:
                            print("Failed country lookup - {0}, {1}".format(city, country))

                    date, date_approximation = get_date_info(date_text)
                    if date:
                        p.date = date
                        p.date_accuracy = date_approximation
                        p.date_text = date_text

                    p.save()
                    # print(p.title)
                    added_tracks.append(p)

            for track in added_tracks:
                r.performances.add(track)

            order = ['accnotes_01', 'accnotes_02', 'accnotes_03', 'boxfront', 'reelfront', 'reelback', 'boxback', 'boxleft', 'boxtop', 'boxright', 'boxbottom']
            for img in reel_image_files:
                try:
                    thumb_path = "img/{0}-thumb.jpg".format(img.split(".")[0])
                    path = "img/{0}".format(img)
                    sort_order = 15
                    for i, element in enumerate(order):
                        if element in path:
                            sort_order = i
                            break

                    i = m.Image.objects.create(file=path, thumb=thumb_path, sort_order=sort_order)
                    r.images.add(i)
                except:
                    print("image add failure")

            if len(locations) == 1:
                location = locations.pop()
                if "," in location:
                    city, country = location.split(", ")
                else:
                    city = ""
                    country = location
                try:
                    l = m.Location.objects.get(name=city, country=country)
                    r.location = l
                except:
                    print("Location add fail")

            r.save()

def import_performer(performer):
    role = m.Role.objects.get(role="Performer")
    p, created = m.Agent.objects.get_or_create(name=performer, role=role)
    if created:
        print("created {}".format(p))


def import_location(location):
    if "," in location:
        city, country = location.split(", ")
    else:
        country = location
        city = ""
    p, created = m.Location.objects.get_or_create(name=city, country=country)
    if created:
        print("created {0}".format(p))

def get_reel_data(csv_location):
    reels = {}
    with open(csv_location, mode="r") as f:
        reader = csv.reader(f)
        next(reader)

        for row in reader:
            barcode = row[BARCODE].strip("-")
            date = row[DATE].strip("-").lstrip("c.")
            city = row[CITY].strip("-")
            country = row[COUNTRY].strip("-")
            performer_1 = row[PERFORMER_1].strip("-")
            performer_2 = row[PERFORMER_2].strip("-")
            track_number = row[TRACK_NUM].strip("-")
            track_title = row[PIECE_TITLE].strip("-")
            reel_title = row[REEL_TITLE].strip("-")
            duration = row[DURATION].strip("-")

            if barcode:
                reels[barcode] = reels.get(barcode, {'reel_title': reel_title, 'tracks': [], 'performers': set(), 'locations': set(), 'date': date})
                reels[barcode]['tracks'].append((track_number, track_title, duration, performer_1, performer_2, city, country, date))
                if performer_2:
                    reels[barcode]['performers'].add(performer_2)
                if performer_1:
                    reels[barcode]['performers'].add(performer_1)
                if city:
                    reels[barcode]['locations'].add(", ".join([city, country]))
                elif country:
                    reels[barcode]['locations'].add(country)

    return reels


def get_perf_loc(csv_location):
    performers = set()
    locations = set()
    with open(csv_location, mode="r") as f:
        reader = csv.reader(f)
        next(reader)

        for row in reader:
            performer_1 = row[PERFORMER_1].strip("-")
            performer_2 = row[PERFORMER_2].strip("-")
            if performer_1:
                performers.add(performer_1)
            if performer_2:
                performers.add(performer_2)

            country = row[COUNTRY].strip("-")
            city = row[CITY].strip("-")
            if country and city:
                locations.add(country)
                locations.add("{0}, {1}".format(city, country))
            elif country:
                locations.add(country)

        # print(performers)
        # print(len(performers))
        #
        # print(locations)
        # print(len(locations))

    return performers, locations


BARCODE, CATALOG_NUM, DATE, CITY, COUNTRY, TRACK_NUM, PERFORMER_1, PERFORMER_2, PIECE_TITLE, REEL_TITLE, SINGER, DURATION, STYLE, COMPOSER = range(14)

if __name__ == "__main__":
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sark_django.settings')
    from sark_django.sark import models as m
    import django
    django.setup()

    csv_location = r'C:\Users\dev\Downloads\field_recording_data.csv'
    performers, locations = get_perf_loc(csv_location)

    reel_data = get_reel_data(csv_location)
    #
    # for location in locations:
    #     import_location(location)
    #
    # for performer in performers:
    #     import_performer(performer)
    #
    import_performances(reel_data)