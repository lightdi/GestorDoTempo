from django import template
from django.utils.safestring import mark_safe
from django.template.defaultfilters import escapejs

register = template.Library()

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


@register.filter
def event_style(event_data):
    if event_data and 'color' in event_data:
        return f"background-color: {event_data['color']} !important; color: white; cursor: pointer;"
    return ""

@register.simple_tag
def event_attributes(event_data):
    if not event_data:
        return ""

    style_attr = ""
    if 'color' in event_data:
        style_attr = f'style="background-color: {event_data["color"]} !important; color: white; cursor: pointer;"'

    title_text = event_data.get("title", "").replace('"', '&quot;')
    title_attr = f'title="{title_text}"'

    t = escapejs(event_data.get("title", ""))
    d = escapejs(event_data.get("description", ""))
    ty = escapejs(event_data.get("type", ""))
    
    onclick_attr = f'onclick="showEventModal(\'{t}\', \'{d}\', \'{ty}\')"'

    return mark_safe(f'{style_attr} {title_attr} {onclick_attr}')
