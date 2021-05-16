import csv
from PIL import Image, ImageFont, ImageDraw 
import pathlib
import os.path
from os import path



def create_certificate(name,score,email,course_name = 0):
    '''
    This is create_certificate.py file

    it will basically create certificate according to the given data.

    it can contain 4 areguments:
      1) name of a person
      2) score he or she achieve
      3) email of a person
      4) course_name
      
    '''
    if path.exists(os.path.join((pathlib.Path().absolute()),'generated_certificate','{name}.jpg'.format(name=name))):
        return "Already Exists"
    else:
        path1 = os.path.join((pathlib.Path().absolute()),'certificate.jpg')
        title_font = ImageFont.truetype('CourierPrime-Regular.ttf', 23)
        signature_font = ImageFont.truetype('Prestige Signature Script - Demo.ttf', 35)
        if course_name != 0:
            Course_name = course_name
        else:
            Course_name = "Extensive Python & PyTorch for AI"
        date = "24th April 2021"
        sign = "Rohan Shravan"
        my_image = Image.open(path1)
        def fill_certificate(my_image,text,font,pixel,y):
            image_editable = ImageDraw.Draw(my_image)
            size_width, size_height = image_editable.textsize(text, font)
            x = pixel-(size_width/2)
            image_editable.text((x,y), text, (0, 0, 0),font=font)

        fill_certificate(my_image,Course_name,title_font,520,289)
        fill_certificate(my_image,name,title_font,520,432)
        fill_certificate(my_image,date,title_font,305,515)
        fill_certificate(my_image,sign,signature_font,736,495)
        my_image.save(os.path.join(pathlib.Path().absolute(),"generated_certificate","{name}.jpg".format(name=name)))