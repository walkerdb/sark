from PIL import Image
import os


def make_thumbnail(input_filepath):

    size = 200, 200
    try:
        print(input_filepath)
        outfile = os.path.splitext(input_filepath)[0] + ".jpg"
        im = Image.open(input_filepath)
        im.save(outfile, "JPEG")

        outfile = os.path.splitext(input_filepath)[0] + "-thumb.jpg"
        im.thumbnail(size, Image.ANTIALIAS)
        im.save(outfile, "JPEG")

    except IOError:
        print("cannot create thumbnail for '%s'" % input_filepath)


if __name__ == "__main__":
    input_dir = r"H:\Sarkisian - TBray digitization\All digitized files, by barcode\39015087085653"
    files = [file for file in os.listdir(input_dir) if file.endswith(".tif")]
    for file in files:
        path = os.path.join(input_dir, file)
        make_thumbnail(path)