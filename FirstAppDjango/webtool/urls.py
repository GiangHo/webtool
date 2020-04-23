from django.conf.urls import url

from webtool import views

app_name = 'webtool'
urlpatterns = [
     url(r'^$', views.index, name='index'),
     url(r'^binary_to_decimal$', views.binary_to_decimal, name = "binary_to_decimal"),
     url(r'^binary_to_hex$', views.binary_to_hex, name = "binary_to_hex"),
     url(r'^binary_to_oct$', views.binary_to_oct, name = "binary_to_oct"),
     url(r'^string_to_ascii$', views.string_to_ascii, name = "string_to_ascii"),
     url(r'^ascii_to_string$', views.ascii_to_string, name = "ascii_to_string"),
     url(r'^url_encode_decode$', views.url_encode_decode, name = "url_encode_decode"),
     url(r'^base64_encode_decode$', views.base64_encode_decode, name = "base64_encode_decode"),
     url(r'^html_encode_decode$', views.html_encode_decode, name = "html_encode_decode"),
     url(r'^json_formatter$', views.format_json, name = "json_formatter"),
     url(r'^xml_formatter$', views.format_xml, name = "xml_formatter"),
     url(r'^sql_formatter$', views.format_sql, name = "sql_formatter"),
     url(r'^xml_to_json$', views.xml_to_json, name = "xml_to_json"),
     url(r'^json_to_xml$', views.json_to_xml, name = "json_to_xml"),
     url(r'^json_to_html$', views.json_to_html, name = "json_to_html"),
     url(r'^xml_to_html$', views.xml_to_html, name = "xml_to_html"),
     url(r'^html_formatter$', views.format_html, name = "html_formatter"),
     # url(r'^check_diff$', views.check_diff, name="check_diff"),
     url(r'^string_counter$', views.string_counter, name="string_counter"),
     url(r'^string_reversal$', views.string_reversal, name="string_reversal"),
     url(r'^remove_extra_space$', views.remove_extra_space, name="remove_extra_space"),
     url(r'^remove_line_breaks$', views.remove_line_breaks, name="remove_line_breaks"),
     url(r'^remove_special_character$', views.remove_special_character, name="remove_special_character"),
     # url(r'^test$', views.test, name="test"),

     url(r'^md5_hash$', views.md5_hash, name="md5_hash"),
     url(r'^sha1_hash$', views.sha1_hash, name="sha1_hash"),
     url(r'^serialize_unserialize_php$', views.serialize_unserialize_php, name="serialize_unserialize_php"),
]

