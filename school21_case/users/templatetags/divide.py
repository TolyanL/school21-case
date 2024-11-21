from .register_lib import register


@register.filter
def divide(value, divisor):
    if divisor == 0:
        return 0
    return round(value / divisor)
