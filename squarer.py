import os

from PIL import Image


IMAGE_EXT = ('.jpg', '.jpeg', '.png')


def main():
    for file in os.listdir('.'):
        (file_name, file_extension) = os.path.splitext(file)
        if file_extension not in IMAGE_EXT:
            continue
        image = Image.open(file)
        (width, height) = image.size
        if width != height:
            (max_side, min_side) = max(width, height), min(width, height)
            canvas = Image.new('RGB', (max_side, max_side), '#FFFFFF')
            offset = round((max_side - min_side) / 2)
            canvas.paste(image, (offset if width < height else 0, offset if width > height else 0))
            canvas.save(file_name + '-squarer' + file_extension)
        else:
            pass

if __name__ == '__main__':
    main()