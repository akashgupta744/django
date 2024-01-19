from django import template
register = template.Library()


def swap(value):
    return value.swapcase()


@register.filter('counting')
def count(value,arg):
    c=0
    for i in range(len(value)):
        if arg == value[i:len(arg)+i:1]:
            c+=1
    return c

@register.filter()
def remove(value, arg):
    return value.replace(arg,'')


register.filter('swapcase',swap)