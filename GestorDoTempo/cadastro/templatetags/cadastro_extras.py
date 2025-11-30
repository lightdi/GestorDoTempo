from django import template

register = template.Library()

@register.simple_tag(takes_context=True)
def url_replace(context, **kwargs):
    query = context['request'].GET.copy()
    for k, v in kwargs.items():
        query[k] = v
    return query.urlencode()

@register.simple_tag
def is_selected(current_value, target_value):
    return 'selected' if str(current_value) == str(target_value) else ''
