from django import template

register = template.Library()


# фильтры
@register.filter(name="slice")
def split_data(text, value: int):
    return text[:value]


@register.filter(name="mediapath")
def media_path(text):
    if text:
        return f'/media/{text}'
    return '../media/product/картошка.png'


# тег
@register.simple_tag(name="media_path")
def media_path(text):
    if text:
        return f'/media/{text}'
    return '../media/product/картошка.png'
