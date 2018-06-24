#!/usr/bin/env python3.5
# # -*- coding: utf-8 -*-

"""BASED
https://www.blog.pythonlibrary.org/2017/10/17/how-to-watermark-your-photos-with-python/
"""

import logging
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from os import makedirs,listdir,remove
from os.path import splitext,exists,split



def resize_image_size(input_image_path, output_image_path, newsize):

    image = Image.open(input_image_path)
    newimage = image.resize(newsize, Image.ANTIALIAS)
    newimage.save(output_image_path)




def add_watermark_text(input_image_path,
                   output_image_path,
                   watermark_text, watermark_text_pos, watermark_text_fill, watermark_text_font):

    photo = Image.open(input_image_path)

    watermark_text_pos_width = watermark_text_pos[0]
    watermark_text_pos_height = watermark_text_pos[1]

    # make the image editable
    drawing = ImageDraw.Draw(photo)

    text_w, text_h = drawing.textsize(watermark_text, watermark_text_font)

    x_pos = watermark_text_pos_width - text_w
    if x_pos < 0: x_pos = watermark_text_pos_width

    y_pos = watermark_text_pos_height - text_h
    if y_pos < 0: y_pos = watermark_text_pos_height

    # 0,0 ---> 1920,0
    #
    #
    # 0,1280 --> 1920,0
    watermark_text_pos_real = (x_pos, y_pos)
    drawing.text(watermark_text_pos_real, watermark_text, fill=watermark_text_fill, font=watermark_text_font)
    photo.save(output_image_path)



def add_watermark_with_transparency(input_image_path,
                                output_image_path,
                                ratio_elements,
                                watermark_image_path,
                                watermark_image_pos):

    base_image = Image.open(input_image_path)
    base_image_width, base_image_height = base_image.size

    watermark = Image.open(watermark_image_path)
    watermark_width, watermark_height = watermark.size

    # resize logo
    ratio_elements_margin = ratio_elements * 1.1 # +10%

    ratio_tmp = watermark_width / base_image_width

    ratio_touse = base_image_width * ratio_elements_margin / watermark_width
    # same para watermark_height
    if ratio_tmp < ratio_elements_margin:
        ratio_touse = 1 + ratio_touse

    newsize_width = int(watermark_width * ratio_touse)
    newsize_height = int(watermark_height * ratio_touse)
    newsize = (newsize_width, newsize_height)

    watermark_image_file_fatherpath, watermark_image_file = split(watermark_image_path)
    watermark_image_file_name, watermark_image_file_extension = splitext(watermark_image_file)
    if "x" in watermark_image_file_name:
        watermark_image_file_name_split = watermark_image_file_name.split("_")
        watermark_image_file_name_withoutRes = ""
        for x in watermark_image_file_name_split[:-1]:
            watermark_image_file_name_withoutRes = watermark_image_file_name_withoutRes + str(x) + "_"
        watermark_image_file_name_withoutRes = watermark_image_file_name_withoutRes[:-1]
    else:
        watermark_image_file_name_withoutRes = watermark_image_file_name

    watermark_image_resize_output_path = watermark_image_file_fatherpath + "/" + watermark_image_file_name_withoutRes \
                                         + "_" + str(newsize_width) + "x" + str(newsize_height)\
                                         + watermark_image_file_extension

    resize_image_size(watermark_image_path, watermark_image_resize_output_path, newsize)

    # add logo to photo
    watermark = Image.open(watermark_image_resize_output_path)
    watermark_width, watermark_height = watermark.size

    watermark_image_pos_width = watermark_image_pos[0]
    watermark_image_pos_height = watermark_image_pos[1]


    transparent = Image.new('RGBA', (base_image_width, base_image_height), (0, 0, 0, 0))
    # https://github.com/python-pillow/Pillow/issues/2609#issuecomment-313841918
    transparent = transparent.convert("RGB")
    transparent.paste(base_image, (0, 0))

    x_pos = (watermark_image_pos_width - watermark_width)
    if x_pos < 0: x_pos = watermark_image_pos_width
    if x_pos >= base_image_width: x_pos = base_image_width

    y_pos = watermark_image_pos_height - watermark_height
    if y_pos < 0: y_pos = watermark_image_pos_height
    if y_pos >= base_image_height: y_pos = base_image_height

    watermark_image_pos_real = (x_pos, y_pos)

    transparent.paste(watermark, watermark_image_pos_real, mask=watermark)
    transparent.save(output_image_path)


