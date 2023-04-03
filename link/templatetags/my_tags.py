from django import template

register = template.Library()

@register.filter(name='add_protocol')
def add_protocol(url):
    if url.startswith('http://') or url.startswith('https://'):
        return url
    else:
        return 'http://' + url