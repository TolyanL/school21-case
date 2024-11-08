from .register_lib import register


@register.filter
def replace(value, args):
    old, new = args.split(",")
    return value.replace(old, new)