def sign_photo(input_image_path,
                output_image_path,
                ratio_elements,
                newsize,
                watermark_text, watermark_text_pos, watermark_text_fill, watermark_text_font,
                watermark_image_path, watermark_image_pos):

    file_fatherpath, file = split(input_image_path)
    file_name, file_extension = splitext(file)
    output_tmp = file_fatherpath + "/" + "." + file_name + "_tmp" + file_extension

    resize_image_size(input_image_path,
                       output_tmp, newsize)

    add_watermark_text(output_tmp,
                       output_tmp,
                       watermark_text,
                       watermark_text_pos,
                       watermark_text_fill,
                       watermark_text_font)


    add_watermark_with_transparency(output_tmp,
                                    output_image_path,
                                    ratio_elements,
                                    watermark_image_path,
                                    watermark_image_pos)

    remove(output_tmp)


def tryit_2018(input_image_path, img_signed_folder_path):

    year = 2018

    image = Image.open(input_image_path)
    width, height = image.size


    maxwidth = 1920
    # original fotos 6000x4000 ==> maxwidth = 1920 ==> (same ratio, ratio 0.32) ==>  maxheight = 1280
    # font size = 40 ==> 40 / 1280 =>  ratio_font 0.03125
    ratio_elements = 0.03125

    ratio = maxwidth/width
    newsize_width = int(width * ratio)
    newsize_height = int(height * ratio)
    # TypeError: integer argument expected, got float
    newsize = (newsize_width, newsize_height)

    file_fatherpath, f = split(input_image_path)
    file_name, file_extension = splitext(f)
    output_image_path = img_signed_folder_path + "/" + "TryIT_" + str(year) + "_" + file_name + "_signed" + file_extension

    watermark_text = '#TRYIT2018'

    # bottom, left
    watermark_text_pos = (0, newsize_height)
    # Hex #ed1a74
    watermark_text_fill = (237, 26, 116, 1)
    watermark_text_font_path="fonts/JUST_IN_THE_FIRESTORM.TTF"

    watermark_text_font_size = int(maxwidth * ratio_elements)
    watermark_text_font = ImageFont.truetype(watermark_text_font_path, watermark_text_font_size)

    watermark_image_path="logos/tryit_2017_logo_57x57.png"
    # bottom, right
    watermark_image_pos = (newsize_width, newsize_height)

    sign_photo(input_image_path,
               output_image_path,
               ratio_elements,
               newsize,
               watermark_text, watermark_text_pos, watermark_text_fill, watermark_text_font,
               watermark_image_path, watermark_image_pos)



if __name__ == '__main__':

    img_input_folder_path = "photos_input"
    img_signed_folder_path = "photos_signed"
    valid_ext = ['.png', '.jpg']


    if not exists(img_signed_folder_path):
        makedirs(img_signed_folder_path)
    else:
        ldir = listdir(img_signed_folder_path)
        if len(ldir) > 0:
            print("There are files in the output folder: " + img_signed_folder_path)
            print("This folder has to be empty before run")
            exit(1)


    if exists(img_input_folder_path):
        ldir = listdir(img_input_folder_path)
        for f in ldir:
            file_path = img_input_folder_path + "/" + f
            file_fatherpath, f = split(file_path)
            file_name, file_extension = splitext(f)

            if file_name[0] == "." and \
                    (file_name[-4:] == "_tmp" or "_tmp" in file_name):
                print("Removing: " + file_path)
                remove(file_path)
                pass

            file_extension = file_extension.lower()
            if file_extension in valid_ext:
                tryit_2018(file_path, img_signed_folder_path)
            else:
                print("Unknown extension: " + file_path)

        if len(ldir) == 0:
            print("There is no file in the folder: " + img_input_folder_path)

    else:
        print("The folder does not exist: " + img_input_folder_path)
        exit(1)


