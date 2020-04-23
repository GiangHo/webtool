# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import sys

import hashlib
import traceback
from cgi import escape

import sqlparse
from bs4 import BeautifulSoup
from dicttoxml import dicttoxml
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.encoding import smart_unicode
from json2html import json2html
from phpserialize import serialize, unserialize
from lxml import etree, html
import xml.etree.ElementTree as ET

from handle.convert_binary_to_decimal import convert_binary_to_decimal
import json
import urllib
import base64
import xml.dom.minidom as xmlformatter
import xmltodict
import HTMLParser

def index(request):
    return render(request, "index.html")
def test(request):
    return render(request, "test.html")

def string_reversal(request):
    try:
        input_value = request.POST.get("inputValue")
        reversal_string = "input invalid"
        try:
            if input_value is not None:
                list_output = input_value.split(" ")
                for i in range(len(list_output)-1, -1, -1):
                    if reversal_string == "":
                        reversal_string = list_output[i]
                    else:
                        reversal_string = reversal_string + " " + list_output[i]
            data_result = {
                "input_value": input_value,
                "output_value": reversal_string
            }
        except:
            data_result = {
                "input_value": input_value,
                "output_value": "input invalid"
            }
        return render(request, "string_reversal.html", {"post": data_result})
    except:
        return render(request, "page404.html")

def remove_extra_space(request):
    try:
        input_value = request.POST.get("inputValue")
        output_string = "input invalid"
        try:
            if input_value is not None:
                output_string = " ".join(input_value.split())
            data_result = {
                "input_value": input_value,
                "output_value": output_string
            }
        except:
            data_result = {
                "input_value": input_value,
                "output_value": "input invalid"
            }
        return render(request, "remove_extra_space.html", {"post": data_result})
    except:
        return render(request, "page404.html")

def remove_line_breaks(request):
    try:
        input_value = request.POST.get("inputValue")
        output_string = "input invalid"
        try:
            if input_value is not None:
                remove_line = input_value.replace('\r', ' ').replace('\n', ' ')
                output_string = " ".join(remove_line.split())
            data_result = {
                "input_value": input_value,
                "output_value": output_string
            }
        except:
            data_result = {
                "input_value": input_value,
                "output_value": "input invalid"
            }
        return render(request, "remove_line_breaks.html", {"post": data_result})
    except:
        return render(request, "page404.html")

def remove_special_character(request):
    try:
        input_value = request.POST.get("inputValue")
        character_value = request.POST.get("characterRemove")
        print "character_value", character_value
        print input_value
        output_string = "input invalid"
        try:
            if input_value is not None and character_value is not None:
                print "character_value_2", character_value
                output_string = input_value.replace(str(character_value), '')
            data_result = {
                "input_value": input_value,
                "output_value": output_string,
                "character_value": character_value
            }
        except:
            data_result = {
                "input_value": input_value,
                "character_value": character_value,
                "output_value": "input invalid"
            }
        return render(request, "remove_special_character.html", {"post": data_result})
    except:
        return render(request, "page404.html")

def md5_hash(request):
    try:
        input_value = request.POST.get("inputValue")
        output_string = "input invalid"
        try:
            if input_value is not None:
                output_string = hashlib.md5(str(input_value).encode()).hexdigest()
            data_result = {
                "input_value": input_value,
                "output_value": output_string
            }
        except:
            data_result = {
                "input_value": input_value,
                "output_value": "input invalid"
            }
        return render(request, "md5_hash.html", {"post": data_result})
    except:
        return render(request, "page404.html")

def sha1_hash(request):
    try:
        input_value = request.POST.get("inputValue")
        output_string = "input invalid"
        try:
            if input_value is not None:
                output_string = hashlib.sha1(str(input_value).encode()).hexdigest()
            data_result = {
                "input_value": input_value,
                "output_value": output_string
            }
        except:
            data_result = {
                "input_value": input_value,
                "output_value": "input invalid"
            }
        return render(request, "sha1_hash.html", {"post": data_result})
    except:
        return render(request, "page404.html")

def serialize_unserialize_php(request):
    try:
        input_value = request.POST.get("inputValue")
        output_value = "input invalid"

        data_result = {
            "input_value": output_value,
            "output_value": "input invalid"
        }
        print "kq ", request.POST
        try:
            if "serialize" in request.POST and input_value is not None:
                serialize_output = serialize(input_value)
                data_result = {
                    "input_value": input_value,
                    "output_value": serialize_output
                }
            elif "unserialize" in request.POST and input_value is not None:
                print "vao"
                unserialize_output = unserialize(input_value)
                data_result = {
                    "input_value": input_value,
                    "output_value": unserialize_output
                }

        except:
            data_result = {
                "input_value": "",
                "output_value": "input invalid"
            }
        return render(request, "serialize_unserialize_php.html", {"post": data_result})
    except:
        return render(request, "page404.html")
