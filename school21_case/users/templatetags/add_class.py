from .register_lib import register


@register.filter
def add_class(field, css_class):
    return field.as_widget(attrs={"class": css_class})
