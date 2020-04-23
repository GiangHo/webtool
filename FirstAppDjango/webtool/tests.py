# -*- coding: utf-8 -*-
# import json
#
# import lxml.html
# import pandas
# from json2html import json2html
# from lxml import etree
# string_value = "<note><to>Tove</to><from>Jani</from><heading>Reminder</heading><body>Don't forget me this weekend!</body></note>"
# jsonfile_tmp = "{\"person\": [{\"name\": \"lacquay\", \"age\": 23, \"address\": \"DongAnh\"}, {\"name\": \"lacquay\", \"age\": 23, \"address\": \"DongAnh\"}]}"
# jsonfile = "{\"menu\": {\"id\": \"file\",\"value\": \"File\",\"popup\": {\"menuitem\": [{\"value\": \"New\", \"onclick\": \"CreateNewDoc()\"},{\"value\": \"Open\", \"onclick\": \"OpenDoc()\"},{\"value\": \"Close\", \"onclick\": \"CloseDoc()\"}]}}}"
# print pandas.read_json(jsonfile)
# result = pandas.DataFrame(pandas.read_json(jsonfile))
# print result
# print result.to_csv(index=False)
# data = json.loads(jsonfile)
# normalized_df = pandas.io.json.json_normalize(data)
# print normalized_df.to_csv(index=False)
# import hashlib
#
# # print hashlib.md5('minhgiang'.encode()).hexdigest()
# m = hashlib.sha1("minhgiang".encode()).hexdigest()
# print m
# import json
# from phpserialize import serialize, unserialize
# str = serialize("{'loginip': '127.0.0.1', 'uid': 96, 'loginfrom': 4, 'logintime': 1317200595}")
# print str
# print unserialize(str)
import HTMLParser
from lxml import etree

from django.utils.html import escape
# html_parser = HTMLParser.HTMLParser()
# my_string= "<head>name</head>"
# b =escape(my_string)
# print(b)
# unescaped = html_parser.unescape(b)
# print unescaped

# from lxml import etree, html
#
# document_root = html.fromstring("<html><body><h1>hello world</h1></body></html>")
# print(etree.tostring(document_root, encoding='unicode', pretty_print=True))


import xml.dom.minidom as xmlformatter
# xml_load = dicttoxml(json.loads("{ "name":"John", "age":30, "car":null }"), attr_type=False).replace("<root>", "").replace("</root>", "")
xml_load = "<?xml version=\"1.0\" encoding=\"UTF-8\" ?><car>abc</car><age>30</age><name>John</name>"
print "xml_load", xml_load
# xml = xmlformatter.parseString(xml_load)
# print "xml", xml
# xml_pretty_str = xml.toprettyxml()
# print "xml_pretty_str", xml_pretty_str

# print (etree.tostring(xml_load, pretty_print=True))
import xml.dom.minidom

xml = xml.dom.minidom.parse(xml_load) # or xml.dom.minidom.parseString(xml_string)
pretty_xml_as_string = xml.toprettyxml()
