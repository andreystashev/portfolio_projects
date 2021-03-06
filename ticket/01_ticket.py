# -*- coding: utf-8 -*-
import os
from PIL import Image, ImageDraw, ImageFont, ImageColor


# Заполнить все поля в билете на самолет.
# Создать функцию, принимающую параметры: ФИО, откуда, куда, дата вылета,
# и заполняющую ими шаблон билета Skillbox Airline.
# Шаблон взять в файле lesson_013/images/ticket_template.png
# Пример заполнения lesson_013/images/ticket_sample.png
# Подходящий шрифт искать на сайте ofont.ru


def make_ticket(fio, from_, to, date):
    template = 'images/ticket_template.png'
    font_path = os.path.join('fonts', 'ofont.ru_Frusta.ttf')
    im = Image.open(template)
    w, h = im.size
    im = im.resize((w, h))
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype(font_path, size=18)
    y = im.size[1] - 220 - (10 + font.size) * 2
    message = f'{fio}'
    draw.text((50, y), message, font=font, fill=ImageColor.colormap['black'])
    y = im.size[1] - 188 - font.size
    message = f'{from_}'
    draw.text((50, y), message, font=font, fill=ImageColor.colormap['black'])
    y = im.size[1] - 122 - font.size
    message = f'{to}'
    draw.text((50, y), message, font=font, fill=ImageColor.colormap['black'])
    y = im.size[1] - 125 - font.size
    message = f'{date}'
    draw.text((285, y), message, font=font, fill=ImageColor.colormap['black'])
    out_path = 'final_ticket.png'
    im.save(out_path)
    print(f'Post card saved az {out_path}')

# make_ticket('Andrey','Moscow','Washington','12.12.2021')

