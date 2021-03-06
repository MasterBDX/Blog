import random
import string
import os
import re

from django.utils.text import slugify
from . import models


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def unique_slug_generator(instance, new_slug=None):
    ''' generate unique random slug '''

    if new_slug is not None:
        slug = new_slug
    else:
        slug = random_string_generator(size=10)

    klass = instance.__class__
    qs_exists = klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{randstr}".format(
                    randstr=random_string_generator(size=10)
                )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug


def pro_pic_random_name(title,image_name):
    slug_title = slugify(title)
    imgName,imgExt = os.path.splitext(image_name)
    random_str = random_string_generator(size=6)
    img_name = slug_title + '-' + random_str + imgExt
    img_path = os.path.join('profiles_pictures',img_name)
    return img_path

def thumbnail_random_name(title,image_name):
    slug_title = slugify(title)
    imgName,imgExt = os.path.splitext(image_name)
    random_str = random_string_generator(size=6)
    img_name = slug_title + random_str + imgExt
    img_path = os.path.join('thumbnail',img_name)
    return img_path

def date_capture(q):
    pattern = re.compile(r'((^\s*\d{4}\s*\W*\s*\d{1,2}\s*\W*\s*\d{1,2}\s*$)|(^\s*\d{1,2}\s*\W*\s*\d{1,2}\s*\W*\s*\d{4}\s*$))')
    match = pattern.match(q)
    cursor = 0
    if match:
        match = match.string
        the_date = []
        num = ''
        for d in match:
            if d.isdigit():
                num += d
                # this is the problem
                if cursor == len(match) - 1:
                    the_date.append(num)
            else:
                if num.isdigit():
                    the_date.append(num)
                    num = ''
            cursor += 1

        if len(the_date[0])==4:
            return '-'.join(the_date),True
        else:
            the_date.reverse()
            return '-'.join(the_date), True
    return None,False
