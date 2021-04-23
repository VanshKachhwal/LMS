from django import template
from django.contrib.auth.models import Group

register = template.Library()

@register.filter(name = "has_group")
def has_group(user, group_name):
	group = Group.objects.get(name = group_name)
	return True if group in user.groups.all() else False

@register.filter(name = 'get_val')
def get_val(dict, key):
	return dict.get(key)

@register.filter
def index(indexable, i):
    return indexable[i]