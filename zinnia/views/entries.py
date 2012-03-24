"""Views for Zinnia entries"""
from django.views.generic.date_based import object_detail as date_object_detail
from django.views.generic.list_detail import object_detail

from zinnia.views.decorators import protect_entry, protect_category_entry


entry_category_detail = protect_category_entry(object_detail)
entry_detail = protect_entry(date_object_detail)