import os
from collections import namedtuple
import re
import subprocess

from mutagen.easyid3 import EasyID3
from PIL import Image


def convert_wav_to_mp3(filepath, notes=""):
    '''
    Given the path to a preservation .wav file, creates a derivative high-quality variable bit-rate .mp3
    Optionally takes a filepath to a file containing metadata, in Tom Bray's line-delineated format, adding that
    data to the mp3 file
    :param filepath:
    :param notes:
    :return:
    '''
    metadata = ""
    if notes:
        metadata = get_audio_metadata(notes)
        print(metadata)
        if metadata.title not in filepath:
            print("barcodes do not match!")

    print("working on {0}...".format(filepath))

    path_, filename = os.path.split(filepath)
    filename = filename.split(".")[0]
    barcode = metadata.title
    print(barcode)
    output_filename = "{0}-{1}.mp3".format(barcode, filename)

    subprocess.call(['ffmpeg', '-y', '-f', 'wav', '-i', filepath, '-ar', '48000', '-vn', '-aq', '0', '-f', 'mp3', os.path.join(path_, output_filename)])

    id3 = EasyID3(os.path.join(path_, output_filename))
    id3["title"] = metadata.title + "-" + filename
    id3["album"] = metadata.album
    id3["date"] = metadata.year
    id3.save()


def get_audio_metadata(filepath):
    '''
    Given a specifically-formatted metadata file, returns a namedtuple containing the title, album, comments, and year
    :param filepath:
    :return:
    '''
    Metadata = namedtuple("Metadata", ["title", "album", "comments", "year"])
    year_regex = r"19[56789]\d|'[56789]\d"
    with open(filepath, mode="r") as f:
        data = f.readlines()
        album_name = data[3].strip()
        barcode = data[0].strip()
        capture_notes = data[15].strip()
        year = re.findall(year_regex, album_name)
        if year:
            year = year[0]
            if len(year) == 3:
                year = "19" + year.strip("'")
        else:
            year = ""

        return Metadata(title=barcode, album=album_name, comments=capture_notes, year=year)


def make_thumbnail(input_filepath, output_dir="", barcode=""):
    '''
    Given an input image, creates a 200x200 px thumbnail for web purposes
    :param input_filepath: path to the image from which to make the thumbnail
    :param output_dir: where to save the derived files to
    :param barcode: will be prefixed to the input file-name
    '''

    size = 200, 200
    try:
        print(input_filepath)
        path_, filename = os.path.split(input_filepath)
        filename = filename.split(".")[0]
        outfile = "{0}-{1}.jpg".format(os.path.join(output_dir, barcode), filename)
        im = Image.open(input_filepath)
        im.save(outfile, "JPEG", quality=90)

        outfile = "{0}-{1}-thumb.jpg".format(os.path.join(output_dir, barcode), filename)
        im.thumbnail(size, Image.ANTIALIAS)
        im.save(outfile, "JPEG")

    except IOError:
        print("cannot create thumbnail for '%s'" % input_filepath)


if __name__ == "__main__":
    input_dir = r"H:\Sarkisian - TBray digitization\All digitized files, by barcode"
    output_dir = r"H:\Sark output\img"

    for folder in os.listdir(input_dir):

        image_files = [image_file for image_file in os.listdir(os.path.join(input_dir, folder)) if image_file.endswith(".tiff") or image_file.endswith(".tif")]
        for image in image_files:
            path = os.path.join(os.path.join(input_dir, folder), image)
            make_thumbnail(path, output_dir=output_dir, barcode=folder)

        audio_files = [audio_file for audio_file in os.listdir(os.path.join(input_dir, folder)) if audio_file.endswith(".wav") and audio_file.startswith("pm")]
        for wav in audio_files:
            audio_path = os.path.join(input_dir, wav)
            notes_path = os.path.join(input_dir, "notes.txt")
            convert_wav_to_mp3(audio_path, notes_path)
